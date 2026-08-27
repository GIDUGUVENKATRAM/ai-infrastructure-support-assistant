# AI Infrastructure Support Assistant

An end-to-end AI infrastructure support application built with FastAPI, Microsoft Foundry, RAG, agent tools, MCP, Docker, Azure Container Apps, managed identity, and Azure observability.

The project was designed as an FDE-style hands-on system that goes beyond a basic chatbot by combining retrieval, tool use, cloud deployment, API security, observability, and production-oriented hardening.

## What It Does

Users can submit infrastructure and VDI support issues through a web interface.

The application can:

- provide AI-assisted troubleshooting guidance;
- retrieve internal infrastructure knowledge through RAG;
- return organization-specific escalation guidance;
- invoke external infrastructure tools through a Foundry agent;
- expose MCP-based infrastructure health capabilities;
- run as a containerized application in Azure;
- use managed identity for Azure-to-Azure authentication;
- capture application and agent telemetry through Azure monitoring.

A validated RAG example is retrieving the escalation code:

```text
VDI-PERF-17
```

for sustained VDI CPU utilization above 90% for more than five minutes.

---

## Architecture

```text
                         User
                           |
                           v
                    Web Interface
                  HTML / CSS / JS
                           |
                           v
                       FastAPI
                 Azure Container App
                           |
                           v
                Microsoft Foundry Agent
                           |
              +------------+------------+
              |            |            |
              v            v            v
             LLM          RAG          Tools
                       / Knowledge       |
                                        v
                               Infrastructure APIs
                                      / MCP
                           |
                           v
                      AI Response
                           |
                           v
                        User
```

Deployment flow:

```text
Source Code
    |
    v
Docker
    |
    v
Azure Container Registry
    |
    v
Azure Container Apps
```

Azure authentication flow:

```text
Container App
     |
     v
User-Assigned Managed Identity
     |
     v
Microsoft Foundry
```

For a more detailed technical walkthrough, see:

`docs/architecture.md`

---

## Key Features

### FastAPI Backend

The application exposes:

```text
GET  /health
POST /support
POST /demo/support
```

`/support` is protected by an API key.

`/demo/support` is connected to the Microsoft Foundry agent and is used by the public demonstration UI.

### Microsoft Foundry Agent

The `fde-support-agent` acts as the orchestration layer.

It can determine whether a support request requires:

- model reasoning;
- internal knowledge retrieval;
- RAG;
- an external API or tool.

### Retrieval-Augmented Generation

The agent uses infrastructure-specific knowledge rather than relying only on general model knowledge.

Example validated internal knowledge includes VDI troubleshooting thresholds and escalation codes such as:

```text
VDI-PERF-17
VDI-MEM-22
VDI-NET-31
```

### OpenAPI Tool Integration

The Foundry agent can invoke the protected FastAPI support API through an OpenAPI tool.

The tool uses an `x-api-key` header configured securely through the Foundry connection.

### MCP Integration

The project includes a separate MCP server:

```text
mcp_server.py
```

and MCP-specific container configuration:

```text
Dockerfile.mcp
```

The MCP service demonstrates how infrastructure health functionality can be exposed to AI agents through a standardized tool protocol.

### Web Interface

A lightweight HTML, CSS, and JavaScript frontend provides a recruiter/demo-friendly interface.

The UI:

- accepts infrastructure support issues;
- checks backend health;
- sends requests to `/demo/support`;
- displays AI responses.

### Azure Deployment

The application is containerized and deployed using:

- Docker
- Azure Container Registry
- Azure Container Apps

### Managed Identity

The deployed application uses a user-assigned managed identity to authenticate from Azure Container Apps to Microsoft Foundry.

This avoids storing developer Azure credentials inside the container.

### Observability

The project integrates:

- Azure Monitor
- Application Insights
- OpenTelemetry
- application logging
- Container App log streaming
- Foundry tracing

### Application Hardening

The project includes:

- environment-based secret configuration;
- `.env` excluded from Git;
- API-key protection;
- Pydantic request validation;
- input length limits;
- output token limits;
- rate limiting on the public demo endpoint;
- sanitized client-facing errors;
- backend exception logging.

---

## Technology Stack

### Application

- Python
- FastAPI
- Pydantic
- HTML / CSS / JavaScript

### AI

- Microsoft Foundry
- Foundry Agents
- OpenAI-compatible Responses API
- RAG / Knowledge
- OpenAPI tools
- MCP

### Azure

- Azure Container Apps
- Azure Container Registry
- User-Assigned Managed Identity
- Azure Monitor
- Application Insights
- OpenTelemetry

### DevOps / Engineering

- Docker
- Git
- GitHub
- Azure CLI

---

## Repository Structure

```text
ai-infrastructure-support-assistant/
|
├── api.py
├── mcp_server.py
├── Dockerfile
├── Dockerfile.mcp
├── requirements.txt
|
├── static/
│   └── index.html
|
├── tests/
│   ├── test_agent_rag.py
│   ├── test_foundry.py
│   ├── test_foundry_mcp.py
│   └── test_llm.py
|
├── examples/
│   └── cli_prototype.py
|
└── docs/
    ├── architecture.md
    ├── architecture-history.md
    ├── troubleshooting.md
    ├── learning-notes.md
    └── interview-notes.md
```

---

## Example Request Flow

A typical request follows this path:

```text
1. User enters an infrastructure issue in the browser.

2. The web interface sends:
   POST /demo/support

3. FastAPI validates the request.

4. FastAPI authenticates to Microsoft Foundry using
   the Container App's user-assigned managed identity.

5. The request is sent to the Foundry agent.

6. The agent decides whether it needs:
   - direct reasoning;
   - RAG / internal knowledge;
   - an external tool.

7. The required context or tool result is retrieved.

8. The agent generates the final response.

9. FastAPI returns the response to the browser.

10. Logs and traces are available through Azure observability.
```

---

## Example Support Questions

```text
A user reports that their VDI session is very slow and
applications are taking a long time to open. What should I check?
```

```text
What is the escalation code for sustained VDI CPU above 90%
for more than five minutes?
```

```text
Use the fde_support_api tool to analyze a Linux VM experiencing
sustained high CPU utilization and degraded application response time.
```

---

## Project Evolution

The project was developed incrementally:

```text
Python CLI
    ↓
LLM Integration
    ↓
FastAPI REST API
    ↓
Docker
    ↓
Azure Deployment
    ↓
Observability
    ↓
RAG
    ↓
MCP
    ↓
Foundry Agent + Tools
    ↓
Managed Identity
    ↓
Web Demo
    ↓
Application Hardening
```

Earlier architecture stages are preserved in:

`docs/architecture-history.md`

---

## Key Engineering Lesson

One important deployment issue appeared when the agent worked locally but failed inside Azure Container Apps.

Locally, `DefaultAzureCredential` could use the developer's Azure login.

Inside Azure, the application used a user-assigned managed identity and needed that identity to be selected explicitly.

The issue was diagnosed through Container App logs and fixed by configuring the credential to use the correct managed identity client ID.

This reinforced the difference between:

```text
Local developer authentication
```

and:

```text
Cloud workload identity
```

---

## Current Status

The project currently includes:

- working FastAPI backend;
- deployed Azure web application;
- Microsoft Foundry agent integration;
- RAG with internal infrastructure knowledge;
- OpenAPI tool calling;
- MCP service;
- managed identity authentication;
- Azure observability;
- request validation and rate limiting;
- Docker-based Azure deployment;
- recruiter/demo web interface.

The application has been validated end to end in Azure.