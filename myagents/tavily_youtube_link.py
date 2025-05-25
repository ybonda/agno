from agno.agent import Agent
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.tavily import TavilyTools
from agno.models.openrouter import OpenRouter
# MODEL= "google/gemini-2.0-flash-001"
MODEL = "openai/gpt-4.1-nano"

agent = Agent(
    model=OpenRouter(id=MODEL),
    description="You are AI expert.",
    instructions=[
        "Given an AI tool by the user, find the latest YouTube video about it and provide a link.",
    ],
    tools=[GoogleSearchTools(),TavilyTools()], 
    show_tool_calls=True)
agent.print_response("Find video with explanation or review of this ai tool: Deevid AI", markdown=True)
