# Troubleshooting Notes

This document records meaningful issues encountered while building the AI Infrastructure Support Assistant.

For each issue, I will document the symptom, investigation, root cause, resolution, and lesson learned.

## Phase 1 — Python CLI Foundation

No significant issues were encountered during Phase 1.

The Python environment, virtual environment, application execution, VS Code setup, and Git initialization worked as expected.

## Troubleshooting Template

Future issues will be documented using the following structure:

### Problem

What happened?

### Error / Symptom

What error or unexpected behavior was observed?

### Investigation

What commands, logs, or tests were used to investigate?

### Root Cause

What caused the problem?

### Resolution

How was the problem fixed?

### Verification

How was the fix tested?

### Lesson Learned

What should I remember from this issue?

---

# Phase 2 — LLM API Integration

## Issue 1 — OpenAI SDK Could Not Find API Credentials

### Problem

The first LLM API test failed when creating the OpenAI client.

### Error / Symptom

```text
openai.OpenAIError: Missing credentials.
```

### Investigation

I checked whether the `OPENAI_API_KEY` environment variable was available in the shell.

I discovered that environment variables exported in one terminal session were not automatically available in another terminal session.

For example, iTerm2 and the VS Code integrated terminal had separate shell environments.

### Root Cause

`OPENAI_API_KEY` was not available in the shell session running the Python application.

### Resolution

I exported `OPENAI_API_KEY` in the same terminal session used to run the application.

### Verification

I verified that Python could see the variable without displaying the secret.

### Lesson Learned

Environment variables are associated with a process/shell environment.

Setting a variable in one terminal session does not automatically make it available in every other terminal session.

---

## Issue 2 — API Key Contained a Non-ASCII Character

### Problem

After the API key became visible to Python, the API request still failed while the HTTP request headers were being created.

### Error / Symptom

```text
UnicodeEncodeError: 'ascii' codec can't encode character '\u2018'
```

### Investigation

I checked the API key without displaying its actual value.

The diagnostic showed:

```text
ASCII only: False
Starts with sk-: False
```

The error identified `\u2018`, which represents a curly/smart single quote.

### Root Cause

The API key environment variable contained an unintended smart quote character.

### Resolution

I removed the incorrect environment variable and exported the API key again without the unintended quote characters.

### Verification

The diagnostic then showed:

```text
Exists: True
ASCII only: True
Starts with sk-: True
```

### Lesson Learned

Secrets can fail because of formatting problems even when the credential itself is correct.

Credentials should also be diagnosed without printing the secret value.

---

## Issue 3 — API Request Rejected Because No Credits Were Available

### Problem

After fixing the API credential configuration, the request reached the OpenAI API but was rejected.

### Error / Symptom

```text
openai.RateLimitError: Error code: 429
code: credit_balance_exhausted
```

### Investigation

The previous credential and encoding errors were no longer occurring.

The API response specifically reported that no API credits remained.

### Root Cause

The API account did not have available API credits.

### Resolution

API billing was configured and credits were added.

### Verification

I ran:

```bash
python test_llm.py
```

again.

The application successfully returned an LLM-generated troubleshooting response recommending `df -h` as the first step for investigating disk-space usage.

### Lesson Learned

A successful API integration depends on more than application code.

External-service dependencies can include:

- Authentication
- Network connectivity
- Service availability
- Account configuration
- Quotas and billing

Different error messages can indicate that the request is reaching different stages of the integration.

---

## Issue 4 — Python `try` Block Syntax Error

### Problem

While adding basic error handling to `app.py`, the application failed before it could run.

### Error / Symptom

```text
SyntaxError: expected 'except' or 'finally' block
```

### Investigation

I inspected the `try` / `except` structure and indentation around the reported line.

### Root Cause

The code following the `try` block was incorrectly indented, so Python encountered code where it expected an `except` or `finally` block.

### Resolution

I corrected the indentation so that the statements belonging to `try` were indented and `except` aligned with `try`.

### Verification

The application executed successfully after correcting the syntax.

### Lesson Learned

Python uses indentation to define code blocks.

A `try` statement must be followed by an appropriately structured `except` or `finally` block.