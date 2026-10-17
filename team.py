from agno.agent import Agent

from agno.models.google import Gemini
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team


load_dotenv()

eng_agent = Agent(name="English_Agent", role="You answer question in English")
chi_agent = Agent(name="Chinese_Agent", role="You answer question in Chinese")
hindi_agent = Agent(name="Hindi_Agent", role="You answer question in Hindi")

team_leader = Team(
    name="Answer & Translate Team", 
    members=[eng_agent, chi_agent, hindi_agent],
    model=Gemini(id="gemini-3.8-flash"),
    markdown=True,
    show_members_responses=True,
    instructions="All members agents must respond to the answer the query in their specific language.Do not call just one agent.",
)


team_leader.print_response("What is the capital of India?")