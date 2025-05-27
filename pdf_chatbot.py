import os
import streamlit as st
import pdfplumber
import json
from datetime import datetime
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Load OpenAI API key
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="📄 Ask Questions from PDF", layout="wide")
st.title("📚 PDF Q&A with Vector Embeddings")

# Init chat log
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# Upload PDF
uploaded_file = st.file_uploader("📤 Upload a PDF", type=["pdf"], key="qa_pdf")

if uploaded_file:
    os.makedirs("uploaded_pdfs", exist_ok=True)
    pdf_path = os.path.join("uploaded_pdfs", uploaded_file.name)

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"✅ Uploaded: {uploaded_file.name}")

    # Extract text
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([page.extract_text() or "" for page in pdf.pages])

    if not text.strip():
        st.warning("⚠️ No extractable text in this PDF.")
        st.stop()

    # Split text into chunks
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.create_documents([text])
    st.info(f"📑 Text split into {len(docs)} chunks.")

    # Create embeddings and save
    embedder = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(docs, embedder)
    db_name = os.path.splitext(uploaded_file.name)[0]
    vectordb_dir = f"vector_db/{db_name}"
    vectordb.save_local(vectordb_dir)
    st.success("✅ Embeddings created and stored.")

    # Ask question
    st.header("💬 Ask Questions from This PDF")
    query = st.text_input("Ask a question...")

    if query:
        vectordb = FAISS.load_local(vectordb_dir, embedder, allow_dangerous_deserialization=True)
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())

        with st.spinner("🤖 Thinking..."):
            response = qa_chain.run(query)

        # Save interaction in session state
        st.session_state.chat_log.append({"question": query, "answer": response})

        # Save to file
        os.makedirs("chat_logs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_path = f"chat_logs/chat_{db_name}_{timestamp}.json"
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(st.session_state.chat_log, f, indent=2, ensure_ascii=False)

        st.success("✅ Chat history saved locally.")
        st.write("🤖", response)




