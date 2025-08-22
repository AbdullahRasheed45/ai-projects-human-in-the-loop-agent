# Human-in-the-Loop AI Agent

An interactive AI agent that shares fun facts, motivational quotes, or jokes with human confirmation before each step. It’s built with [Agno](https://github.com/AutonomousAgentsLab/agno), Nebius AI Studio’s Llama‑3.3‑70B model, and the [`rich`](https://github.com/Textualize/rich) library for a polished console experience. This project demonstrates how to incorporate human-in-the-loop workflows and retry mechanisms into an autonomous agent.

## Features

- **Human approval for every tool invocation.** A pre-hook asks whether you want to continue, cancel, or retry before the agent uses a tool.
- **Retry mechanism.** If you choose “retry,” the agent will try again with fresh context, up to three times, before stopping.
- **Multiple fun tools.** The agent has three tools to deliver an interesting fact, a motivational quote, or a joke.
- **Rich console output.** Responses are formatted with rich colors and emojis to improve readability.

## Tech stack

- Python 3.8+
- [Agno](https://github.com/AutonomousAgentsLab/agno) – framework for building agentic applications.
- Nebius AI Studio – Llama‑3.3‑70B model for language understanding.
- [rich](https://github.com/Textualize/rich) – attractive console output.
- [python‑dotenv](https://github.com/theskumar/python-dotenv) – loads environment variables.
- [gradio](https://github.com/gradio-app/gradio) – provides a simple web UI (see `app.py`).

## Prerequisites

- A Nebius API key (obtain from Nebius AI Studio). Copy `.env.example` to `.env` and set your key:
  ```
  NEBIUS_API_KEY=your_nebius_api_key_here
  ```
- Python 3.8 or higher.

## Installation

1. Clone this repository.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your `NEBIUS_API_KEY` as shown above.

## Running the agent in the console

Run the main script to start the agent in your terminal:

```bash
python main.py
```

The agent will greet you and ask permission before executing each tool. Use `y` to proceed, `n` to cancel, or `retry` to try again.

## Running the agent with a web UI

A Gradio interface is available for a more visual experience. To launch it locally, run:

```bash
python app.py
```

This will start a local server and open a browser tab where you can enter questions and see responses.

## Deployment

To share the app publicly, you can deploy the Gradio interface to a platform like Hugging Face Spaces (see the `finance-agent` project for an example). Make sure to set the `NEBIUS_API_KEY` secret in your hosting environment.

## License

This project is provided for demonstration and educational purposes.
