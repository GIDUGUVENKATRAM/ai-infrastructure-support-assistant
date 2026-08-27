import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition, MCPTool


PROJECT_ENDPOINT = os.getenv("FOUNDRY_PROJECT_ENDPOINT")

MCP_SERVER_URL = "https://fde-ai-support-mcp.livelyfield-7bca1320.eastus.azurecontainerapps.io/mcp"

project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

mcp_tool = MCPTool(
    server_label="fde-support-mcp",
    server_url=MCP_SERVER_URL,
    require_approval="never",
)

agent = project.agents.create_version(
    agent_name="fde-support-mcp-test-agent",
    definition=PromptAgentDefinition(
        model="gpt-4.1-mini",
        instructions=(
            "You are an infrastructure support agent. "
            "Use the MCP tools when infrastructure health information is required."
        ),
        tools=[mcp_tool],
    ),
)

print(
    f"Agent created: {agent.name}, "
    f"version: {agent.version}"
)
openai = project.get_openai_client()

response = openai.responses.create(
    tool_choice="required",
    input=(
        "Check the health of VDI-APP-01 using the available MCP tool. "
        "Tell me the CPU, memory, active sessions, and status."
    ),
    extra_body={
        "agent_reference": {
            "name": agent.name,
            "type": "agent_reference"
        }
    }
)

print("\nAgent response:")
print(response.output_text)