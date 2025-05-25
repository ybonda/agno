from agno.agent import Agent
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.spider import SpiderTools
from agno.tools.website import WebsiteTools
from agno.models.openrouter import OpenRouter

# MODEL= "google/gemini-2.0-flash-001"
# MODEL = "openai/gpt-4.1-nano"
MODEL= "google/gemini-2.5-flash-preview-05-20"

agent = Agent(
    model=OpenRouter(id=MODEL),
    tools=[GoogleSearchTools(fixed_language="English")],
    # tools=[GoogleSearchTools(fixed_language="English"), WebsiteTools()],
    # description="You are a news agent that helps users find the latest news.",
    # instructions=[
    #     "Given a topic by the user, respond with 4 latest news items about that topic.",
    #     "Search for 10 news items and select the top 4 unique items.",
    #     "Search in English.",
    #     "Return links to the articles.",
    # ],
    description="You are AI exprert that helps users find information about AI tools.",
    instructions=[
        "Given an AI tool website URL by a user, search the internet and respond in JSON format with",
        " - name: name of the tool.",
        " - short_description: short description of the tool (12 words max).",
        " - description: detailed description of the tool (30-100 words)",
        " - Explain how the tool works.",
        " - Explain how to use the tool.",
        " - Explain what are use cases.",
        " - Provide strong pros for why this tool is better than the alternatives based on actual search results.",
        " - Provide strong cons for why this tool is worse than the alternatives based on actual search results.",
        " - Provide 1-3 alternative tools.",
        " Crawl pricing page and provide the pricing information.",
        " - You must fetch the latest details on their pricing plans, if pricing is available.",
    ],
    show_tool_calls=True,
    use_json_mode=True,
    debug_mode=True,
)

agent.print_response("AI tool website: https://base44.com/")
# agent.print_response("AI tool website: https://v0.dev/")
# agent.print_response("AI tool website: https://emastered.com/", markdown=True)
# agent.print_response("AI tool website: https://neosvg.com/", markdown=True)
# agent.print_response("AI tool website: https://www.tavily.com/", markdown=True)
# agent.print_response("AI tool website: https://cline.bot/", markdown=True)
