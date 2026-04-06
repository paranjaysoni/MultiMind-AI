import streamlit as st
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph.LLMS.groqllm import GroqLLM
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    
    if not user_input:
        st.warning("Please select an LLM and a use case to proceed.")
        return 
    
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            #Config the LLM's
            obj_llm_config = GroqLLM(user_control_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Failed to initialize the LLM. Please check your configuration.")
                return
            
            #initialise nd setup graph according to the use case
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("No use case selected. Please select a use case to proceed.")
                return
            
            #Graph Builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            
            except Exception as e:
                st.error(f"Error setting up the graph: {e}")
                return

        except Exception as e:
            st.error(f"Error setting up the graph: {e}")
            return