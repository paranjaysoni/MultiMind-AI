import streamlit as st
from src.langgraph.main import load_langgraph_agenticai_app

groq_api_key = st.secrets["GROQ_API_KEY"]

if __name__ == "__main__":
    load_langgraph_agenticai_app()