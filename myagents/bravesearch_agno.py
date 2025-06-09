from agno.agent import Agent
from agno.tools.bravesearch import BraveSearchTools
from agno.models.openrouter import OpenRouter

MODEL = "openai/gpt-4o-mini"

agent = Agent(
    model=OpenRouter(id=MODEL),
    tools=[BraveSearchTools()],
    description="You are a pricing expert in ai tools and services.",
    instructions=[
        "Given the website of the ai tool or service, respond with the pricing details."
    ],
    show_tool_calls=True,
)
agent.print_response("https://accessibe.com/", markdown=True)
