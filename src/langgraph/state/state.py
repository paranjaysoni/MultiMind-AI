from typing_extensions import TypedDict, list
from langchain import add_message
from typing import Annotated

class State(TypedDict):
    '''
    Represent the structure of the state used in graph
    '''
    messages: Annotated[list, add_message]