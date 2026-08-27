import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

project = AIProjectClient(
    endpoint=os.getenv("FOUNDRY_PROJECT_ENDPOINT"),
    credential=DefaultAzureCredential()
)

openai = project.get_openai_client()

response = openai.responses.create(
    input=(
        "What is the escalation code for sustained VDI CPU "
        "above 90% for more than five minutes?"
    ),
    extra_body={
        "agent_reference": {
            "name": "fde-support-agent",
            "type": "agent_reference"
        }
    }
)

print("\nANSWER:")
print(response.output_text)

print("\nOUTPUT ITEMS:")
for item in response.output:
    print(item)