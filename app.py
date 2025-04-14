import os
import streamlit as st
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
# from langchain_huggingface import HuggingFaceEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings

# Force CPU to avoid meta tensor errors
os.environ["CUDA_VISIBLE_DEVICES"] = ""

st.title("Med-surge Chat-bot")

# API Keys
pinecone_api_key = st.secrets["PINECONE_API_KEY"]
groq_api_key = st.secrets["GROQ_API_KEY"]

# Default session states
st.session_state.setdefault("model_name1", "sentence-transformers/all-MiniLM-L6-v2")
st.session_state.setdefault("model_name", "llama-3.3-70b-versatile")
st.session_state.setdefault("messages", [])

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
prompt_input = st.chat_input("Ask your question?")
if prompt_input:
    st.session_state.messages.append({"role": "user", "content": prompt_input})
    with st.chat_message("user"):
        st.markdown(prompt_input)

# Initialize Pinecone
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index("med-surge")

# Create embeddings (use CPU)
embeddings = HuggingFaceEmbeddings(
    model_name=st.session_state["model_name1"]
)

# Vector store and retriever
vector_store = PineconeVectorStore(index=index, embedding=embeddings)
retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 1, "score_threshold": 0.5}
)

# Prompt template
prompt_template = ChatPromptTemplate.from_template(
    """
    You are a Medical AI assistant with access to a specific knowledge base. Your task is to answer user questions **only** based on the provided context.

    <context>
    {context}
    </context>

    If the answer is **not found** in the context, respond with:
    *"I don't know the answer to that based on my available knowledge."*

    Otherwise, extract the most relevant details, **summarize**, and present a clear, concise response.

    ### Question:
    {input}

    ### Answer:
    """
)

# Chat model & RAG setup
model = ChatGroq(groq_api_key=groq_api_key, model_name=st.session_state["model_name"])
document_chain = create_stuff_documents_chain(model, prompt_template)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Only invoke chain if user sent input
if prompt_input:
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = retrieval_chain.invoke({"input": prompt_input})
            ai_response = response["answer"]
            st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
