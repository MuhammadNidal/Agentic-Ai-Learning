# LangChain helps you connect AI with real-world things like files, databases, APIs, memory, and tools.

# Without LangChain → AI can only talk
# With LangChain → AI can think, remember, search, and act




# Important components of LangChain:
# 🔑 Important Components of LangChain (Easy Words)
# 1️⃣ LLM (Language Model) – The Brain 🧠
# This is the AI brain that thinks and talks.
# 👉 Example: ChatGPT, Gemini, Claude

# 2️⃣ Prompt – Instructions to AI 💬
# Prompt is what you tell the AI to do.
# 👉 Example:
# “Explain this in simple words”

# 3️⃣ Prompt Template – Reusable Prompt 🔁
# Same prompt, different input.
# 👉 Example:
# “Explain {topic} in simple words”

# 4️⃣ Chain – Step-by-step process 🔗
# Chain means doing tasks one after another.
# 👉 Example:
# User question → AI → Final answer

# 5️⃣ Memory – Remembers chat 🧠💾
# Memory helps AI remember previous messages.
# 👉 Example:
# AI remembers your name in the conversation

# 6️⃣ Document Loader – Reads files 📄
# Loads data from files like:
# PDF
# Text
# CSV
# 👉 Example: Reading an insurance file

# 7️⃣ Text Splitter – Break big text ✂️
# Splits large documents into small parts.
# 👉 Why?
# AI understands small text better.

# 8️⃣ Embeddings – Text → Numbers 🔢
# Converts text into numbers so AI can serch meaning.
# 👉 Used for smart search

# 9️⃣ Vector Store – Smart storage 🗄️
# Stores embeddings for fast searching.
# 👉 Example: FAISS, Chroma

# 🔟 Retriever – Finds correct info 🔍
# Fetches only important parts from documents.

# 1️⃣1️⃣ Tools – Give AI power 🛠️
# Tools let AI:
# Use calculator
# Search web
# Call APIs
# 1️⃣2️⃣ Agent – Decision maker 🤖
# Agent decides:
# 👉 “Which tool should I use now?”

# 1️⃣3️⃣ Output Parser – Clean output 📤

# Formats AI response into:
# JSON
# List
# Table

# 🧩 Simple Flow (Easy to Remember)
# User
#  ↓
# Prompt
#  ↓
# Chain
#  ↓
# LLM
#  ↓
# Tools / Memory / Documents
#  ↓
# Answer

# 🎯 One-Line Simple Definition
# LangChain helps AI think step-by-step, remember things, read files, and use tools.



# from langchain_community.document_loaders import TextLoader

# loader = TextLoader("recipe_template.csv")
# documents = loader.load()

# print(documents[0].page_content)


# 👉 In simple words:
# LangChain helps you connect AI with real-world things like files, databases, APIs, memory, and tools.

# Without LangChain → AI can only talk
# With LangChain → AI can think, remember, search, and act

# 2️⃣ Why do we need LangChain?
# Normally, an AI model:
# Answers questions
# Has no memory
# Cannot read your files
# Cannot connect to databases
# Cannot call APIs
# LangChain solves this problem by chaining multiple steps together.

# 📌 That’s why it is called Lang + Chain
# (Language + Chain of actions).










# Real-life Example (Very Easy)
# Imagine AI is a smart student:
# ❌ Without LangChain:
# Student can only answer from memory
# ✅ With LangChain:
# Student can:
# Read books (PDF, docs)
# Search the internet
# Remember past answers
# Use calculator
# Talk to databases
# Take action








# 👉 Create virtual environment
# python -m venv venv


# This creates a folder named venv

# ▶️ Step 3: Activate Virtual Environment
# ✅ On Windows
# venv\Scripts\activate






