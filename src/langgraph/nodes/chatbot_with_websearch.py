'''Node Defination for chatbopt with WebSearch Functionality. This node will use the tools from Tavily to perform web search and other functions.'''

from src.langgraph.state.state import State

class ChatbotWithWebSearchNode:
    '''Chatbot with WebSearch Logic Implementation'''
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        '''Process the input state and generate a response using tool integration'''
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        tools_response = f"Tool Integration for: '{user_input}"

        return {"messages" : [llm_response, tools_response]}
    
    def create_chatbot(self, tools):
        '''Returns a chatbot node function'''
        llm_with_tool = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            '''Chatbot logic for processing the input state and returning a response'''
            return {"messages": [llm_with_tool.invoke(state["messages"])]}
        
        return chatbot_node