## PydanticAI Local Blog Agent

A practical local AI agent built with [PydanticAI](https://ai.pydantic.dev/) and Ollama. It uses `gemma4:e4b` to create blog ideas with real tools for titles, outlines, and opening hooks.

## Requirements

- Python 3.14
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/)
- The `gemma4:e4b` model

Pull the model before running the agent:

```bash
ollama pull gemma4:e4b
```

## Setup

Install the project dependencies:

```bash
uv sync
```

The agent expects Ollama to be available at `http://localhost:11434`. You can override the connection with a `.env` file:

```env
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_API_KEY=ollama
```

## Run

Start Ollama, then run the example:

```bash
uv run python main.py
```

The project also includes `main.ipynb`, which demonstrates the same workflow interactively, including passing the previous run's message history into a follow-up request.

## Project Structure

- `main.py` - Tool-using blog strategist agent.
- `main.ipynb` - Interactive tutorial notebook.
- `pyproject.toml` - Project metadata and dependencies.

## License

This project is intended for learning and experimentation.
