from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
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
    