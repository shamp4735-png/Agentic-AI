from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

from dotenv import load_dotenv


load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        model=Gemini(id="gemini-3.8-flash"),
        markdown=True,
        add_history_to_context=True,
        
        
    )

agent = build_agent()

user_id = "rahul@gmail.com"
agent.print_response("What is the capital of India?", user_id=user_id)
agent.print_response("What is the best time to visit it?", user_id=user_id)

memories = agent.get_user_memories(user_id=user_id)

print("MEMORIES: ")
pprint(memories)
