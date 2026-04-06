from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
import os
import streamlit as st

def get_tools():
    '''Return the tools to be used in the graph.'''
    os.environ["TAVILY_API_KEY"] = st.secrets["TAVILY_API_KEY"]
    tools = [TavilySearchResults(max_results=2)]
    return tools

def create_tool_nodes(tools):
    '''Create tool nodes for the graph.'''
    return ToolNode(tools=tools)