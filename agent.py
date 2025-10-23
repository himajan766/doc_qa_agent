import os
import sys
from tkinter import Tk, filedialog
from dotenv import load_dotenv
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    UnstructuredMarkdownLoader,
    CSVLoader,
    UnstructuredHTMLLoader,
    JSONLoader,
    UnstructuredExcelLoader
)
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables from .env file
load_dotenv()

# Check API key is set
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please add it to your .env file: OPENAI_API_KEY=your-key-here")

def select_file():
    """Open a file picker dialog to select a document"""
    root = Tk()
    root.withdraw()  # Hide the main window
    root.attributes('-topmost', True)  # Bring dialog to front
    
    file_path = filedialog.askopenfilename(
        title="Select a document to analyze",
        filetypes=[
            ("All Supported", "*.pdf *.txt *.docx *.md *.csv *.html *.htm *.json *.xlsx *.xls"),
            ("PDF files", "*.pdf"),
            ("Text files", "*.txt"),
            ("Word documents", "*.docx"),
            ("Markdown files", "*.md"),
            ("CSV files", "*.csv"),
            ("HTML files", "*.html *.htm"),
            ("JSON files", "*.json"),
            ("Excel files", "*.xlsx *.xls"),
            ("All files", "*.*")
        ]
    )
    root.destroy()
    return file_path

# Step 1: Load document with automatic format detection
def load_document(file_path: str):
    """Load document based on file extension"""
    ext = os.path.splitext(file_path)[1].lower()
    
    loaders = {
        '.pdf': PyPDFLoader,
        '.txt': TextLoader,
        '.docx': Docx2txtLoader,
        '.md': UnstructuredMarkdownLoader,
        '.csv': CSVLoader,
        '.html': UnstructuredHTMLLoader,
        '.htm': UnstructuredHTMLLoader,
        '.json': JSONLoader,
        '.xlsx': UnstructuredExcelLoader,
        '.xls': UnstructuredExcelLoader,
    }
    
    if ext not in loaders:
        raise ValueError(f"Unsupported file format: {ext}. Supported formats: {', '.join(loaders.keys())}")
    
    loader_class = loaders[ext]
    
    # Special handling for JSON files (requires jq_schema parameter)
    if ext == '.json':
        loader = loader_class(file_path, jq_schema='.', text_content=False)
    else:
        loader = loader_class(file_path)
    
    return loader.load()

if __name__ == "__main__":
    # Get document path from command line argument or file picker
    if len(sys.argv) > 1:
        document_path = sys.argv[1]
        print(f"Loading document: {document_path}")
    else:
        print("Please select a document to analyze...")
        document_path = select_file()
        
        if not document_path:
            print("No file selected. Exiting.")
            sys.exit(0)
        
        print(f"Selected: {document_path}")
    
    # Check if file exists
    if not os.path.exists(document_path):
        print(f"Error: File not found: {document_path}")
        sys.exit(1)
    
    print("Loading and processing document...")
    
    try:
        # Load document
        docs = load_document(document_path)
        
        # Step 2: Split into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(docs)
        print(f"Document split into {len(chunks)} chunks")
        
        # Step 3: Create embeddings + vector store
        print("Creating embeddings (this may take a moment)...")
        embeddings = OpenAIEmbeddings()
        vector_store = Chroma.from_documents(chunks, embeddings)
        
        # Step 4: Retriever
        retriever = vector_store.as_retriever(search_kwargs={"k": 5})
        
        # Step 5: LLM
        llm = OpenAI(temperature=0.0)
        
        # Step 6: Answer function
        def answer_question(question: str):
            retrieved = retriever.invoke(question)
            if not retrieved:
                return "I'm sorry — I don't have enough information in the document to answer that."
            
            context = "\n\n".join([doc.page_content for doc in retrieved])
            prompt = f"""Answer the question based only on the following context:

{context}

Question: {question}"""
            
            answer = llm.invoke(prompt)
            return answer
        
        print("\n✅ Document loaded successfully! You can now ask questions.\n")
        
        # Step 7: CLI loop
        while True:
            q = input("Enter question (or 'quit'): ")
            if q.lower() == "quit":
                print("Goodbye!")
                break
            print("Answer:", answer_question(q))
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
