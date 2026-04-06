from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    '''Return the tools to be used in the graph.'''
    tools = [TavilySearchResults(max_results=2)]
    return tools

def create_tool_nodes(tools):
    '''Create tool nodes for the graph.'''
    return ToolNode(tools=tools)