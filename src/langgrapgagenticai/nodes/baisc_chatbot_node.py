from src.langgrapgagenticai.state.state import State

class BasicChatBotNode:
    """
    Basic chatbot logic implementation
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Process the input state and generate the chatbot responses
        """
        return {"messages": self.llm.invoke(state["messages"])}
        # Since it is a baisc chatbot and we have to only get the responses from a llm directly as it is we will be
        # processing the user query here and returning the response provided by the llm as it is 