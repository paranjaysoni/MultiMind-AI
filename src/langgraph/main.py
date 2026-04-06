import streamlit as st
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI


def load_langgraph_agenticai_app():
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    
    if not user_input:
        st.warning("Please select an LLM and a use case to proceed.")
        return 
    
    user_message = st.chat_input("Enter your message:")