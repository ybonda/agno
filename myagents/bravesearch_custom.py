import json
import os
from typing import Optional

import requests
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools import Toolkit
from agno.utils.log import log_info, log_error


class BraveSearchCustomTools(Toolkit):
    """
    Custom Brave search tool that uses the Brave API directly.
    
    Args:
        api_key (Optional[str]): Brave API key. If not provided, will use BRAVE_API_KEY environment variable.
        fixed_max_results (Optional[int]): A fixed number of maximum results.
        fixed_country (Optional[str]): A fixed country code for search results.
        fixed_language (Optional[str]): A fixed language for search results.
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        fixed_max_results: Optional[int] = None,
        fixed_country: Optional[str] = None,
        fixed_language: Optional[str] = None,
        **kwargs,
    ):
        self.api_key = api_key or os.getenv("BRAVE_API_KEY")
        if not self.api_key:
            raise ValueError("BRAVE_API_KEY is required. Please set the BRAVE_API_KEY environment variable.")
        
        self.fixed_max_results = fixed_max_results
        self.fixed_country = fixed_country
        self.fixed_language = fixed_language
        
        tools = []
        tools.append(self.brave_search)
        
        super().__init__(name="brave_search_custom", tools=tools, **kwargs)
    
    def brave_search(
        self,
        query: str,
        max_results: Optional[int] = None,
        country: Optional[str] = None,
        search_lang: Optional[str] = None,
    ) -> str:
        """
        Search Brave for the specified query and return the results.
        
        Args:
            query (str): The query to search for.
            max_results (int, optional): The maximum number of results to return. Default is 5.
            country (str, optional): The country code for search results. Default is "us".
            search_lang (str, optional): The language of the search results. Default is "en".
            
        Returns:
            str: A JSON formatted string containing the search results.
        """
        max_results = self.fixed_max_results or max_results or 5
        country = self.fixed_country or country or "us"
        search_lang = self.fixed_language or search_lang or "en"
        
        if not query:
            return json.dumps({"error": "Please provide a query to search for"})
        
        log_info(f"Searching Brave for: {query}")
        
        try:
            response = requests.get(
                "https://api.search.brave.com/res/v1/web/search",
                headers={
                    "X-Subscription-Token": self.api_key,
                },
                params={
                    "q": query,
                    "count": max_results,
                    "country": country,
                    "search_lang": search_lang,
                },
            )
            
            if response.status_code == 200:
                data = response.json()
                
                filtered_results = {
                    "web_results": [],
                    "query": query,
                    "total_results": 0,
                }
                
                if "web" in data and "results" in data["web"]:
                    web_results = []
                    for result in data["web"]["results"]:
                        web_result = {
                            "title": result.get("title", "No title"),
                            "url": result.get("url", "No URL"),
                            "description": result.get("description", "No description"),
                        }
                        web_results.append(web_result)
                    filtered_results["web_results"] = web_results
                    filtered_results["total_results"] = len(web_results)
                
                return json.dumps(filtered_results, indent=2)
            else:
                error_msg = f"API call failed with status code {response.status_code}: {response.text}"
                log_error(error_msg)
                return json.dumps({"error": error_msg})
                
        except Exception as e:
            error_msg = f"Error making API request: {str(e)}"
            log_error(error_msg)
            return json.dumps({"error": error_msg})


MODEL = "openai/gpt-4o-mini"

agent = Agent(
    model=OpenRouter(id=MODEL),
    tools=[BraveSearchCustomTools()],
    description="You are a pricing expert in ai tools and services.",
    instructions=[
        "Given the website of the ai tool or service, respond with the pricing details."
    ],
    tool_call_limit=1,
    show_tool_calls=True,
)
agent.print_response("https://accessibe.com/", markdown=True)
