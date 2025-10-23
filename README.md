# 📄 Document QA Agent

An intelligent AI-powered question-answering agent that uses **LangChain** and **OpenAI** to answer questions from any document you upload. Simply select a file, ask questions, and get accurate answers based on the document's content!

## 🚀 Features

- **Multi-Format Support**: Works with PDF, Word, Text, Markdown, CSV, HTML, JSON, and Excel files
- **Automatic Format Detection**: Intelligently detects and processes different file formats
- **Interactive File Selection**: Easy-to-use GUI file picker or command-line interface
- **Context-Aware Answers**: Uses RAG (Retrieval-Augmented Generation) to provide accurate, context-based responses
- **Real-time Q&A**: Ask unlimited questions about your document in a conversational interface

## 📋 Supported File Formats

| Format | Extensions | Description |
|--------|-----------|-------------|
| PDF | `.pdf` | Portable Document Format |
| Text | `.txt` | Plain text files |
| Word | `.docx` | Microsoft Word documents |
| Markdown | `.md` | Markdown formatted files |
| CSV | `.csv` | Comma-separated values |
| HTML | `.html`, `.htm` | Web pages |
| JSON | `.json` | JSON data files |
| Excel | `.xlsx`, `.xls` | Microsoft Excel spreadsheets |

## 🛠️ Installation

### Prerequisites

- Python 3.9 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/account/api-keys))

### Step 1: Clone the Repository

```bash
git clone https://github.com/himajan766/doc_qa_agent.git
cd doc_qa_agent
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

Create a `.env` file in the project root directory:

```bash
# .env file
OPENAI_API_KEY=your-openai-api-key-here
```

Replace `your-openai-api-key-here` with your actual OpenAI API key.

## 🎯 Usage

### Method 1: Interactive File Picker (Recommended)

Simply run the script and a file browser will open:

```bash
python agent.py
```

1. A file picker dialog will appear
2. Select any supported document
3. Wait for the document to be processed
4. Start asking questions!

### Method 2: Command Line Argument

Pass the file path directly:

```bash
python agent.py /path/to/your/document.pdf
```

### Example Session

```bash
$ python agent.py

Please select a document to analyze...
Selected: /Users/john/Documents/research_paper.pdf
Loading and processing document...
Document split into 45 chunks
Creating embeddings (this may take a moment)...

✅ Document loaded successfully! You can now ask questions.

Enter question (or 'quit'): What is the main topic of this document?
Answer: The main topic of this document is machine learning applications in healthcare...

Enter question (or 'quit'): What methods were used?
Answer: The document describes three primary methods: supervised learning, neural networks...

Enter question (or 'quit'): quit
Goodbye!
```

## 🧪 Testing the Agent

### Quick Test with Sample Documents

1. **Test with a text file:**
   ```bash
   echo "The quick brown fox jumps over the lazy dog. This is a test document about animals." > test.txt
   python agent.py test.txt
   ```
   Ask: "What animal is mentioned?"

2. **Test with your own PDF:**
   - Find any PDF on your computer (resume, research paper, book chapter)
   - Run `python agent.py` and select it
   - Ask questions about its content

3. **Test with a CSV file:**
   - Use any CSV with data
   - Ask questions about the data patterns or specific values

### Sample Questions to Try

- "What is this document about?"
- "Summarize the main points"
- "What are the key findings?"
- "Who is mentioned in this document?"
- "What dates are mentioned?"
- "List the main topics covered"

## 🏗️ How It Works

```
┌─────────────────┐
│  User uploads   │
│   document      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Auto-detect    │
│  file format    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Load & parse   │
│  document       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Split into     │
│  chunks         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Create         │
│  embeddings     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Store in       │
│  vector DB      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  User asks      │
│  question       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Retrieve       │
│  relevant       │
│  chunks         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  OpenAI         │
│  generates      │
│  answer         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Display answer │
│  to user        │
└─────────────────┘
```

## 🔧 Technical Details

### Architecture

- **Document Loaders**: LangChain Community loaders for various formats
- **Text Splitting**: RecursiveCharacterTextSplitter (1000 chars, 100 overlap)
- **Embeddings**: OpenAI Embeddings API
- **Vector Store**: ChromaDB for semantic search
- **LLM**: OpenAI GPT models for answer generation
- **Retrieval**: Top-5 most relevant document chunks

### Technologies Used

- **LangChain**: Framework for LLM applications
- **OpenAI API**: GPT models and embeddings
- **ChromaDB**: Vector database for document storage
- **Python-dotenv**: Environment variable management
- **Tkinter**: GUI file picker

## 📝 Requirements

See `requirements.txt` for full list of dependencies:

- langchain >= 0.3.0
- langchain-openai >= 0.2.0
- langchain-community >= 0.3.0
- openai >= 1.0.0
- chromadb >= 0.4.0
- And more...

## ⚠️ Troubleshooting

### Common Issues

**1. "OPENAI_API_KEY not set" error**
- Make sure you created a `.env` file with your API key
- Verify the key is valid at [OpenAI Platform](https://platform.openai.com)

**2. "Import error" for langchain modules**
- Run: `pip install --upgrade -r requirements.txt`
- Restart your terminal/IDE

**3. "File not found" error**
- Ensure the file path is correct
- Use the file picker to avoid path issues

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

Created by [@himajan766](https://github.com/himajan766)

## 🙏 Acknowledgments

- Built with [LangChain](https://www.langchain.com/)
- Powered by [OpenAI](https://openai.com/)
- Vector storage by [ChromaDB](https://www.trychroma.com/)

---

**⭐ If you find this useful, please star this repository!**
