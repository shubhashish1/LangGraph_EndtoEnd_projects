# As soon as we click on submit button, it should be able to display the result of the ui
# Here we will stream the conversation and display it in the ui.
# Here we will be creating process to show or display result to the user

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
import json

class DisplayResultStreamlit:

    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    # Now as we know we are getting the user_input via st.user_input
    # But we are not displaying anything to the user, not his/her message or the response to their question
    # This can be achieved using st.user_message option from streamlit which we will do here in display_result_on_ui
    # 
    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot":
            # We will stream the conversation here using a loop
            for event in graph.stream({"messages": ("user", user_message)}): # Here we are streaming first the query asked by user
                print(f"Printing event: {event.values()}")
                for value in event.values(): # Here event.values() is ("user", user_message) and value is user_message
                    print(f'Printing value from event.values() {value["messages"]}')
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        print(f"The response is: {value["messages"].content}")
                        st.write(value["messages"].content)