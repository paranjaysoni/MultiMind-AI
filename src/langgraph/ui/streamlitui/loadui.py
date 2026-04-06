import streamlit as st
import os

from src.langgraph.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), page_icon=self.config.get_page_icon())
        st.title(self.config.get_page_title())


        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_use_cases()

            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)

            self.user_controls["selected_usecase"]=st.selectbox("Select Usecases",usecase_options)

        return self.user_controls
