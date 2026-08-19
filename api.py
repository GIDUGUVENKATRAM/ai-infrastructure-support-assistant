import logging
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
client = OpenAI()

class SupportRequest(BaseModel):
    issue: str

@app.get("/health")
def health_check():
    return {"status": "ok "}

@app.post("/support")
def support(request: SupportRequest):
    logger.info("Support request received")
    try:
        logger.info("Sending request to LLM")

        response = client.responses.create(
            model = "gpt-5.6",
            input = request.issue
        )
        logger.info("LLM response received successfully")


        return{
             "response": response.output_text
         }
    except Exception:
        logger.exception("LLM request failed")
        raise HTTPException(
            status_code=500,
            detail="AI Service request failed"
        )
    