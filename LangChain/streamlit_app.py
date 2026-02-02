import streamlit as st
import os
from langchain_community.document_loaders import CSVLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Document Search App",
    page_icon="🔍",
    layout="wide"
)

# Title
st.title("🔍 Document Search with LangChain")
st.markdown("Upload documents, create embeddings, and perform semantic search!")

# Sidebar for configuration
st.sidebar.header("⚙️ Configuration")

# Initialize session state
if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = None
if 'documents_loaded' not in st.session_state:
    st.session_state.documents_loaded = False

# Main content area
col1, col2 = st.columns([1, 2])

with col1:
    st.header("📁 Document Management")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Choose a file", 
        type=['csv', 'txt'],
        help="Upload CSV or TXT files"
    )
    
    # Text splitting parameters
    st.subheader("🔧 Text Splitting")
    chunk_size = st.slider("Chunk Size", 100, 1000, 500)
    chunk_overlap = st.slider("Chunk Overlap", 0, 100, 50)
    
    # Embedding model selection
    st.subheader("🤖 Embedding Model")
    embedding_models = [
        "sentence-transformers/all-MiniLM-L6-v2",
        # "sentence-transformers/all-mpnet-base-v2",
        # "sentence-transformers/distilbert-base-nli-mean-tokens"
    ]
    selected_model = st.selectbox(
        "Select Embedding Model",
        embedding_models
    )
    
    # Process button
    if st.button("🚀 Process Document", type="primary"):
        if uploaded_file is not None:
            with st.spinner("Processing document..."):
                # Save uploaded file temporarily
                temp_file_path = f"temp_{uploaded_file.name}"
                with open(temp_file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                try:
                    # Load document based on file type
                    if uploaded_file.name.endswith('.csv'):
                        loader = CSVLoader(file_path=temp_file_path)
                    else:
                        loader = TextLoader(temp_file_path)
                    
                    documents = loader.load()
                    
                    # Split documents
                    text_splitter = RecursiveCharacterTextSplitter(
                        chunk_size=chunk_size,
                        chunk_overlap=chunk_overlap
                    )
                    docs = text_splitter.split_documents(documents)
                    
                    # Create embeddings
                    embeddings = HuggingFaceEmbeddings(
                        model_name=selected_model
                    )
                    
                    # Create vector store
                    st.session_state.vectorstore = Chroma.from_documents(
                        docs,
                        embedding=embeddings,
                        persist_directory="./chroma_db"
                    )
                    
                    st.session_state.documents_loaded = True
                    st.success(f"✅ Document processed successfully! Created {len(docs)} chunks.")
                    
                except Exception as e:
                    st.error(f"❌ Error processing document: {str(e)}")
                
                finally:
                    # Clean up temp file
                    if os.path.exists(temp_file_path):
                        os.remove(temp_file_path)
        else:
            st.warning("⚠️ Please upload a file first!")

with col2:
    st.header("🔍 Semantic Search")
    
    if st.session_state.documents_loaded and st.session_state.vectorstore:
        # Search interface
        search_query = st.text_input(
            "Enter your search query:",
            placeholder="e.g., 'check the record ali data is present or not?'"
        )
        
        # Number of results
        k_results = st.slider("Number of results", 1, 10, 3)
        
        if st.button("🔎 Search", type="primary"):
            if search_query:
                with st.spinner("Searching..."):
                    try:
                        results = st.session_state.vectorstore.similarity_search(
                            search_query,
                            k=k_results
                        )
                        
                        st.subheader(f"📊 Search Results ({len(results)} found)")
                        
                        for i, result in enumerate(results, 1):
                            with st.expander(f"Result {i}", expanded=True):
                                st.write("**Content:**")
                                st.write(result.page_content)
                                
                                if result.metadata:
                                    st.write("**Metadata:**")
                                    st.json(result.metadata)
                                
                                st.divider()
                    
                    except Exception as e:
                        st.error(f"❌ Search error: {str(e)}")
            else:
                st.warning("⚠️ Please enter a search query!")
    
    else:
        st.info("📝 Please upload and process a document first to enable search functionality.")
        
        # Load existing database option
        if os.path.exists("./chroma_db"):
            st.subheader("💾 Load Existing Database")
            if st.button("Load Previous Database"):
                try:
                    embeddings = HuggingFaceEmbeddings(
                        model_name=selected_model
                    )
                    st.session_state.vectorstore = Chroma(
                        persist_directory="./chroma_db",
                        embedding_function=embeddings
                    )
                    st.session_state.documents_loaded = True
                    st.success("✅ Previous database loaded successfully!")
                    st.experimental_rerun()
                except Exception as e:
                    st.error(f"❌ Error loading database: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using LangChain, HuggingFace, and Streamlit")