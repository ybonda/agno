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
        " - description: detailed description of the tool (50-200 words)",
        " - how_it_works: Explain how the tool works.",
        " - how_to _use: Explain how to use the tool.",
        " - use_cases: Explain what are use cases.",
        " - pros: Provide 1-4 strong pros for why this tool is better than the alternatives based on actual search results.",
        " - cons: Provide 1-3 strong cons for why this tool is worse than the alternatives based on actual search results.",
        " - alternatives: Provide 1-3 alternative tools.",
        " - tags: select 1-2 best matching tags ONLY from the list: Project Management, Business Forecasting, Business Automation, Social Media, Ethical AI Tools, Virtual Performers, Chatbots, Content Strategy, 3D Design, Fashion AI, Academic Writing, Writing Tools, Graphic Design, DevOps Assistants, Life Assistants, Fitness Apps, Automation Tools, Real Estate Analysis, Prompt Generators, Mental Health, Meeting Assistants, Travel Planning, Non-profit Solutions, Video Editing, No-Code Platform, Animation, Security, Coding Assistants, E-learning, Medical AI, Speech-to-Text, Science, App Builders, Blockchain AI, Environmental Monitoring, Chat Summarizers, Text-to-3D, Data Analysis, Fun AI, E-commerce Tools, Investment Tools, Robotics, Music Generation, Avatar Generation, Language Learning, Compliance, Gaming AI, Coocking AI, Quantum Computing AI, API, AI for Social Good, Knowledge Management, Marketing Tools, Resume Builders, Financial Analysis, Manufacturing AI, News, Art Generators, Research, Presentation, Storytelling, Video Generation, Translation, SEO Tools, Personal Development, Voice Assistants, Image Generation, Food AI, Voice Generation, Event Planning, Consulting, Adult Content, Storyboarding, Legal AI Tools, VR & AR, Task Management, Human Resources, Sports AI, Telemedicine, Recruitment, Customer Service, Vibe Coding, Parenting AI, Business Intelligence, Dating AI, Medical Diagnosis, CRM, Image to Video, Text to Video, Video to Video."
        "- category: select the best matching single category ONLY from the list: Healthcare & Wellness, Gaming & Entertainment, Developer Tools, Image & Art, Education & Research, Productivity, 3D & Spatial, Audio & Voice, Lifestyle & Personal, Professional Services, Communication, News & Media, Business & Finance, Video & Animation, Content Creation, Social Impact, NSFW, Industry-Specific AI.",

        # " Crawl pricing page and provide the pricing information.",
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
agent.print_response("AI tool website: https://cline.bot/")
