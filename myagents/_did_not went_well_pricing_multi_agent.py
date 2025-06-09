import os
from typing import List
from dotenv import load_dotenv
from agno.agent import Agent
from agno.run.response import RunEvent, RunResponse
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


search_agent = Agent(
    model=OpenRouter(id=MODEL),
    # tools=[GoogleSearchTools(fixed_language="English", fixed_max_results=13, cache_results=True)],
    tools=[
        Crawl4aiTools(max_length=None),
        # TavilyTools(),
        DuckDuckGoTools(fixed_max_results=13, search=True, news=False),
        # FirecrawlTools(scrape=False, crawl=True),
        GoogleSearchTools(fixed_language="English", fixed_max_results=13, cache_results=True),
    ],
    tool_call_limit=2,  # Limit to maximum 2 tool calls to control LLM usage
    description="You are pricing search agent that helps users find pricing URL page for provided AI tool website.",
    instructions=[
        "Use Google Search and DuckDuckGo to find the official pricing page URL. Sometimes, the pricing information is on the home page, so check for that.",
        "First try to identify if the tool is free to use. If it is, return 'Free'.",
        "Return only the pricing page URL, no other text or information.",
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# the_url = "https://www.vidnoz.com/"
# the_url = "https://www.accessibe.com/"
# the_url = "https://www.firecrawl.dev/"
# the_url = "https://www.alchemi.ai/"
# the_url = "https://www.waves.com/illugen"
# the_url = "https://www.get-teleprompt.com/"
# the_url = "https://www.trynia.ai/"
# the_url = "https://www.tavily.com/"
# the_url = "https://www.neosvg.com/"
# the_url = "https://cline.bot/"
the_url = "https://www.emastered.com/"


response: RunResponse = search_agent.run(the_url)
print("\n\n------------------SEARCH AGENT RESPONSE------------\n\n\n\n")
print(response.content)


crawl_agent = Agent(
    model=OpenRouter(id=MODEL),
    tools=[Crawl4aiTools(max_length=None)],
    description="You are crawler agent that helps users find the most recent pricing information about AI tools and services.",
    instructions=[
        "Crawl the pricing page and respond with the latest pricing information.",
        "Sometimes, the pricing information is on the home page, so crawl the home page as well.",
        "If pricing information is not found or not clear, check if the tool is free to use.",
        "State all their pricing plans and pricing details.",
        "State if Free tier is available.",
        "State if there is a free trial available.",
        "State if the tool is free to use.",
        "In case if input is 'Free', meaning the tool is free to use, state that it is free to use. Do not crawl the pricing page.",
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

crawl_agent.print_response(response.content + "\n"  +  f"The home page URL is: {the_url}")
