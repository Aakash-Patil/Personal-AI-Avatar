# Personal AI Avatar

A personal AI avatar for **Akash Shekhar Patil** — an interactive chatbot that acts as a digital twin on a portfolio or personal website. Visitors can ask questions about career, background, skills, and experience, and the assistant answers using context from a resume and a short personal summary.

## Features

- **Resume-aware chat** — Loads content from `resume.pdf` and `summary.txt` to ground every response in real profile data
- **Digital twin persona** — Stays in character as Akash, with a professional tone suited for recruiters, clients, and collaborators
- **Topic guardrails** — Focuses on career-related questions and declines unrelated topics
- **Streaming responses** — Uses OpenAI streaming for a responsive chat experience
- **Simple web UI** — Gradio `ChatInterface` launches in the browser with minimal setup

## Tech Stack

- **Python 3.12+**
- **[uv](https://docs.astral.sh/uv/)** — dependency and environment management
- **[OpenAI API](https://platform.openai.com/)** — chat completions (`gpt-5.4-mini`)
- **[Gradio](https://www.gradio.app/)** — chat interface
- **[pypdf](https://pypi.org/project/pypdf/)** — PDF text extraction

## Prerequisites

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed
- An OpenAI API key

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Aakash-Patil/Personal-AI-Avatar.git
cd Personal-AI-Avatar
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Add your profile data

Place or update these files in the project root:

| File | Purpose |
|------|---------|
| `resume.pdf` | Full resume text extracted at runtime for detailed Q&A |
| `summary.txt` | Short bio and highlights used in the system prompt |

### 5. Run the chatbot

```bash
uv run python ai.py
```

Gradio opens a chat interface in your default browser. Ask questions such as:

- "What is your experience with Python and AI?"
- "Tell me about your background."
- "What technologies do you work with?"

## How It Works

1. On each message, `get_system_prompt()` builds a system prompt from `summary.txt` and the text extracted from `resume.pdf`.
2. The prompt instructs the model to act as a digital twin, stay professional, and avoid inventing facts.
3. Conversation history is passed to the OpenAI Chat Completions API with streaming enabled.
4. Responses are streamed back to the Gradio UI in real time.

## Project Structure

```
Personal-AI-Avatar/
├── ai.py           # Main application: PDF extraction, prompt, chat, Gradio UI
├── resume.pdf      # Resume used as RAG-style context (not committed if sensitive)
├── summary.txt     # Short personal summary for the system prompt
├── pyproject.toml  # Project metadata and dependencies
├── uv.lock         # Locked dependency versions
└── .env            # API keys (not committed; create locally)
```

## Customization

To adapt this avatar for another person or site:

1. Replace `resume.pdf` and `summary.txt` with your own content.
2. Update the name and fallback message in the system prompt inside `get_system_prompt()` in `ai.py`.
3. Optionally change the OpenAI model in the `chat()` function.

## Notes

- The assistant is instructed to say it does not know when information is missing from the provided context.
- Questions unrelated to career and background are redirected with a polite boundary message.
- Keep `.env` out of version control; it is listed in `.gitignore`.

## License

This project is for personal portfolio use. Add a license here if you plan to open-source or share it more broadly.
