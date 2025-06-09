import os
from typing import List
from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.spider import SpiderTools
from agno.tools.website import WebsiteTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from agno.models.openrouter import OpenRouter
from agno.tools.crawl4ai import Crawl4aiTools
from agno.tools.firecrawl import FirecrawlTools

# Load environment variables from .env file
load_dotenv()

# MODEL = "google/gemini-2.5-flash-preview-05-20"
MODEL = "openai/gpt-4.1-nano"


agent = Agent(
    model=OpenRouter(id=MODEL),
    tools=[
        Crawl4aiTools(max_length=14000),
        DuckDuckGoTools(fixed_max_results=3, search=True, news=False),
        GoogleSearchTools(fixed_language="English", fixed_max_results=3, cache_results=True),
    ],
    tool_call_limit=2,  # Limit to maximum 2 tool calls to control LLM usage
    description="You are AI exprert that helps users find the most recent pricing information about AI tools and services.",
    instructions=[
        "Use google_search_tools or duckduckgo to find the official pricing page URL. Pass that URL to crawl4ai_tools to crawl the pricing page and respond with the latest pricing information.",
        "If pricing information is not found or not clear, check if the tool is free to use.",
        "State all their pricing plans and pricing details.",
        "State if Free tier is available.",
        "State if there is a free trial available.",
        "State if the tool is free to use.",
    ],
    show_tool_calls=True,
    markdown=True,
    # use_json_mode=True,
    debug_mode=True,
)

# agent.print_response("Home page URL: https://accessibe.com/, name: Accessibe")
# agent.print_response("Home page URL: https://aigregator.com/, name: Aigregator")
# agent.print_response("Home page URL: https://www.vidnoz.com/, name: Vidnoz")
# agent.print_response("Home page URL: https://www.firecrawl.dev/, name: Firecrawl")
# agent.print_response("Home page URL: https://groas.ai/, name: Groas")
# agent.print_response("Home page URL: https://base44.com/, name: Base44")
# agent.print_response("Home page URL: https://www.alchemi.ai/, name: Alchemi")
# agent.print_response("Home page URL: https://v0.dev/, name: V0")
# agent.print_response("Home page URL: https://emastered.com/, name: Emastered")
# agent.print_response("Home page URL: https://neosvg.com/, name: Neosvg")
# agent.print_response("AI tool website: https://www.tavily.com/")
agent.print_response("Home page URL: https://cline.bot/, name: Cline")
# agent.print_response("AI tool website: https://www.trynia.ai/")
# agent.print_response("https://www.waves.com/illugen")
# agent.print_response("AI tool website: https://www.get-teleprompt.com/")
