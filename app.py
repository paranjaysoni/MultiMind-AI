import streamlit as st
from src.langgraph.main import load_langgraph_agenticai_app

groq_api_key = st.secrets["GROQ_API_KEY"]

if __name__ == "__main__":
    load_langgraph_agenticai_app()

# Footer Credit
st.markdown("---")
st.markdown(
    "<h5 style='text-align: center; color: grey;'>Built with  ❤️  by <a href='https://github.com/paranjaysoni' target='_blank' style='color: grey; text-decoration: none;'>Paranjay Soni</a></h5>",
    unsafe_allow_html=True
)