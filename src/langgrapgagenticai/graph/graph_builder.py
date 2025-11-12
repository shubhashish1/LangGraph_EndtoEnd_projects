from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

from src.langgrapgagenticai.state.state import State
from src.langgrapgagenticai.nodes.baisc_chatbot_node import BasicChatBotNode

from src.langgrapgagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgrapgagenticai.tools.search_tool import get_tools, create_tool_node

class GraphBuilder:

    def __init__(self, model):
        self.llm = model
        # StateGraph is the structure of the entire langgraph by connecting all the nodes with conditional edges
        # So to design our graph we need to have StateGraph
        self.graph_builder = StateGraph(State)
        # Now as we have the StateGraph, we also need to have the state management class track the states
        # we will do it here in the state folder

        """
        Example to understand what's happening:

        # Now let's build the graph

        builder=StateGraph(State)                     # We are calling the State class here which we can then use to get/update the states of all nodes

        builder.add_node("first_node", first_node)    # Here the state variable will be the variable of State class which is already called in
                                                      # StateGraph
        builder.add_node("second_node", second_node)
        builder.add_node("third_node", third_node)

        
        # So here the skeleton is done, now we will be joining the edges to complete the graph
        """
    # Here we have the graph_builder class created, now we need to add nodes here from the nodes folder to load the
    # nodes in the graph_builder to build the graph

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initiates a chatbot node using BasicChatBotNode class
        and integrates it into the graph. The chatbot node is set both as entry and exit point of the graph
        """
        self.basic_chatbot_node = BasicChatBotNode(self.llm)
        # Now let's add the node in the buider by adding the node class's execution function
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)

        # Now let's add edges

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    # We can have multiple usecases here, and then we can execute them based on selection, to do that we need to have a
    # function here which can be able to do that selection here based on user input

    # We need to have the function here to get the toolnode graph setup done
    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tools integration.
        This method creates a chatbot graph that includes both a chatbot node
        and a tool node. It defines tools, initilizes the chatbot with tool
        capabilities and set up conditional and direct edges between nodes.
        The chatbot node is set as entry point
        """

        # Define the tool and toolnode
        tools = get_tools()
        tool_node = create_tool_node(tools)

        # Now let's define the llm
        llm = self.llm

        # Now let's create the chatbot node here in the graph to access
        obj_chatbot_with_node = ChatbotWithToolNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools=tools)

        # Now let's create the graph
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        # Define conditional and direct edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        # tools_condition default function given by langgraph
        # If the latest message(result) from assistant is tool call then tools_condition routes to tools
        # If the latest message(result) from assistant is not a tool call then tools_condition routes to END
        self.graph_builder.add_edge("tools", END)

    def setup_graph(self, usecase: str):
        """Calls the specific graph for selected usecase"""
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "Chatbot with Tool":
            self.chatbot_with_tools_build_graph()
        return self.graph_builder.compile()