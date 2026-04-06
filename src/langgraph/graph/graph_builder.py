from langgraph.graph import StateGraph, START, END
from src.langgraph.state.state import State
from src.langgraph.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph.tools.search_tool import get_tools, create_tool_nodes
from langgraph.prebuilt import tools_condition, ToolNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)
    
    def basic_chatbot_build_graph(self):
        """
        Build a basic chatbot using langgraph.
        """

        basic_chatbot_node = BasicChatbotNode(self.llm) 

        self.graph_builder.add_node("chatbot", basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_websearch_build_graph(self):
        """
        Build a chatbot with web search capabilities using langgraph & Tavily.
        """
        #Tool & Tool Node
        tools = get_tools()
        tool_node = create_tool_nodes(tools)
        #LLM
        llm = self.llm
        #Chatbot Node


        #Add Node
        self.graph_builder.add_node("chatbot", "")
        self.graph_builder.add_node("tools", tool_node)
    
        #Edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)


    def setup_graph(self, usecase):
        """
        Setup the graph according to the use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "Chatbot with WebSearch":
            self.chatbot_with_websearch_build_graph()

        else:
            raise ValueError("Invalid use case")

        return self.graph_builder.compile()