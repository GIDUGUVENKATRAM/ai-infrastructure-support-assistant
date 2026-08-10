# AI Infrastructure Support Assistant

An AI-powered infrastructure support assistant built as a Forward Deployed Engineer (FDE) portfolio project.

The project is being developed incrementally, starting with a simple Python application and progressively adding LLM integration, APIs, containerization, cloud deployment, retrieval-augmented generation (RAG), security, and evaluation.

## Project Goal

The goal of this project is to build an assistant that can help users troubleshoot infrastructure-related issues using an LLM and internal infrastructure documentation.

Example infrastructure questions may include:

- Why is a Linux server running out of disk space?
- How can I troubleshoot high CPU utilization?
- Why is a virtual machine unreachable?
- How do I investigate a service that is not responding?

## Current Status

**Phase 1 — Python CLI Foundation**

The application currently:

- Runs locally using Python
- Accepts an infrastructure issue from the user
- Stores the input in a Python variable
- Displays the entered issue back to the user
- Uses a Python virtual environment for dependency isolation
- Uses Git for version control

AI/LLM functionality will be added in a later phase.

## Current Architecture

```text
User
  |
  v
Terminal
  |
  v
Python Application
(app.py)
```

## Project Structure

```text
ai-infrastructure-support-assistant/
├── .gitignore
├── README.md
└── app.py
```

The local `.venv/` directory is excluded from Git.

## Running the Application

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run the application:

```bash
python app.py
```

Example:

```text
AI Infrastructure Support Assistant
-----------------------------------
Describe your infrastructure issue: Linux server is running out of disk space

You entered:
Linux server is running out of disk space
```

## Technology Stack

Current:

- Python
- Git

The technology stack will expand as new capabilities are implemented.

## Development Approach

This project follows an incremental, build-first approach. Each phase introduces a small set of concepts and results in a working, testable version of the application.