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
        self.user_controls = {} # Created a empy dict to capture all the user selections

    def initialize_session(self):
        # Here initialize_session is the function where we will create the session state dict
        # with some keys and their default values. If it is complex, create only this: 
        # if "state" not in st.session_state:
        #      st.session_state.state = []
        return {
            "current_step": "requirements",
            "requirements": "",
            "user_stories": "",
            "po_feedback": "",
            "generated_code": "",
            "review_feedback": "",
            "decision": None
        }
    
    # def render_requirements(self):
    #     st.markdown("## 📝 Requirements Submission")
    #     st.session_state.state["requirements"] = st.text_area(
    #         "Enter your requirements:",
    #         height= 200,
    #         key="req_input"
    #     )
    #     if st.button("Submit your requirements", key="submit_req"):
    #         st.session_state.state["current_step"] = "generate_user_stories"
    #         st.session_state.IsSDLC = True

    def load_streamlit_ui(self):
        # We have to get the page title from the config file 
        # Hence we need to set the page_config from which we will get the page title to display
        
        st.set_page_config(page_icon="robot", page_title=self.config.get_page_title(), layout= "wide")
        # Now once this is set we have to put the header to display
        st.header(f"🤖🧠🇦🇮👾 {self.config.get_page_title()}")

        # Now let's create the session_state list and the keys
        st.session_state.timeframe= ''
        st.session_state.IsFetchButtonClicked= False
        st.session_state.IsSDLC = False

        # Let's first create the sidebar
        with st.sidebar:
            # Get the options from config
            llm_options = self.config.get_llm_option()
            usecase_options = self.config.get_usecase_options()

            # Now we will use these in our st selectbox
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                # Select the model from selectbox
                model_options = self.config.get_groq_model_options()

                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)

                # Let's get the api key from the user
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key",
                                                                                                      type="password")
                
                # If not given by the user then we have to show a message to enter api key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("🚨 Please enter your GROQ API KEY to procced. Don't have? refer: https://console.groq.com/keys")

            # Now we are done with the model selection with API key and here we have added emoji in the warning message
            # Let's do the usecase selection now from the select box
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", usecase_options)

            # Now since we have more than one usecase, we will have to provide condition if a usecase
            # is selected then we need to cal it's graph, if b is selected call b graph
            if self.user_controls["selected_usecase"] == "Chatbot with Tool":
                # Now we have to enable the tavily api key input for the user here
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY_API_KEY",
                                                                                                                                         type="password")
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY_API_KEY to porceed")

            # Now let's check if we have the session state present or not else we will create
            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session() # Here we are adding state to the session_state
                # which is generated from initialize_session function with some keys defined
                # So basically the structure will be session_state will have the key state, timeframe, IsSDLC etc
                # and the state key will have further more keys of itself which are coming from initialize_session()
                # Here initialize_session is the function where we will create the session state dict
                # with some keys and their default values. If it is complex, create only this: 
                # if "state" not in st.session_state:
                #      st.session_state.state = []
            # self.render_requirements() # This is the function which will help us get the user requirements
            # as a new requirement in the sidebar itself
        # All done now we will return all the user controls captured
        return self.user_controls

        # Till this elemts we have only created the sidebar, the chat_messages are not yet created
###################################################################################
    # def initialize_session(self):
    #     # Here we are declaring all the keys we are storing in the session
    #     # This is a structure we have created to store the session details of each use case one by one
    #     return {
    #         "current_step": "requirements",
    #         "requirements": "",
    #         "user_stories": "",
    #         "po_feedback": "",
    #         "generated_code": "",
    #         "review_feedback": "",
    #         "decision": None
    #     }
    
    # def render_requirements(self):
    #     st.markdown("## Requirements Submission")
    #     st.session_state.state["requirements"] = st.text_area(
    #         "Enter your requirements:",
    #         height=200,
    #         key="
    # req_input"
    #     ) # Here requirements is nothing but the user queries

    #     if st.button("Submit Requirements", key="Submit Req"):
    #         st.session_state.state["current_step"] = "generate_user_stories"
    #         st.session_state.IsSDLC = True

    # # Now let's write code to load the streamlit ui

    # def load_streamlit_ui(self):
    #     st.set_page_config(page_title= self.config.get_page_title(), layout="wide")
    #     st.header(self.config.get_page_title())
    #     st.session_state.timeframe = ''
    #     st.session_state.IsFetchButtonClicked = False # TO track whether the button is clickedd on not
    #     st.session_state.IsSDLC = False

    #     # Now let's load the sidebar 

    #     with st.sidebar:
    #         # Get options from config
    #         llm_options = self.config.get_llm_option()
    #         usecase_options = self.config.get_usecase_options()

    #         # LLM selection
    #         self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options) # Here used the use controls to provide option for user to select the llm they want

    #         if self.user_controls["selected_llm"] == "Groq":
    #             # model selection
    #             model_options = self.config.get_groq_model_options()
    #             self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
    #             # Here we have created a dropbox or selectbox of usercontrol types
    #             # Now let's get the input of the api key the user is giving
    #             self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API_KEY",
    #                                                                                                   type="password")
    #             # Validate API key to check the api key provided is valid or not
    #             if not self.user_controls["GROQ_API_KEY"]:
    #                 st.warning("Please enter your groq api key to proceed. Don't have? refer: https://console.groq.com/keys")

    #             # Use case selection
    #             self.user_controls["selected_usecase"] = st.selectbox("Select One Usecase", usecase_options)

    #             if "state" not in st.session_state:
    #                 st.session_state.state = self.initialize_session()
    #             self.render_requirements() # This is a function to load all the right side part of the ui
    #             # We have rthe sidebar loaded first and then we should have the right side part loaded
            
    #         return self.user_controls