## Current Status

**Phase 2 — LLM API Integration**

The application now:

- Runs locally using Python
- Accepts an infrastructure issue from the user
- Sends the issue to an LLM through the OpenAI API
- Displays an AI-generated troubleshooting response
- Uses the OpenAI Python SDK
- Uses an environment variable for API credentials
- Uses basic error handling for API failures
- Uses a Python virtual environment for dependency isolation
- Uses `requirements.txt` to record Python dependencies
- Uses Git for version control

## Current Architecture

```text
User
  |
  v
Terminal / CLI
  |
  v
Python Application
(app.py)
  |
  v
OpenAI Python SDK
  |
  v
OpenAI API
  |
  v
LLM
  |
  v
Generated Response
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

## Running the Application

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Set the API key in the current shell session:

```bash
export OPENAI_API_KEY=your_api_key
```

Do not hardcode the API key inside the source code.

Run the application:

```bash
python app.py
```

Example:

```text
AI Infrastructure Support Assistant
-----------------------------------
Describe your infrastructure issue: Linux server is running out of disk space

AI Response:
Start by checking filesystem utilization using `df -h`...
```

## Technology Stack

Current:

- Python
- OpenAI API
- OpenAI Python SDK
- Git

Python dependencies are recorded in:

```text
requirements.txt
```