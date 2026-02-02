import gradio as gr
import os
from langchain_community.document_loaders import CSVLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

class DocumentSearchApp:
    def __init__(self):
        self.vectorstore = None
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    
    def process_document(self, file, chunk_size, chunk_overlap):
        """Process uploaded document and create vector store"""
        if file is None:
            return "❌ Please upload a file first!"
        
        try:
            # Determine file type and load accordingly
            if file.name.endswith('.csv'):
                loader = CSVLoader(file_path=file.name)
            else:
                loader = TextLoader(file.name)
            
            documents = loader.load()
            
            # Split documents
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )
            docs = text_splitter.split_documents(documents)
            
            # Create vector store
            self.vectorstore = Chroma.from_documents(
                docs,
                embedding=self.embeddings,
                persist_directory="./chroma_db"
            )
            
            return f"✅ Document processed successfully! Created {len(docs)} chunks."
            
        except Exception as e:
            return f"❌ Error processing document: {str(e)}"
    
    def search_documents(self, query, num_results):
        """Search in the vector store"""
        if self.vectorstore is None:
            return "❌ Please process a document first!"
        
        if not query.strip():
            return "❌ Please enter a search query!"
        
        try:
            results = self.vectorstore.similarity_search(query, k=num_results)
            
            if not results:
                return "📝 No results found for your query."
            
            output = f"🔍 Found {len(results)} results:\n\n"
            
            for i, result in enumerate(results, 1):
                output += f"**Result {i}:**\n"
                output += f"{result.page_content}\n"
                if result.metadata:
                    output += f"*Metadata: {result.metadata}*\n"
                output += "\n" + "-"*50 + "\n\n"
            
            return output
            
        except Exception as e:
            return f"❌ Search error: {str(e)}"
    
    def load_existing_db(self):
        """Load existing database if available"""
        try:
            if os.path.exists("./chroma_db"):
                self.vectorstore = Chroma(
                    persist_directory="./chroma_db",
                    embedding_function=self.embeddings
                )
                return "✅ Existing database loaded successfully!"
            else:
                return "❌ No existing database found."
        except Exception as e:
            return f"❌ Error loading database: {str(e)}"

# Initialize the app
app = DocumentSearchApp()

# Create Gradio interface
with gr.Blocks(title="Document Search App", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🔍 Document Search with LangChain")
    gr.Markdown("Upload documents, create embeddings, and perform semantic search!")
    
    with gr.Tabs():
        # Document Processing Tab
        with gr.TabItem("📁 Document Processing"):
            with gr.Row():
                with gr.Column(scale=1):
                    file_input = gr.File(
                        label="Upload Document",
                        file_types=['.csv', '.txt']
                    )
                    chunk_size = gr.Slider(
                        minimum=100,
                        maximum=1000,
                        value=500,
                        label="Chunk Size"
                    )
                    chunk_overlap = gr.Slider(
                        minimum=0,
                        maximum=100,
                        value=50,
                        label="Chunk Overlap"
                    )
                    process_btn = gr.Button("🚀 Process Document", variant="primary")
                
                with gr.Column(scale=1):
                    process_output = gr.Textbox(
                        label="Processing Status",
                        lines=5,
                        interactive=False
                    )
                    load_existing_btn = gr.Button("💾 Load Existing Database")
            
            process_btn.click(
                app.process_document,
                inputs=[file_input, chunk_size, chunk_overlap],
                outputs=process_output
            )
            
            load_existing_btn.click(
                app.load_existing_db,
                outputs=process_output
            )
        
        # Search Tab
        with gr.TabItem("🔍 Search"):
            with gr.Row():
                with gr.Column(scale=1):
                    search_input = gr.Textbox(
                        label="Search Query",
                        placeholder="e.g., 'check the record ali data is present or not?'"
                    )
                    num_results = gr.Slider(
                        minimum=1,
                        maximum=10,
                        value=3,
                        label="Number of Results"
                    )
                    search_btn = gr.Button("🔎 Search", variant="primary")
                
                with gr.Column(scale=2):
                    search_output = gr.Textbox(
                        label="Search Results",
                        lines=15,
                        interactive=False
                    )
            
            search_btn.click(
                app.search_documents,
                inputs=[search_input, num_results],
                outputs=search_output
            )

# Launch the app
if __name__ == "__main__":
    demo.launch(share=True)