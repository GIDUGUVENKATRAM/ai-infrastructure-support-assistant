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