# 🏥 EHR QA Agent - Medical Report AI Chatbot using RAG

A Retrieval-Augmented Generation (RAG) based chatbot that answers questions from Electronic Health Record (EHR) PDF documents using LangChain, ChromaDB, Hugging Face embeddings, Ollama, and Streamlit.

---

## 📌 Overview

This project allows users to ask questions about medical reports in natural language.

The application:

1. Loads medical PDF reports.
2. Splits documents into smaller chunks.
3. Converts chunks into vector embeddings.
4. Stores embeddings in a Chroma vector database.
5. Retrieves the most relevant context using semantic similarity search.
6. Sends the retrieved context and user question to a local LLM (Qwen2.5 via Ollama).
7. Displays the generated response through a Streamlit chat interface.

---

## 🚀 Features

- 📄 PDF document ingestion
- ✂️ Recursive text chunking
- 🔍 Semantic similarity search
- 🧠 Hugging Face sentence embeddings
- 💾 Chroma Vector Database
- 🤖 Local LLM using Ollama (Qwen2.5)
- 💬 Streamlit Chat Interface
- 🔒 Offline inference (No OpenAI API required)

---

## 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Sentence Transformers
- Ollama
- Qwen2.5
- PyPDF

---

## 📂 Project Structure

```text
ehr-qa-agent/
│
├── data/
│   └── Medical PDF Reports
│
├── create_documents.py
├── ehr_ingest.py
├── ehr_rag_pipeline.py
├── app.py
│
├── chroma_langchain_db/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Architecture

```text
Medical PDF Reports
        │
        ▼
Document Loader
        │
        ▼
Text Splitter
        │
        ▼
Sentence Embeddings
        │
        ▼
Chroma Vector Database
        │
        ▼
Similarity Search
        │
        ▼
Retrieved Context
        │
        ▼
Prompt Template
        │
        ▼
Qwen2.5 (Ollama)
        │
        ▼
Generated Answer
```

---

## 🔄 Workflow

### Document Indexing

- Load PDF reports
- Split into chunks
- Generate embeddings
- Store vectors in ChromaDB

### Question Answering

- User enters a question
- Convert question into embedding
- Retrieve relevant document chunks
- Build prompt with retrieved context
- Generate response using Qwen2.5
- Display answer in Streamlit

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/ehr-qa-agent.git
cd ehr-qa-agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download and install Ollama:

https://ollama.com/download

Pull the model:

```bash
ollama pull qwen2.5:3b
```

Start Ollama:

```bash
ollama serve
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💬 Example Questions

- What is the patient's diagnosis?
- What medications are prescribed?
- What is the patient's blood pressure?
- What are the patient's allergies?
- What laboratory results are available?
- Summarize this medical report.


---

## 👨‍💻 Author

Prince Jaiswal

GitHub: https://github.com/Princejaiswl
