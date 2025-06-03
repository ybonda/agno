import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.website import WebsiteTools
from agno.tools.crawl4ai import Crawl4aiTools
from agno.models.openrouter import OpenRouter
from agno.tools.duckduckgo import DuckDuckGoTools

# Load environment variables from .env file
load_dotenv()

# MODEL = "google/gemini-2.0-flash-001"
# MODEL = "openai/gpt-4.1-nano"
MODEL = "google/gemini-2.5-flash-preview-05-20"
# MODEL = "google/gemini-2.0-flash-001"

# Pricing-Only Extraction Agent with Sequential Tool Strategy
pricing_agent = Agent(
    model=OpenRouter(id=MODEL),
    tools=[
        GoogleSearchTools(fixed_language="English", fixed_max_results=7, cache_results=True),
        # DuckDuckGoTools(fixed_max_results=7, search=True),
    ],
    tool_call_limit=3,  # Increased for comprehensive pricing extraction
    description="You are a pricing extraction specialist that focuses solely on finding and extracting pricing information from AI tool websites.",
    instructions=[
        "Extract pricing information of AI tool from the website. ",
        "It's important to state most recent pricing information.",
        "It's important to state the price of the different plans.",
        ""
    ],
    show_tool_calls=True,
    use_json_mode=True,
    debug_mode=True,
)

# Test cases - uncomment to test different AI tools
# pricing_agent.print_response("AI tool website: https://base44.com/")
# pricing_agent.print_response("AI tool website: https://v0.dev/")
# pricing_agent.print_response("AI tool website: https://emastered.com/")
pricing_agent.print_response("AI tool website: https://neosvg.com/")
# pricing_agent.print_response("AI tool website: https://www.tavily.com/")
# pricing_agent.print_response("AI tool website: https://cline.bot/")
# pricing_agent.print_response("AI tool website: https://www.trynia.ai/")
# pricing_agent.print_response("AI tool website: https://www.waves.com/illugen")
# pricing_agent.print_response("AI tool website: https://www.get-teleprompt.com/") 