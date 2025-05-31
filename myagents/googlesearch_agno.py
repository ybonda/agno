import os
from typing import List, Dict, Optional
from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.spider import SpiderTools
from agno.tools.website import WebsiteTools
from agno.models.openrouter import OpenRouter

# Load environment variables from .env file
load_dotenv()

try:
    from pymongo import MongoClient
    from pymongo.errors import PyMongoError
except ImportError:
    raise ImportError("`pymongo` not installed. Please install it with `pip install pymongo`")

try:
    from rapidfuzz import fuzz, process
except ImportError:
    raise ImportError("`rapidfuzz` not installed. Please install it with `pip install rapidfuzz`")

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


def find_ai_tool_by_fuzzy_match(tool_name: str, threshold: int = 70) -> Optional[Dict]:
    """
    Find AI tool in database using fuzzy string matching.
    
    Args:
        tool_name: The tool name to search for (from LLM alternatives)
        threshold: Minimum similarity score (0-100) to consider a match
        
    Returns:
        Dictionary with tool info and match score, or None if no match found
    """
    try:
        db = get_mongodb_connection()
        ai_tools_collection = db["ai_tools"]
        
        # Fetch all AI tools with relevant fields
        tools_cursor = ai_tools_collection.find({}, {
            "name": 1, 
            "name_slug": 1, 
            "description": 1, 
            "ai_tool_url": 1,
            "_id": 0
        })
        
        tools = list(tools_cursor)
        
        if not tools:
            print("No AI tools found in database")
            return None
        
        best_match = None
        best_score = 0
        
        # Normalize the search term
        search_term = tool_name.lower().strip()
        
        for tool in tools:
            # Calculate fuzzy match scores for different fields
            name_score = fuzz.ratio(search_term, tool.get("name", "").lower())
            slug_score = fuzz.ratio(search_term, tool.get("name_slug", "").lower())
            
            # Also try partial matching for better results
            name_partial_score = fuzz.partial_ratio(search_term, tool.get("name", "").lower())
            slug_partial_score = fuzz.partial_ratio(search_term, tool.get("name_slug", "").lower())
            
            # Take the highest score from all matching strategies
            max_score = max(name_score, slug_score, name_partial_score, slug_partial_score)
            
            if max_score > best_score and max_score >= threshold:
                best_score = max_score
                best_match = {
                    "tool": tool,
                    "match_score": max_score,
                    "matched_field": "name" if max(name_score, name_partial_score) >= max(slug_score, slug_partial_score) else "name_slug"
                }
        
        return best_match
        
    except Exception as e:
        print(f"Error searching for AI tool '{tool_name}': {e}")
        return None


def find_alternatives_in_db(alternatives: List[str]) -> List[Dict]:
    """
    Find multiple AI tool alternatives in database using fuzzy matching.
    
    Args:
        alternatives: List of tool names from LLM response
        
    Returns:
        List of dictionaries with found tools and their match info
    """
    found_tools = []
    
    for alt_name in alternatives:
        match = find_ai_tool_by_fuzzy_match(alt_name)
        if match:
            found_tools.append({
                "original_name": alt_name,
                "found_tool": match["tool"],
                "match_score": match["match_score"],
                "matched_field": match["matched_field"]
            })
            print(f"✓ Found match for '{alt_name}': {match['tool']['name']} (score: {match['match_score']})")
        else:
            print(f"✗ No match found for '{alt_name}'")
    
    return found_tools


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
    tools=[GoogleSearchTools(fixed_language="English", fixed_max_results=13)],
    tool_call_limit=3,  # Limit to maximum 3 tool calls to control LLM usage
    description="You are AI exprert that helps users find information about AI tools.",
    instructions=[
        "Given an AI tool website URL by a user, search the internet and respond in JSON format with",
        "IMPORTANT: You have a maximum of 3 search calls, so make them count. Use comprehensive search queries.",
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
# agent.print_response("AI tool website: https://v0.dev/")
# agent.print_response("AI tool website: https://emastered.com/")
# agent.print_response("AI tool website: https://neosvg.com/", markdown=True)
# agent.print_response("AI tool website: https://www.tavily.com/")
# agent.print_response("AI tool website: https://cline.bot/")
# agent.print_response("AI tool website: https://www.trynia.ai/")
# agent.print_response("AI tool website: https://www.waves.com/illugen")
# agent.print_response("AI tool website: https://www.get-teleprompt.com/")

# Example usage of fuzzy matching for alternatives
print("\n" + "="*50)
print("TESTING FUZZY MATCHING FOR ALTERNATIVES")
print("="*50)

# Example alternatives from LLM response
sample_alternatives = ["Bubble.io", "Glide", "Replit", "Google AI Studio"]

print(f"Searching for alternatives: {sample_alternatives}")
print("-" * 30)

found_alternatives = find_alternatives_in_db(sample_alternatives)

print(f"\nFound {len(found_alternatives)} matches out of {len(sample_alternatives)} alternatives:")
for match in found_alternatives:
    tool = match["found_tool"]
    print(f"  • {match['original_name']} → {tool['name']} ({tool['ai_tool_url']}) [Score: {match['match_score']}]")
