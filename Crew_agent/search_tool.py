from langchain_google_community import GoogleSearchAPIWrapper
from langchain_core.tools import Tool


search = GoogleSearchAPIWrapper()

def google_search():
    google_search_tool = Tool(
        name="google_search",
        description="Search Google for recent results.",
        func=search.run,
    )
    return google_search_tool
