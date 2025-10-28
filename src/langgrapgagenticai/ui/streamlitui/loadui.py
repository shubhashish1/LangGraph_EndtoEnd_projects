# Here we will be loading the ui page
# Here basically we will prepare all the ui elements
# The display_result file will be only to render the output to the user.

import streamlit as st
import os
from datetime import date
from src.langgrapgagenticai.ui.uiconfigfile import Config

# Now we will be sending the output message either as HumanMessage or AI Message depending on the scenario

from langchain_core.messages import AIMessage, HumanMessage

class LoadStreamlitUI:
    def __init__(self):
        # For ui page design to make the models show in the ui and also the backend configs has to come from a
        # configuration setup which we can call as config file. So we will have a uiconfigfile.ini
        # .ini is a set up file that stores the config setup just like a ymal file setting, So we store data in keyvalue
        self.config = Config()
        # Now let's load the user controls that we are getting from uiconfigfile.ini file
        self.user_controls = {}

    # Now let's write code to load the streamlit ui

    def load_streamlit_ui(self):
        st.set_page_config(page_title= self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False # TO track whether the button is clickedd on not
        st.session_state.IsSDLC = False

        # Now let's load the sidebar 

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_option()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options) # Here used the use controls to provide option for user to select the llm they want

            if self.user_controls["selected_llm"] == "Groq":
                # model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                # Here we have created a dropbox or selectbox of usercontrol types