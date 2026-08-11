# Architecture

## Phase 1 — Python CLI Foundation

The first version of the AI Infrastructure Support Assistant is a local command-line application written in Python.

## Architecture Diagram

```text
User
  |
  | Infrastructure issue
  v
Terminal
  |
  v
Python Application
(app.py)
  |
  | Displays entered issue
  v
Terminal
  |
  v
User
```

## Request Flow

1. The user starts the application using `python app.py`.
2. Python executes the code inside `app.py`.
3. The application prompts the user to describe an infrastructure issue.
4. `input()` receives the user's text.
5. The text is stored in the `issue` variable.
6. `print()` displays the value back to the user.

## Current Components

### Python Application

`app.py` contains the current application logic.

Its responsibilities are:

- Display the application name.
- Accept user input.
- Store the infrastructure issue.
- Display the entered issue.

### Command-Line Interface

The terminal currently acts as the user interface.

There is no web interface or API in Phase 1.

### Python Virtual Environment

The `.venv` virtual environment isolates the project's Python environment and future dependencies from other Python projects on the development machine.

The `.venv` directory is local and is not tracked by Git.

## Current Limitations

Phase 1 does not yet:

- Generate AI responses.
- Call an LLM.
- Expose an API.
- Provide a web interface.
- Store or retrieve infrastructure documentation.
- Use RAG.
- Run inside a Docker container.
- Run in the cloud.

These capabilities will be introduced incrementally in later phases.


---

# Phase 2 — LLM API Integration

Phase 2 adds an external Large Language Model (LLM) to the application.

The Python application now sends the user's infrastructure issue to the OpenAI API and displays the generated troubleshooting response.

## Architecture Diagram

```text
User
  |
  | Infrastructure issue
  v
Terminal / CLI
  |
  v
Python Application
(app.py)
  |
  | API request
  v
OpenAI Python SDK
  |
  v
OpenAI API
  |
  v
LLM
  |
  | Generated response
  v
OpenAI API
  |
  v
Python Application
  |
  v
Terminal
  |
  v
User
```

## Request Flow

1. The user starts the application with `python app.py`.
2. The application asks the user to describe an infrastructure issue.
3. Python stores the user's input in the `issue` variable.
4. The OpenAI Python SDK creates an API request.
5. The value stored in `issue` is sent to the OpenAI API.
6. The LLM processes the infrastructure question.
7. The API returns the generated response.
8. The SDK provides the response to the Python application.
9. The application extracts `response.output_text`.
10. The troubleshooting response is displayed in the terminal.

## New Components

### OpenAI Python SDK

The OpenAI Python SDK is an external Python dependency that simplifies communication between the Python application and the OpenAI API.

The application creates a client using:

`client = OpenAI()`

The client is used to send requests to the API.

### OpenAI API

The OpenAI API is the remote interface used by the application to access an LLM.

The application is currently an API consumer. It does not yet expose its own API.

### Large Language Model

The LLM processes the user's natural-language infrastructure issue and generates troubleshooting guidance.

The model provides general knowledge and does not yet have access to organization-specific infrastructure documentation.

### API Credential

The application authenticates to the OpenAI API using the `OPENAI_API_KEY` environment variable.

The API key is not hardcoded into the application source code.

## Error Handling

The LLM API request is wrapped in basic Python `try` / `except` error handling.

This allows the application to display a readable error when an API request fails instead of terminating with an unhandled traceback.

## Phase 1 vs Phase 2

Phase 1:

```text
User → CLI → Python → CLI → User
```

Phase 2:

```text
User → CLI → Python → OpenAI API → LLM → Python → CLI → User
```

The main architectural change is that the application now depends on an external AI service to generate troubleshooting responses.

## Current Limitations

The application does not yet:

- Expose its own REST API.
- Provide a web interface.
- Use internal infrastructure documents.
- Use embeddings or a vector database.
- Implement RAG.
- Run inside Docker.
- Run in the cloud.
- Implement production-grade security or observability.

These capabilities will be introduced incrementally in later phases.

