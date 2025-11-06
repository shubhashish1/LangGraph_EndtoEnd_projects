import streamlit as st
import json
from src.langgrapgagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgrapgagenticai.LLMS.groqllm import GROQLLM
from src.langgrapgagenticai.graph.graph_builder import GraphBuilder

# Now let's load the ui elements written in loadui and then also add the chat_input option to make it conversational

def load_langgraph_agenticai_app():
    """
    This function initializes the UI, Handles user_input chat messages, displays the output
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui() # This is to load the sidebar we have created

    if not user_input:
        st.error("Error: Failed to load user input from ui")
        return
    
    # Now user_input and ai chat_message to be loaded into the body
    if st.session_state.IsFetchButtonClicked: # Getting the user message once posted and clicked the arrow button
        user_message = st.session_state.timeframe # Capturing the the time when the user asked question
    else:
        user_message = st.chat_input("Enter your message here:") # If no session created and fresh chat started

    # Now we can get the model loading details from groqllm file
    if user_message:
        try:
            # Configure llm
            obj_llm_config = GROQLLM(user_controls_input=user_input)
            # Now let's get the llm model from user_input
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initiated")
                return # This will return the message or output we have written above
            
            # Initialze and set up graph based on usecase selected
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No usecase selected")
                return
            
            # Now once we have the model, then we will have the langgraph and we need to call it and pass our model
            # to load the exact graph for the desired usecase and then provide response
            graph_builder = GraphBuilder(model)
            graph_builder.setup_graph()
            
        except Exception as e:
            raise e