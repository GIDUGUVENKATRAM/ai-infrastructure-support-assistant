import logging
import os

import fastapi
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.monitor.opentelemetry import configure_azure_monitor
from dotenv import load_dotenv
from fastapi.responses import FileResponse, JSONResponse
from openai import OpenAI
from pydantic import BaseModel, Field
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address


# Load environment variables and enable Azure monitoring
load_dotenv()
configure_azure_monitor()

logging.basicConfig(level=logging.INFO)

logging.getLogger(
    "azure.core.pipeline.policies.http_logging_policy"
).setLevel(logging.WARNING)

logging.getLogger(
    "azure.monitor.opentelemetry.exporter"
).setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

app = fastapi.FastAPI()


# Required environment configuration
API_KEY = os.getenv("FDE_API_KEY")
FOUNDRY_ENDPOINT = os.getenv("FOUNDRY_ENDPOINT")
FOUNDRY_API_KEY = os.getenv("FOUNDRY_API_KEY")
FOUNDRY_PROJECT_ENDPOINT = os.getenv("FOUNDRY_PROJECT_ENDPOINT")

if not API_KEY:
    raise RuntimeError("FDE_API_KEY environment variable is not set")

if not FOUNDRY_ENDPOINT:
    raise RuntimeError("FOUNDRY_ENDPOINT environment variable is not set")

if not FOUNDRY_API_KEY:
    raise RuntimeError("FOUNDRY_API_KEY environment variable is not set")

if not FOUNDRY_PROJECT_ENDPOINT:
    raise RuntimeError(
        "FOUNDRY_PROJECT_ENDPOINT environment variable is not set"
    )


# Direct model client used by /support
client = OpenAI(
    base_url=FOUNDRY_ENDPOINT,
    api_key=FOUNDRY_API_KEY
)


# Foundry project client used by /demo/support
project = AIProjectClient(
    endpoint=FOUNDRY_PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(
        managed_identity_client_id="a6f00f4a-6aa5-4153-bd13-0f249a7a42af"
    )
)

agent_client = project.get_openai_client()


# Rate limiting for public demo endpoint
limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.add_exception_handler(
    RateLimitExceeded,
    lambda request, exc: JSONResponse(
        status_code=429,
        content={
            "detail": "Too many requests. Please try again later."
        }
    )
)


# Request validation
class SupportRequest(BaseModel):
    issue: str = Field(
        min_length=3,
        max_length=4000
    )


# Serve demo webpage
@app.get("/")
def home():
    return FileResponse("static/index.html")


# Health check
@app.get("/health")
def health_check():
    return {"status": "ok"}


# Protected direct-model API
@app.post("/support")
def support(
    request: SupportRequest,
    x_api_key: str = fastapi.Header(...)
):
    if x_api_key != API_KEY:
        raise fastapi.HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    logger.info("Protected support request received")

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=request.issue,
            max_output_tokens=500
        )

        logger.info("Protected LLM response received successfully")

        return {
            "response": response.output_text
        }

    except Exception:
        logger.exception("Protected LLM request failed")

        raise fastapi.HTTPException(
            status_code=500,
            detail="AI Service request failed"
        )


# Public demo endpoint
#
# Web UI
#   -> FastAPI
#   -> fde-support-agent
#   -> agent decides whether to use RAG / tools
#   -> response
@app.post("/demo/support")
@limiter.limit("5/minute")
def demo_support(
    request: fastapi.Request,
    support_request: SupportRequest
):
    logger.info("Demo support request received")

    try:
        response = agent_client.responses.create(
            input=support_request.issue,
            max_output_tokens=500,
            extra_body={
                "agent_reference": {
                    "name": "fde-support-agent",
                    "type": "agent_reference"
                }
            }
        )

        logger.info("Foundry agent response received successfully")

        return {
            "response": response.output_text
        }

    except Exception as e:
        print(
            f"FOUNDRY_AGENT_ERROR: {type(e).__name__}: {str(e)}",
            flush=True
        )

        logger.exception("Foundry agent request failed")

        raise fastapi.HTTPException(
            status_code=500,
            detail="AI Agent request failed"
        )