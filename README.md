
# 🧠 Med-Surg RAG Assistant

This is a **Retrieval-Augmented Generation (RAG)** application built with **Streamlit**, designed to help users interactively query and explore content from a **medical-surgical nursing textbook**. The app combines the power of **large language models (LLMs)** with a structured vector-based knowledge base for accurate and context-rich answers.

---

## 🚀 Features

- 📚 **Domain-specific Knowledge Base**: Indexed med-surg textbook content for reliable medical-nursing context.
- 🧠 **Retrieval-Augmented Generation**: Combines LLMs with Pinecone vector search to retrieve and reason over relevant context.
- 💬 **Chat Interface**: Easy-to-use Streamlit frontend for querying the knowledge base.
- ⚡ **Groq + Langchain**: Uses `langchain` integrations with `ChatGroq` for fast and scalable LLM querying.

---

## 🏗️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Vector Store**: [Pinecone](https://www.pinecone.io/)
- **LLM Integration**: [Langchain](https://www.langchain.com/) + [Groq](https://groq.com/)
- **Embeddings**: [HuggingFaceEmbeddings](https://huggingface.co/) (`sentence-transformers`)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/medsurg-rag-assistant.git
cd medsurg-rag-assistant
```

### 2. Set up your environment

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file or set the following variables in your environment:

```env
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_env
GROQ_API_KEY=your_groq_api_key
```

You can use [`python-dotenv`](https://pypi.org/project/python-dotenv/) to load `.env` files automatically if needed.

---

## 🧪 Running the App

```bash
streamlit run app.py
```

Replace `app.py` with your actual script filename.

---

## 📖 How It Works

1. **User Input**: The user submits a query.
2. **Vector Search**: Relevant textbook chunks are retrieved from Pinecone using HuggingFace embeddings.
3. **Prompt Construction**: Retrieved docs are passed to a prompt template.
4. **LLM Response**: The prompt is sent to a Groq-powered LLM for a final answer.
5. **Display**: Answer is rendered in the Streamlit interface.

---

## 📚 Use Case

- Useful for **nursing students**, **educators**, and **medical professionals** who need precise answers sourced directly from a trusted med-surg textbook.
- Great for studying, teaching, or supplementing clinical knowledge.

---

## 🛠️ To-Do / Future Enhancements

- Add user authentication (e.g., Streamlit login or Firebase)
- Support PDF ingestion and dynamic chunking
- Save and export chat history
- Switch between different knowledge bases (e.g., pharmacology, pathophysiology)

---

## 📜 License

MIT License

---

## 🙌 Acknowledgments

- Streamlit Team
- Pinecone
- Hugging Face
- Langchain
- Groq LLM

---

Let me know if you'd like it tailored further (e.g., with screenshots, deployment instructions, or citation format).
