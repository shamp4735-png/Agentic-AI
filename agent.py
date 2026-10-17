from agno.agent import Agent

from agno.models.google import Gemini
from agno.models.groq import Groq

from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

def build_agent():
    return Agent(
        model=Gemini(id="qwen/qwen3_32b"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful assistant.",
        add_datetime_to_context=True,
    )

agent = build_agent()

agent.print_response("it is safe to travel to UAE today?")