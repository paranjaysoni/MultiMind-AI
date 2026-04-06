'''Node Defination for chatbopt with WebSearch Functionality. This node will use the tools from Tavily to perform web search and other functions.'''

from src.langgraph.state.state import State
from langchain_core.messages import AIMessage

class ChatbotWithWebSearchNode:
    '''Chatbot with WebSearch Logic Implementation'''
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        user_message = state["messages"][-1].content
        response = self.llm.invoke(state["messages"])
        return {
            "messages": [response]
        }
    
    def create_chatbot(self, tools):
        '''Returns a chatbot node function'''
        llm_with_tool = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            '''Chatbot logic for processing the input state and returning a response'''
            return {"messages": [llm_with_tool.invoke(state["messages"])]}
        
        return chatbot_node