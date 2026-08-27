# AI Infrastructure Support Assistant — Architecture

## Overview

The AI Infrastructure Support Assistant is a cloud-deployed AI application designed to assist with infrastructure troubleshooting.

The solution combines a FastAPI application, Microsoft Foundry agent, retrieval-augmented generation (RAG), tool calling, an MCP service, containerized deployment, managed identity authentication, and Azure observability.

The application evolved from a local Python CLI prototype into an end-to-end cloud-hosted AI support system.

---

## High-Level Architecture

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
                       FastAPI
                           |
                           v
                     Web Interface
                           |
                           v
                         User
```

---

## Main Components

### 1. Web Interface

The user interacts with a lightweight HTML, CSS, and JavaScript interface.

The interface:

- accepts infrastructure support questions;
- sends requests to the FastAPI backend;
- displays AI-generated troubleshooting responses;
- checks application health through the `/health` endpoint.

The frontend is served by FastAPI from `static/index.html`.

---

### 2. FastAPI Application

`api.py` is the primary application entry point.

FastAPI provides the service layer between the web interface and the AI services.

Important endpoints include:

```text
GET  /health
POST /support
POST /demo/support
```

`/health` provides application health verification.

`/support` is a protected direct-model endpoint requiring an API key.

`/demo/support` is the public demonstration endpoint connected to the Microsoft Foundry agent.

---

### 3. Microsoft Foundry Agent

The deployed application connects to the `fde-support-agent` configured in Microsoft Foundry.

The agent acts as the AI orchestration layer.

Instead of every request being sent directly to a base model, the agent can determine whether additional capabilities are required, including:

- internal knowledge retrieval;
- RAG;
- configured tools;
- infrastructure service calls.

This allows the application to provide responses grounded in infrastructure-specific information rather than relying only on general model knowledge.

---

## Retrieval-Augmented Generation (RAG)

RAG provides the agent with access to infrastructure-specific knowledge.

Conceptually:

```text
User Question
     |
     v
Foundry Agent
     |
     v
Knowledge Retrieval
     |
     v
Relevant Infrastructure Context
     |
     v
LLM
     |
     v
Grounded Response
```

A validated example from the project is retrieving organization-specific VDI troubleshooting thresholds and escalation codes such as:

```text
VDI-PERF-17
```

This information comes from the configured knowledge source rather than relying solely on the model's general knowledge.

---

## Agent Tools

The Foundry agent can use configured tools when a request requires information or actions outside the model itself.

The project includes infrastructure-oriented tool integration through APIs.

Conceptually:

```text
User Request
     |
     v
Foundry Agent
     |
     +---- No tool required ----> Generate response
     |
     +---- Tool required -------> Call tool/API
                                      |
                                      v
                                  Tool result
                                      |
                                      v
                                     Agent
                                      |
                                      v
                                  Final response
```

This demonstrates agentic orchestration rather than simple prompt-response LLM usage.

---

## MCP Integration

The project includes an MCP server implemented in:

```text
mcp_server.py
```

with a separate container definition:

```text
Dockerfile.mcp
```

The MCP layer demonstrates how infrastructure capabilities can be exposed through a standardized tool interface for AI applications.

This separates infrastructure-facing functionality from the primary FastAPI application and provides a foundation for extending the assistant with additional operational tools.

---

## Azure Deployment Architecture

The application is containerized using Docker and deployed to Azure Container Apps.

```text
Source Code
    |
    v
Docker Build
    |
    v
Container Image
    |
    v
Azure Container Registry
    |
    v
Azure Container Apps
    |
    v
FastAPI Application
```

The deployed application exposes a public HTTPS endpoint through Azure Container Apps.

---

## Authentication and Managed Identity

The application uses a user-assigned managed identity for Azure-to-Azure authentication.

```text
Azure Container App
        |
        v
User-Assigned Managed Identity
        |
        v
Microsoft Foundry
```

This avoids embedding Azure credentials directly in application source code.

During deployment, an authentication issue was identified where local development succeeded because `DefaultAzureCredential` could use the developer's Azure identity, while the Azure Container App needed explicit selection of the user-assigned managed identity.

The application therefore explicitly selects the appropriate managed identity when creating the Azure credential.

This allows the deployed container to authenticate to Foundry without storing developer credentials inside the container.

---

## Security and Application Hardening

The application includes several basic hardening controls.

### Environment-based configuration

Secrets and configuration are provided through environment variables rather than hardcoded into source code.

The `.env` file is excluded from Git.

### API-key protection

The `/support` endpoint requires a private API key through the request header.

### Request validation

Pydantic validates incoming support requests.

Input length limits help prevent empty or excessively large prompts.

### Rate limiting

The public demo endpoint is rate limited to reduce abuse and unnecessary AI consumption.

### Output limits

AI output token limits help control response size and service usage.

### Sanitized client errors

Detailed exceptions are written to backend logs while clients receive simplified error messages.

---

## Observability

The application integrates Azure monitoring and OpenTelemetry.

```text
FastAPI Application
       |
       v
OpenTelemetry
       |
       v
Azure Monitor / Application Insights
```

Application logging provides visibility into:

- application startup;
- incoming support requests;
- successful AI responses;
- Foundry failures;
- authentication problems;
- application exceptions.

Container App log streaming was also used during deployment troubleshooting.

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
│   └── test_foundry_mcp.py
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

## End-to-End Request Flow

A typical deployed request follows this path:

```text
1. User enters an infrastructure issue in the browser.

2. JavaScript sends:
   POST /demo/support

3. FastAPI validates the request.

4. FastAPI authenticates to Microsoft Foundry using
   the Container App's user-assigned managed identity.

5. The request is sent to the Foundry agent.

6. The agent determines whether it needs:
   - model reasoning,
   - RAG / knowledge retrieval,
   - or an external tool.

7. Relevant knowledge or tool results are provided
   to the agent when required.

8. The agent generates the final troubleshooting response.

9. FastAPI returns the response as JSON.

10. The web interface displays the response to the user.

11. Application activity and failures are available
    through Azure observability and container logs.
```

---

## Architectural Evolution

The project was intentionally developed incrementally:

```text
Python CLI
    ↓
LLM API Integration
    ↓
FastAPI REST API
    ↓
Docker
    ↓
Azure Deployment
    ↓
Observability
    ↓
RAG / Knowledge
    ↓
MCP
    ↓
Foundry Agent + Tools
    ↓
Managed Identity
    ↓
Web Demo + Application Hardening
```

The earlier architecture stages are preserved in `docs/architecture-history.md`.

---

## Final Architecture Goal

The project demonstrates how an infrastructure support use case can evolve beyond a basic chatbot into a cloud-hosted AI application combining:

**LLM + RAG + Agents + Tools + MCP + APIs + Containers + Cloud Identity + Observability.**