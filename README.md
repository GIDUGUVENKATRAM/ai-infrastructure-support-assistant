## Current Status

**Phase 3 — FastAPI Integration**

The application now:

- Accepts infrastructure support requests through a REST API.
- Provides a `GET /health` endpoint to verify the service is running.
- Provides a `POST /support` endpoint for infrastructure issues.
- Validates incoming request data using Pydantic.
- Sends infrastructure issues to an LLM through the OpenAI API.
- Returns AI-generated troubleshooting guidance as JSON.
- Includes basic error handling for LLM API failures.

Client
  ↓
FastAPI
  ↓
Python application
  ↓
OpenAI API
  ↓
LLM
  ↓
FastAPI
  ↓
Client