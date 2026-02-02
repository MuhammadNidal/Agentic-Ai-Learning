import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="CSV Search App", layout="centered")

st.title("🔍 User Record Search (Chroma + LangChain)")
st.write("Ask questions about your CSV data")

# -----------------------------
# Load embeddings
# -----------------------------
@st.cache_resource
def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )
    return vectorstore

vectorstore = load_vectorstore()

# -----------------------------
# User input
# -----------------------------
query = st.text_input(
    "Enter your question",
    placeholder="e.g. Is there a user named Maria Noor?"
)

k = st.slider("Number of results", min_value=1, max_value=5, value=1)

# -----------------------------
# Search button
# -----------------------------
if st.button("Search"):
    if not query.strip():
        st.warning("Please enter a question")
    else:
        results = vectorstore.similarity_search(query, k=k)

        if results:
            st.success("Result(s) found 👇")
            for i, doc in enumerate(results, 1):
                st.markdown(f"### Result {i}")
                st.code(doc.page_content)
        else:
            st.error("No matching records found")
