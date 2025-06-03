import os
from typing import List
from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.spider import SpiderTools
from agno.tools.website import WebsiteTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.openrouter import OpenRouter

# Load environment variables from .env file
load_dotenv()

try:
    from pymongo import MongoClient
    from pymongo.errors import PyMongoError
except ImportError:
    raise ImportError("`pymongo` not installed. Please install it with `pip install pymongo`")

# MODEL= "google/gemini-2.0-flash-001"
# MODEL = "openai/gpt-4.1-nano"
MODEL = "google/gemini-2.5-flash-preview-05-20"


def get_mongodb_connection():
    """Get MongoDB connection using environment variables."""
    mongodb_url = os.getenv("MONGODB_URL")
    db_name = os.getenv("DB_NAME", "aigregator")

    if not mongodb_url:
        raise ValueError("MONGODB_URL environment variable is not set")

    try:
        client = MongoClient(mongodb_url)
        # Test the connection
        client.admin.command("ping")
        return client[db_name]
    except PyMongoError as e:
        raise ConnectionError(f"Failed to connect to MongoDB: {e}")


def load_tags_from_db() -> List[str]:
    """Load tags from MongoDB tags collection."""
    try:
        db = get_mongodb_connection()
        tags_collection = db["tags"]

        # Fetch all tags and extract the tag names
        tags_cursor = tags_collection.find({}, {"name": 1, "_id": 0})
        tags = [tag["name"] for tag in tags_cursor if "name" in tag]

        if not tags:
            raise Exception("No tags found in database")

        return tags
    except Exception as e:
        print(f"Error loading tags from database: {e}")
        raise e


def load_categories_from_db() -> List[str]:
    """Load categories from MongoDB categories collection."""
    try:
        db = get_mongodb_connection()
        categories_collection = db["categories"]

        # Fetch all categories and extract the category names
        categories_cursor = categories_collection.find({}, {"name": 1, "_id": 0})
        categories = [category["name"] for category in categories_cursor if "name" in category]

        if not categories:
            raise Exception("No categories found in database")

        return categories
    except Exception as e:
        raise e


# Load tags and categories from database
tags = load_tags_from_db()
categories = load_categories_from_db()

# Convert lists to comma-separated strings for the prompt
tags_str = ", ".join(tags)
categories_str = ", ".join(categories)

# Additional optimization options (uncomment to use):
# 
# Option 1: Use a smaller, faster model for initial searches
# MODEL = "openai/gpt-4o-mini"  # Cheaper and faster
#
# Option 2: Reduce search results to save tokens
# tools=[GoogleSearchTools(fixed_language="English", fixed_max_results=5)],
#
# Option 3: Add caching to avoid repeated searches
# from agno.tools.googlesearch import GoogleSearchTools
# tools=[GoogleSearchTools(fixed_language="English", fixed_max_results=13, cache_results=True)],
#
# Option 4: Use more specific search queries in instructions to get better results faster

agent = Agent(
    model=OpenRouter(id=MODEL),
    # tools=[GoogleSearchTools(fixed_language="English", fixed_max_results=13, cache_results=True)],
    tools=[DuckDuckGoTools(fixed_max_results=23, search=True, news=True)],
    tool_call_limit=2,  # Limit to maximum 2 tool calls to control LLM usage
    description="You are AI exprert that helps users find information about AI tools.",
    instructions=[
        "Given an AI tool website URL by a user, search the internet and respond in JSON format with",
        "IMPORTANT: You have a maximum of 2 search calls, so make them count. Use comprehensive search queries.",
        "For your first search, use the website URL directly to get basic information about the tool.",
        "If you need more information, make 1-2 additional targeted searches for specific details like pricing, features, or alternatives.",
        " - name: crawl the name of the tool from the tool webpage content.",
        " - short_description: short description of the tool (12 words max).",
        " - description: detailed description of the tool (50-200 words)",
        " - how_it_works: Based on the search results explain how the tool works.",
        " - how_to _use: Based on the search results explain how to use the tool.",
        " - use_cases: Based on the search results explain what are use cases.",
        " - features: Based on the search results explain what are the main features.",
        " - target_audience: Based on the search results explain who is the target audience.",
        " - pros: Provide 1-4 strong pros for why this tool is better than the alternatives based on actual search results.",
        " - cons: Provide 1-3 strong cons for why this tool is worse than the alternatives based on actual search results.",
        " - alternatives: Provide 1-3 alternative tools.",
        f" - tags: select 1-2 best matching tags ONLY from the provided list: {tags_str}.",
        f"- category: select the best matching single category ONLY from the provided list: {categories_str}.",
        "Avoid in the response uncertainties, hedging, and phrases like 'I think', 'I believe', 'it seems', 'it looks like', 'it appears'.",
        # " Crawl pricing page and provide the pricing information."
        # ,
        # " - pricing_plans: an array of pricing plans, if pricing is available.",
    ],
    show_tool_calls=True,
    use_json_mode=True,
    debug_mode=True,
)

# agent.print_response("AI tool website: https://base44.com/")
agent.print_response("AI tool website: https://groas.ai/")
# agent.print_response("AI tool website: https://www.stagehand.dev/")
# agent.print_response("AI tool website: https://v0.dev/")
# agent.print_response("AI tool website: https://emastered.com/")
# agent.print_response("AI tool website: https://neosvg.com/", markdown=True)
# agent.print_response("AI tool website: https://www.tavily.com/")
# agent.print_response("AI tool website: https://cline.bot/")
# agent.print_response("AI tool website: https://www.trynia.ai/")
# agent.print_response("AI tool website: https://www.waves.com/illugen")
# agent.print_response("AI tool website: https://www.get-teleprompt.com/")
