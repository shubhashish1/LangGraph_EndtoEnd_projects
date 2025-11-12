# This tool will help us search on the internet
# We can call this as google for Agentic AI
# Here we can ask the user to provide their Tavily API key in ui as they can use their to get results

from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import ToolNode

# def get_tavily_tool():
#     """
#     Gets the Tavily tool to do the web search
#     """
#     return TavilySearchResults(max_results=2)

def get_tools():
    """
    Returns the list of tools to be used
    """
    tools = [TavilySearchResults(max_results=2)]
    return tools

# Let's create toolnode to use the list of tools as node in our graph
def create_tool_node(tools):
    """
    Creates and returns a toolnode for the graph
    """
    return ToolNode(tools=tools)