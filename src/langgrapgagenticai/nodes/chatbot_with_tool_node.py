# Here we need to take the toolnode and bind it with llm so that we can be able to use in our graph

from src.langgrapgagenticai.state.state import State

class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration
    """
    def __init__(self, model):
        self.llm = model

    # We need to create a tool condition which will be used as an edge to connect the toolnode
    # to the graph

    def process(self, state: State) -> dict:
        """
        Calls this to generate response from tools once toolnode is called
        """
        # First we have to get the user query where we need to call toolnode
        user_input = state["messages"][-1] if state["messages"] else ""

        # Now let's put this user query as user message
        user_query = self.llm.invoke([{"role": "user", "content": user_input}])

        return {"messages": [user_query]}
    
    # Now as we have now the user query we need to get the response from toolnode
    # by binding the toolnode to llm
    def create_chatbot(self, tools):
        # Here we will be wrting the code to bind the tools to llm so that llm can use it
        # whenever we have tool call
        """
        Returns a chatbot node function
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}
            # Here we are returning the output of llm_with_tools by taking the user message
            # from state["messages"]
        return chatbot_node
    
    # Now with this our toolnode creation process is done. Next we will go to the graphBuilder.
    # to add the node and edge to the graph