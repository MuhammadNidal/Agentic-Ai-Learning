# import langchain
# print("LangChain installed successfully")



# from langchain_community.document_loaders import CSVLoader

# loader = CSVLoader(file_path="recipe_template.csv")
# documents = loader.load()

# print(documents[1].page_content)


# from langchain_community.document_loaders import TextLoader

# loader = TextLoader("notes.txt")
# documents = loader.load()

# print(documents[0].page_content)





# from langchain_text_splitters import RecursiveCharacterTextSplitter

# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=100,
#     chunk_overlap=20
# )

# chunks = text_splitter.split_documents(documents)
# print(chunks[0].page_content)


from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load document
loader = CSVLoader(file_path="recipe_template.csv")
documents = loader.load()

# Split document
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# FREE & LOCAL embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store in Chroma DB
vectorstore = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("✅ Data ingested successfully!")


results = vectorstore.similarity_search(
"check the record ali data is present or not?",
    k=1
)
print(results[0].page_content)

# results = vectorstore.similarity_search(
#     "Is there a user named Ali Khan?",
#     k=2
# )

# for r in results:
#     print(r.page_content)










# What is happening here?
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=50
# )


# This code is splitting a long text into smaller pieces (chunks) so it’s easier for an LLM to read, search, or store in embeddings.
# 1️⃣ chunk_size = 500
# 👉 This means:
# Each chunk will contain up to 500 characters
# Characters include letters, spaces, punctuation, etc.
# Example
# If your text is:
# "This is a very long document with thousands of characters..."
# It will be split like:
# Chunk 1 → characters 1–500
# Chunk 2 → characters 451–950
# Chunk 3 → characters 901–1400

# So 500 characters per chunk.
# 2️⃣ chunk_overlap = 50
# 👉 This means:
# Each chunk shares 50 characters with the previous chunk
# This avoids losing context between chunks
# Why overlap is important?
# Without overlap, the model might miss meaning at the boundary.
# 🔍 Simple Visual Example
# Imagine this text (numbers = character positions):

# 1----------------------------------------500
#                                            451----------------------------------------950

# Chunk breakdown:
# Chunk 1
# Characters 1 → 500
# Chunk 2
# Characters 451 → 950
# 👉 The 50 characters (451–500) appear in both chunks



# What is stored inside chroma_db?
# When you run:
# vectorstore = Chroma.from_documents(
#     docs,
#     embedding=embeddings,
#     persist_directory="./chroma_db"
# )
# Chroma stores 4 main things:
# 1️⃣ Vector embeddings (MOST IMPORTANT)
# These are numbers created by your embedding model.
# Example (conceptually):
# [0.012, -0.44, 0.98, 0.001, ...]
# ✔ Used for:
# Semantic search
# Similarity matching
# RAG (Retrieval-Augmented Generation)
# 📌 This is the core purpose of Chroma.
# 2️⃣ Original text chunks
# Your docs are usually split text chunks like:
# "LangChain is a framework for developing applications..."
# ✔ Stored so Chroma can:
# Return the actual text
# Not just numbers
# 3️⃣ Metadata
# Extra info attached to each chunk, for example:

# {
#   "source": "book.pdf",
#   "page": 12
# }
# ✔ Used for:
# Filtering
# Showing source references
# Debugging search results

# 4️⃣ Indexes & database files
# Internal files such as:
# chroma.sqlite3
# index/
# collections/
# ✔ Used by Chroma to:
# Search fast
# Organize vectors efficiently
# ⚠️ You normally never touch these files manually.