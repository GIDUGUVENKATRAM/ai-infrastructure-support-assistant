# Learning Notes

## Phase 1 — Python CLI Foundation

### Python Interpreter

The Python interpreter executes Python code.

When I run:

`python app.py`

the Python interpreter reads and executes the instructions inside `app.py`.

---

### CLI

CLI stands for Command-Line Interface.

In Phase 1, the user interacts with the application through the terminal rather than through a web interface.

Current interaction:

User → Terminal → Python Application

---

### Variable

A variable stores a value that can be used later in a program.

Example:

`issue = input("Describe your infrastructure issue: ")`

The text entered by the user is stored in the variable named `issue`.

---

### Virtual Environment

A Python virtual environment provides an isolated Python environment for a project.

This project uses:

`.venv`

It allows project dependencies to be installed without mixing them with packages used by other Python projects.

Activate it on macOS with:

`source .venv/bin/activate`

---

### Environment Variable

An environment variable is a value supplied to an application by its environment rather than hardcoded directly into the source code.

Environment variables are commonly used for configuration such as:

- API keys
- Environment names
- Service URLs
- Application settings

A virtual environment and an environment variable are different concepts.

---

### Dependency

A dependency is an external package or library that an application needs.

Phase 1 currently has no external Python dependencies.

Later phases will introduce dependencies as they are needed.

---

### PATH

PATH is a list of directories that the shell searches when I enter a command.

For example:

`which python`

shows which Python executable will run.

After activating `.venv`, `python` points to the Python executable inside the project's virtual environment.

---

### Git Repository

A Git repository is a project directory whose changes are tracked by Git.

I created the repository with:

`git init`

Git stores its internal repository information inside the hidden `.git/` directory.

---

### .gitignore

`.gitignore` tells Git which files or directories should not be tracked.

The project currently ignores:

`.venv/`

The virtual environment should be recreated rather than committed to the repository.

---

### Staging Area

The Git staging area contains changes selected for the next commit.

`git add .`

stages project changes that are not excluded by `.gitignore`.

---

### Commits

A Git commit is a saved checkpoint in the repository's history.

The first project commit records the initial working Python application.

I can view commit history with:

`git log --oneline`


---

# Phase 2 — LLM API Integration

### Large Language Model (LLM)

LLM stands for Large Language Model.

In this project, the LLM is the component that interprets a user's infrastructure issue and generates troubleshooting guidance.

The LLM is not running locally on my Mac. The application accesses it through a remote API.

---

### API

API stands for Application Programming Interface.

In this project, the Python application uses the OpenAI API to send infrastructure questions to an LLM and receive generated responses.

The application currently consumes an external API.

It does not yet expose its own API.

---

### API Client

An API client is code or an object used to communicate with an API.

In this project:

`client = OpenAI()`

creates an OpenAI API client.

The client is then used to send requests.

---

### SDK

SDK stands for Software Development Kit.

The OpenAI Python SDK provides Python classes and functions that simplify communication with the OpenAI API.

It was installed with:

`pip install openai`

---

### API Request

A request is information sent by the application to an API.

Example:

- Model to use
- User's infrastructure issue
- Authentication information

The request is sent using:

`client.responses.create(...)`

---

### API Response

A response is information returned by the API after processing a request.

In this project, the generated text is accessed using:

`response.output_text`

---

### API Key

An API key is a credential used by an application to authenticate to an API.

This project uses the environment variable:

`OPENAI_API_KEY`

The key is not hardcoded inside `app.py`.

---

### External Dependency

An external dependency is a package or service that the application depends on but does not implement itself.

Phase 2 introduces two important external dependencies:

- OpenAI Python SDK
- OpenAI API

The SDK runs locally inside the Python virtual environment.

The API is a remote service accessed over the network.

---

### requirements.txt

`requirements.txt` records the Python packages required by the application.

It can be used to recreate the project's dependencies on another machine with:

`pip install -r requirements.txt`

This is preferable to committing the local `.venv` directory.

---

### Error Handling

Error handling allows the application to respond intentionally when an operation fails.

The LLM API request is currently wrapped in:

`try`

and:

`except`

The `try` block contains code that may fail.

The `except` block handles the failure and displays an error message instead of allowing an unhandled traceback.

---

### Syntax and Indentation

Python uses indentation to define blocks of code.

For example, code inside a `try` block must be indented.

The `except` statement must align with the corresponding `try`.

Incorrect indentation can cause a `SyntaxError`.