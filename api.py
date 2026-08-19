from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

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
    try:
        response = client.responses.create(
            model = "gpt-5.6",
            input = request.issue
        )

        return{
             "response": response.output_text
         }
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="AI Service request failed"
        )
    