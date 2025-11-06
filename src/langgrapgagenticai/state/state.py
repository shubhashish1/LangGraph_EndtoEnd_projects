from typing import Annotated, Literal, Optional, TypedDict, List
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage

class State(TypedDict): # Here TypedDict is we are storing the info in dict format with keys and values
    """
    Represents the structure of the state used in the graph
    """
    messages: Annotated[list, add_messages] # We are using annotated to append the list with any new messages coming
    # via add_messages in run time as messages key. So messages is the key for the state dict and the list of messages
    # are the values here