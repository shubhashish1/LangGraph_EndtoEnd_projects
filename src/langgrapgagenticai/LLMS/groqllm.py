# Here we have to write the code which should be able to load the llm model

# Now as we know our architecture the model should be loaded from the ui by the user. Hence will have a ui page.

import os
from langchain_groq import ChatGroq
import streamlit as st


class GROQLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model = self.user_controls_input["selected_groq_model"]
            # Now if the model key is n't there there should be an error message showing to user
            if groq_api_key=="" and os.environ["GROQ_API_KEY"]=="":
                st.error("Please enter GROQ API key")
            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
        except Exception as e:
            raise ValueError(f"Error occured with exception {e}")
        return llm