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