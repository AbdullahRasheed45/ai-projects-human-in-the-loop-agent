import os
from typing import Iterator
from dotenv import load_dotenv
from agno.agent import Agent
from agno.exceptions import RetryAgentRun, StopAgentRun
from agno.models.nebius import Nebius
from agno.tools import FunctionCall, tool
import gradio as gr

# Load environment variables from .env
load_dotenv()

# Pre-hook for human approval
MAX_RETRIES = 3
retry_counter = {"count": 0}

def pre_hook(fc: FunctionCall):
    """Pre-hook for tool calls. In this web UI, human approval is handled in the console version."""
    return

# Tools definitions
@tool(pre_hook=pre_hook)
def get_fact(fact: str) -> Iterator[str]:
    yield fact

@tool(pre_hook=pre_hook)
def get_quote(quote: str) -> Iterator[str]:
    yield quote

@tool(pre_hook=pre_hook)
def get_joke(joke: str) -> Iterator[str]:
    yield joke

# Initialize the agent (same instructions as in main.py)
agent = Agent(
    description="An agent that shares fun stuff like facts, quotes, or jokes.",
    instructions="""
    You are a fun and informative agent. Use the appropriate tool to share either:
    - a fun fact
    - a motivational quote
    - or a joke

    When you get a response from a tool:
    1. For facts, start with "Here's an interesting fact: " followed by the tool's output
    2. For quotes, start with "Here's a motivational quote: " followed by the tool's output
    3. For jokes, start with "Here's a joke: " followed by the tool's output

    Ask the user before sharing, and retry only if they say so. Stop after 3 retries.

    If you have no tools to use, you should say "I don't have any tools to use."
    """,
    tools=[get_fact, get_quote, get_joke],
    markdown=True,
    model=Nebius(
        id="meta-llama/Llama-3.3-70B-Instruct",
        api_key=os.getenv("NEBIUS_API_KEY"),
    ),
)

# The respond function for the Gradio interface
def respond(message: str) -> str:
    """Generate a response from the agent."""
    # Reset retry counter before each run
    retry_counter["count"] = 0
    try:
        result = agent.run(message)
        # Convert the agent's response to text
        return str(result)
    except Exception as e:
        return f"Error: {e}"

# Build the Gradio interface
iface = gr.Interface(
    fn=respond,
    inputs=gr.inputs.Textbox(lines=2, placeholder="Ask for a fact, quote, or joke..."),
    outputs="markdown",
    title="Human-in-the-Loop AI Agent",
    description="Ask the agent to share a fun fact, motivational quote, or joke. The agent will use Nebius and Agno under the hood.",
)

if __name__ == "__main__":
    iface.launch()
