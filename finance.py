from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.groq import Groq

from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

load_dotenv()

def build_agent():
    return Agent(
        model=Gemini(id="gemini-3.8-flash"),
        tools=[YFinanceTools()],
        markdown=True,
     
        add_datetime_to_context=True,
        description="This agent is designed to provide financial information and insights using the YFinance API.",
        instructions="You are a financial assistant. Use the YFinance API to provide accurate and up-to-date financial information.",
        debug_mode=True
    )

agent = build_agent()

agent.print_response("Share the MSFT stock price and its recent performance.")