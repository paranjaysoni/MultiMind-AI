import streamlit as st
from langchain_groq import ChatGroq

groq_api_key = st.secrets["GROQ_API_KEY"]

class GroqLLM:
    def __init__(self, user_control_input):
        self.user_control_input = user_control_input

    def get_llm_model(self):
        try:
            selected_groq_model = self.user_control_input.get("selected_groq_model")

            llm = ChatGroq(
                api_key=groq_api_key,
                model=selected_groq_model,
            )

            return llm

        except Exception as e:
            raise ValueError(f"Error initializing GroqLLM: {e}")