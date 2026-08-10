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