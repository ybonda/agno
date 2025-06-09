from agno.agent import Agent
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.tavily import TavilyTools
from agno.models.openrouter import OpenRouter
from agno.tools.arxiv import ArxivTools

# MODEL= "google/gemini-2.0-flash-001"
MODEL = "openai/gpt-4.1-nano"

agent = Agent(
    model=OpenRouter(id=MODEL),
    description="You are SEO expert.",
    instructions=[
        "Given an AI tool home page URL by the user, tell what is the traffic rank or estimated popularity of the tool.",
    ],
    tools=[
        # GoogleSearchTools(),
        # TavilyTools(),
        ArxivTools(),
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# agent.print_response("Home page URL: https://www.vidnoz.com/, name: Vidnoz")
agent.print_response("Home page URL: https://www.accessibe.com/, name: Accessibe")
# agent.print_response("Home page URL: https://www.accessibe.com/, name: Accessibe", markdown=True)
# agent.print_response("Home page URL: https://www.firecrawl.dev/, name: Firecrawl", markdown=True)
# agent.print_response("Home page URL: https://www.alchemi.ai/, name: Alchemi", markdown=True)
# agent.print_response("Home page URL: https://www.emastered.com/, name: Emastered", markdown=True)
# agent.print_response("Home page URL: https://www.neosvg.com/, name: Neosvg", markdown=True)
# agent.print_response("Home page URL: https://www.v0.dev/, name: V0", markdown=True)
# agent.print_response("Home page URL: https://www.get-teleprompt.com/, name: Get Teleprompt", markdown=True)
# agent.print_response("Home page URL: https://www.trynia.ai/, name: Trynia", markdown=True)
# agent.print_response("Home page URL: https://www.waves.com/illugen, name: Waves Illugen", markdown=True)
