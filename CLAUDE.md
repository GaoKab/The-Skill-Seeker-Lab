# CLAUDE.md — The Skill Seeker Lab

## Project Overview

The Skill Seeker Lab is a Streamlit web application that uses OpenAI's GPT-4 API to recommend skills for users to learn. It collects user goals, interests, challenges, and budget, then returns AI-powered skill recommendations alongside real-time course suggestions fetched from the Udemy API.

## Repository Structure

```
.
├── .devcontainer/
│   └── devcontainer.json   # Dev Container config (Python 3.11, Streamlit auto-start)
├── skill_seeker_ai.py      # Main (and only) application file
├── requirements.txt        # Python dependencies
└── CLAUDE.md               # This file
```

This is a single-file application. All logic — UI, API calls, and AI integration — lives in `skill_seeker_ai.py`.

## Tech Stack

- **Python 3.11** (specified via Dev Container)
- **Streamlit** — UI framework, runs on port 8501
- **OpenAI SDK** (`openai`) — GPT-4 chat completions for skill recommendations
- **Requests** — HTTP calls to the Udemy course API

## Dependencies

Defined in `requirements.txt`:
```
openai
streamlit
requests
```

Install with:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run skill_seeker_ai.py
```

The Dev Container is pre-configured to run this automatically on port 8501 with CORS and XSRF protection disabled for local development.

## Configuration & Secrets

- The OpenAI API key is loaded via `st.secrets["OPENAI_API_KEY"]`. When running locally, create a `.streamlit/secrets.toml` file:
  ```toml
  OPENAI_API_KEY = "sk-..."
  ```
- **Never commit API keys or secrets.** The file `.streamlit/secrets.toml` should remain in `.gitignore`.

## Known Code Issues

The current `skill_seeker_ai.py` has structural issues that should be understood before making changes:

1. **Duplicate imports and function definitions**: `openai` is imported twice (lines 2 and 20), `streamlit` is imported twice (lines 1 and 22), and `get_ai_recommendation` is defined twice (lines 18 and 26). The second definitions (lines 20–35) are the active ones due to Python's top-to-bottom execution; the first `get_ai_recommendation` (line 18) is effectively dead code.
2. **Unused initial API key assignment**: Line 6 (`openai.api_key = "your-api-key"`) is overwritten by line 24 (`openai.api_key = st.secrets["OPENAI_API_KEY"]`). The line-6 assignment is dead code.
3. **Udemy API**: The `get_courses()` function calls the Udemy API without authentication headers, which may result in failures. The Udemy API typically requires client-id/secret auth.

## Development Guidelines

### Making Changes
- This is a single-file app. All changes go in `skill_seeker_ai.py` unless new modules are being introduced.
- When refactoring, clean up the duplicate imports and function definitions noted above.
- Preserve the Streamlit UI structure (title, input fields, button, output sections).

### Testing
- There are no automated tests. Verify changes by running the Streamlit app locally.
- Test the full flow: enter goals/interests/challenges, click the recommendation button, and verify the AI response renders correctly.

### Code Style
- No linter or formatter is configured. Follow standard Python conventions (PEP 8).
- Keep the code straightforward — this is a prototype/learning project.

### Git Workflow
- The default branch is `main`.
- Commit messages in this repo have been short and descriptive (e.g., "Update skill_seeker_ai.py").
- No CI/CD pipeline is configured.

### Dev Container
- Configured in `.devcontainer/devcontainer.json`.
- Uses `mcr.microsoft.com/devcontainers/python:1-3.11-bullseye`.
- Auto-installs dependencies from `requirements.txt` and starts the Streamlit server on attach.
- VS Code extensions: `ms-python.python`, `ms-python.vscode-pylance`.
