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