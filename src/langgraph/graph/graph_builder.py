from langgraph.graph import StateGraph, START, END
from src.langgraph.state.state import State
from src.langgraph.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph.tools.search_tool import get_tools, create_tool_nodes
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgraph.nodes.chatbot_with_websearch import ChatbotWithWebSearchNode
from src.langgraph.nodes.ai_news_node import AINewsNode

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
        obj_chatbot_with_websearch = ChatbotWithWebSearchNode(llm)
        chatbot_node = obj_chatbot_with_websearch.create_chatbot(tools)
        #Add Node
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)
        #Edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def ai_news_builder_graph(self):
        '''Build a news generator using langgraph & Tavily.'''
        
        ai_news_node = AINewsNode(self.llm)
        
        #Added Nodes
        self.graph_builder.add_node("fetch_news", ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news", ai_news_node.summarize_news)
        self.graph_builder.add_node("save result", ai_news_node.save_result)
        #Added Edges
        self.graph_builder.set_entry_point("fetch_news") #Same as making edge from START to "fetch_news"
        self.graph_builder.add_edge("fetch_news", "summarize_news")
        self.graph_builder.add_edge("summarize_news", "save result")
        self.graph_builder.add_edge("save result", END) #Same as making edge from "save result" to END



    def setup_graph(self, usecase):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        elif usecase == "Chatbot with WebSearch":
            self.chatbot_with_websearch_build_graph()
        
        elif usecase == "AI News":
            self.ai_news_builder_graph()

        else:
            raise ValueError(f"Invalid use case: {usecase}")

        return self.graph_builder.compile()