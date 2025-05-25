from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.youtube import YouTubeTools
from agno.models.openrouter import OpenRouter

MODEL_NAME = "google/gemini-2.0-flash-001"


agent = Agent(tools=[Newspaper4kTools()], debug_mode=True, show_tool_calls=True)
agent.print_response("Make summary of this page https://base44.com/", stream=True)