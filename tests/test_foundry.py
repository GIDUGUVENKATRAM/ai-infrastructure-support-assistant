import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("FOUNDRY_ENDPOINT")
deployment_name = "gpt-4.1-mini"
api_key = os.getenv("FOUNDRY_API_KEY")

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    input="Use not able to login to linux server",
)

print(f"answer: {response.output[0]}")
