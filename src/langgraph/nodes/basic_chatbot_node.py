# We'll define what our chatbot node do? What's it's Functionality?
from src.langgraph.state.state import State


class BasicChatbotNode:
    '''Basic Chatbot Logic Implementation'''
    def __init__(self, model):
        self.llm = model

    def process(self, state) -> dict:
        '''Process the input state and return the output state'''
        return {"messages": self.llm.invoke(state["messages"])}