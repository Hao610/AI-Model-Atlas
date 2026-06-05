import os
import streamlit as st
from core.rag_pipeline import RAGPipeline
from config.settings import settings

# Page styling settings
st.set_page_config(
    page_title="AI-Model-Atlas | Hybrid RAG Reference App",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Force elegant premium dark aesthetics
st.markdown("""
<style>
    .reportview-container {
        background: #0f172a;
    }
    .sidebar .sidebar-content {
        background: #1e293b;
    }
    h1, h2, h3 {
        color: #f8fafc !important;
        font-family: 'Outfit', 'Inter', sans-serif;
    }
    .stChatInput {
        border-radius: 8px;
    }
</style>
""", unsafe_allowed_code=True)

# Initialize Session State
if "pipeline" not in st.session_state:
    st.session_state.pipeline = RAGPipeline()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "ingested_file" not in st.session_state:
    st.session_state.ingested_file = None

st.title("🗺️ Hybrid RAG Reference Application")
st.caption("v2.1 Reference-Grade Implementation | Built on top of the AI-Model-Atlas Roadmap")

# Sidebar settings configuration panel
with st.sidebar:
    st.header("⚙️ Core Configurations")
    
    # Mode selector
    mode = st.selectbox(
        "Execution Mode (RAG_MODE)",
        options=["ollama", "api"],
        index=0 if settings.RAG_MODE == "ollama" else 1
    )
    if mode != settings.RAG_MODE:
        settings.RAG_MODE = mode
        # Re-initialize pipeline with updated settings mode
        st.session_state.pipeline = RAGPipeline()
        st.success(f"Switched system execution mode to: **{mode.upper()}**")
        
    st.divider()
    
    st.subheader("🛠️ Model Options")
    if settings.RAG_MODE == "ollama":
        settings.OLLAMA_MODEL = st.text_input("Ollama LLM Model name", value=settings.OLLAMA_MODEL)
        st.info("Ensure Ollama service is active locally and the model is pulled (`ollama pull <model>`).")
    else:
        settings.API_MODEL = st.text_input("Cloud API Model name", value=settings.API_MODEL)
        settings.API_KEY = st.text_input("API Access Key", value=settings.API_KEY, type="password")
        settings.API_BASE_URL = st.text_input("API Provider Endpoint", value=settings.API_BASE_URL)
        
    st.divider()
    
    st.subheader("📚 Parser Settings")
    chunk_size = st.slider("Chunk Character Size", min_value=100, max_value=2000, value=800, step=100)
    chunk_overlap = st.slider("Chunk Overlap Buffer", min_value=10, max_value=500, value=100, step=10)
    
    st.divider()
    st.markdown("Created by Loi Chiang Hao as part of **[AI-Model-Atlas](https://github.com/Hao610/AI-Model-Atlas)**.")

# Main dashboard interface
col_left, col_right = st.columns([3, 2])

with col_right:
    st.subheader("📂 Document Context Ingestion")
    uploaded_file = st.file_uploader("Upload a PDF document to query against", type=["pdf"])
    
    if uploaded_file is not None:
        if st.session_state.ingested_file != uploaded_file.name:
            with st.spinner("Processing text extraction, chunking, and embedding creation..."):
                os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
                save_path = os.path.join(settings.UPLOAD_DIR, uploaded_file.name)
                with open(save_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                    
                try:
                    num_chunks = st.session_state.pipeline.ingest_pdf(
                        save_path,
                        chunk_size=chunk_size,
                        chunk_overlap=chunk_overlap
                    )
                    st.session_state.ingested_file = uploaded_file.name
                    st.success(f"Successfully digested **{uploaded_file.name}** into {num_chunks} vector chunks!")
                except Exception as e:
                    st.error(f"Ingestion pipeline failure: {str(e)}")
                    
    st.subheader("🔍 Vector Retrieval Logs")
    if "latest_sources" in st.session_state and st.session_state.latest_sources:
        for idx, match in enumerate(st.session_state.latest_sources):
            with st.expander(f"Chunk Match #{idx+1} (Cosine Similarity Distance: {match['score']:.4f})"):
                st.caption(f"Source Document: {match['metadata'].get('source', 'N/A')}")
                st.code(match['content'], language="text")
    else:
        st.info("Retrieved reference context text snippets will display here when queries execute.")

with col_left:
    st.subheader("💬 Interactive RAG Assistant")
    
    # Prompt settings customizer
    system_prompt = st.text_area(
        "Custom Pipeline System Instructions",
        value="You are a helpful AI assistant. Answer the user's questions truthfully and accurately based strictly on the provided context. If the context does not contain the answer, state that you do not know.",
        height=70
    )
    
    # Display Chat logs
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    # Input field
    if user_query := st.chat_input("Ask a question based on your uploaded document..."):
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.write(user_query)
            
        with st.chat_message("assistant"):
            if not st.session_state.ingested_file:
                warning_msg = "⚠️ Please upload and process a PDF document in the right panel before querying."
                st.write(warning_msg)
                st.session_state.messages.append({"role": "assistant", "content": warning_msg})
            else:
                placeholder = st.empty()
                response_txt = ""
                
                # Run query
                stream, sources = st.session_state.pipeline.execute_query(
                    query=user_query,
                    system_prompt=system_prompt
                )
                
                # Save source states
                st.session_state.latest_sources = sources
                
                # Render streaming output
                for chunk in stream:
                    response_txt += chunk
                    placeholder.markdown(response_txt + "▌")
                placeholder.markdown(response_txt)
                
                # Save chat logs
                st.session_state.messages.append({"role": "assistant", "content": response_txt})
                # Refresh page to show updated vector source expansion logs
                st.rerun()
