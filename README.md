
# PDF Chatbot using Streamlit

A simple, interactive web application that lets you upload one or more PDF documents and chat with their contents in natural language. Powered by Streamlit, LangChain, and OpenAI (or any other supported LLM), your PDFs become conversational knowledge bases.

---

## Features

- **PDF Upload**  
  Upload single or multiple PDF files via an easy-to-use sidebar.

- **Document Parsing & Chunking**  
  Extracts text from PDFs, splits into manageable “chunks” for better context handling.

- **Vector Embeddings & Search**  
  Converts chunks into embeddings and stores them in a vector store (e.g. FAISS or Chroma) for fast semantic retrieval.

- **Chat Interface**  
  Ask questions in free form; the app finds the most relevant passages and generates informed answers.

- **Session State**  
  Maintains chat history within your browser session so you can carry on a back-and-forth conversation.

- **Customizable LLM**  
  Swap in any supported LLM: OpenAI’s GPT models, Anthropic’s Claude, local LLMs, etc.

---

## Tech Stack

- **Frontend & UI**: [Streamlit](https://streamlit.io/)  
- **PDF Processing**: [PyPDF2](https://pypi.org/project/PyPDF2/) or [`pypdf`](https://pypi.org/project/pypdf/)  
- **LangChain**: prompt templates, text splitting, LLM interface  
- **Embeddings & Vector Store**: FAISS, Chroma, or any LangChain-compatible vector store  
- **LLM Provider**: OpenAI (via `openai` SDK) by default  

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Rishi-Kora/PDF-Chatbot-using-streamlit.git
   cd PDF-Chatbot-using-streamlit


2. **Create & activate a virtual environment** (optional, but recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate     # Linux / macOS
   venv\Scripts\activate        # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install streamlit langchain openai pypdf faiss-cpu
   ```

4. **Set your OpenAI API key**

   ```bash
   export OPENAI_API_KEY="your_api_key_here"       # Linux / macOS
   set OPENAI_API_KEY="your_api_key_here"          # Windows
   ```

---

## Usage

1. **Run the app**

   ```bash
   streamlit run pdf_chatbot.py
   ```

2. **Upload PDFs**
   Click the “Browse files” button in the sidebar and select one or more PDFs.

3. **Start chatting**
   Type your question in the chat input at the bottom. The app displays your query and the LLM’s response in a chat-style format.

4. **Continue the conversation**
   Ask follow-up questions; session state preserves history.

---

## Code Overview

* **`pdf_chatbot.py`**

  * Imports and configures Streamlit, LangChain, and vector store
  * Defines helper functions:

    * `load_pdfs(files)`: Reads and concatenates text from uploaded PDFs
    * `split_into_chunks(text)`: Uses LangChain’s text splitter
    * `create_vector_store(chunks)`: Builds or loads FAISS/Chroma index
    * `ask_question(query)`: Retrieves relevant chunks and calls the LLM
  * Sets up Streamlit UI: sidebar for uploads, main chat window, custom CSS

* **`LICENSE`**
  MIT License — free to use and modify.

---

## 🗂 Project Structure

```
PDF-Chatbot-using-streamlit/
├── LICENSE
├── pdf_chatbot.py      # Main Streamlit application
└── README.md           # This file
```

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourIdea`)
3. Commit your changes (`git commit -m "Add some feature"`)
4. Push to your branch (`git push origin feature/YourIdea`)
5. Open a Pull Request — we’d love to see what you build!

---

## Contact

Feel free to open an issue or reach out to me at **[rishi.kora@example.com](mailto:rishi.kora@example.com)**.

---

## License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.
`
