# Interview Notes

## Phase 1 — Python CLI Foundation

These questions cover concepts implemented or encountered during Phase 1 of the AI Infrastructure Support Assistant.

---

### 1. What have you built so far?

I started the AI Infrastructure Support Assistant as a simple Python command-line application.

The application accepts an infrastructure issue from the user, stores the input, and displays it back to the user.

I intentionally started with a minimal working application before introducing LLMs, APIs, containers, and other components.

---

### 2. What is the current architecture?

The current architecture is:

User → Terminal → Python Application

The terminal is currently the user interface, and `app.py` contains the application logic.

The architecture will evolve incrementally as additional capabilities are introduced.

---

### 3. Why did you start with a CLI application?

A CLI provides the simplest way to validate the application's basic input and execution flow without introducing unnecessary components.

It gives me a working foundation that I can progressively extend.

---

### 4. What is a Python virtual environment, and why are you using one?

A virtual environment provides an isolated Python environment for a project.

I use `.venv` so that dependencies required by this application can be installed independently from other Python projects on my machine.

---

### 5. What is the difference between a virtual environment and an environment variable?

A virtual environment isolates the Python interpreter and project dependencies.

An environment variable provides configuration or values to an application, such as API keys, service URLs, or environment-specific settings.

---

### 6. What is a dependency?

A dependency is an external package or library that an application requires.

The Phase 1 application currently uses only Python functionality and does not require external Python packages.

Future phases will introduce dependencies as needed.

---

### 7. Why is `.venv` in `.gitignore`?

The `.venv` directory contains the local Python virtual environment and installed packages.

It should not be committed because other developers or deployment environments should recreate the required environment from the project's dependency definitions instead of using my local environment.

---

### 8. What is the difference between Git and GitHub?

Git is the version-control system used to track changes and create commits.

GitHub is a platform that can host Git repositories remotely and allow the project to be shared and reviewed.

---

### 9. What is Git staging?

The staging area contains changes selected for inclusion in the next Git commit.

For example:

`git add .`

stages the current project changes before they are committed.

---

### 10. What is a Git commit?

A commit is a saved checkpoint in the project's version history.

I use meaningful commits to record milestones as the application evolves.

---

## Phase 1 Architecture

User  
↓  
Terminal / CLI  
↓  
Python Application (`app.py`)  
↓  
Terminal Output

---

## Questions I Should Be Able to Answer

After Phase 1, I should be comfortable explaining:

- What the application currently does.
- How the current architecture works.
- What a CLI application is.
- What a Python interpreter does.
- What a Python virtual environment is.
- Why dependency isolation matters.
- The difference between a virtual environment and an environment variable.
- What PATH does at a basic level.
- Why `.gitignore` is used.
- What Git staging means.
- What a Git commit represents.
- The difference between Git and GitHub.


---

# Phase 2 — LLM API Integration

### 1. What did you add in Phase 2?

I integrated an LLM into the AI Infrastructure Support Assistant.

The application now accepts an infrastructure issue from the user, sends it to an LLM through the OpenAI API, receives a generated troubleshooting response, and displays it in the terminal.

---

### 2. Why does your application use an LLM?

The LLM provides the natural-language processing and generation capability of the application.

Instead of creating hardcoded rules for every possible infrastructure problem, users can describe issues in natural language and the LLM can generate relevant troubleshooting guidance.

---

### 3. What is the current architecture?

The current architecture is:

User → CLI → Python Application → OpenAI SDK → OpenAI API → LLM

The generated response then returns through the application and is displayed to the user.

---

### 4. What is the difference between an LLM, API, and SDK?

An LLM is the model that processes natural language and generates a response.

An API is the interface my application uses to communicate with the remote AI service.

An SDK is a software library that makes interacting with that API easier from a programming language such as Python.

---

### 5. What does `client = OpenAI()` do?

`OpenAI()` creates an API client object using the OpenAI Python SDK.

The client is used by my Python application to communicate with the OpenAI API.

Creating the client does not create an API or send the infrastructure question.

The actual request is sent when the application calls `client.responses.create(...)`.

---

### 6. What happens when a user enters an infrastructure issue?

The user's text is stored in the Python variable `issue`.

That value is passed to the OpenAI client:

`client.responses.create(...)`

The SDK sends the request to the OpenAI API.

The LLM processes the input and generates a response.

The application retrieves the generated text from `response.output_text` and displays it in the terminal.

---

### 7. How do you protect the API key?

The API key is not hardcoded into the Python source code.

It is provided through the `OPENAI_API_KEY` environment variable.

The OpenAI SDK reads the credential from the environment.

This reduces the risk of accidentally committing the credential to Git.

---

### 8. What did you learn about environment variables?

Environment variables belong to a process environment.

I discovered this when the API key was available in iTerm2 but not in the VS Code integrated terminal.

Exporting a variable in one shell session does not automatically make it available to another shell session.

---

### 9. What problems did you encounter while integrating the LLM?

I encountered several different problems at different layers of the integration.

First, the SDK reported missing credentials because the API key was not available in the shell running Python.

After correcting that, the HTTP request failed because the API key contained an unintended non-ASCII smart quote.

After correcting the credential formatting, the API returned an HTTP 429 error because the API account had no available credits.

I diagnosed each problem separately rather than changing the application code without identifying the cause.

---

### 10. Why do you use `requirements.txt`?

`requirements.txt` records the Python dependencies required by the project.

Someone setting up the application on another machine can install those dependencies using:

`pip install -r requirements.txt`

This is preferable to committing my local `.venv` directory.

---

### 11. Why did you create `test_llm.py` before modifying `app.py`?

I wanted to test the LLM integration independently from the main application.

The small test allowed me to verify the SDK, credentials, API connectivity, billing, and model response before introducing those changes into the working application.

This made troubleshooting easier because fewer components were involved.

---

### 12. How do you currently handle API failures?

The API request is wrapped in a Python `try` / `except` block.

If the request succeeds, the application displays