# AskPDF - Intelligent Document Chat 📚

AskPDF is a state-of-the-art AI application that enables you to chat with multiple PDF documents simultaneously. Using advanced Retrieval-Augmented Generation (RAG), it extracts meaningful insights and answers from your files in seconds.

![AskPDF Interface](https://github.com/ankurraj2003/AskPDF/blob/main/demo.png?raw=true)

## 🚀 Features

- **Multi-Document Support:** Upload and process multiple PDFs at once.
- **Intelligent RAG:** Uses LangChain and OpenAI to provide context-aware answers.
- **Fast Search:** Leverages FAISS for lightning-fast similarity search over document chunks.
- **Conversational Memory:** Retains chat history for natural follow-up questions.
- **Premium UI:** A stunning, modern interface featuring:
    - **Glassmorphism:** Elegant semi-transparent blurred surfaces.
    - **Dynamic Glows:** Interactive glow effects and neon accents.
    - **Animations:** Smooth transitions and fade-in effects.

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **LLM Orchestration:** [LangChain](https://www.langchain.com/)
- **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
- **Vector Database:** [FAISS](https://github.com/facebookresearch/faiss)
- **Language Model:** OpenAI GPT
- **Environment:** Python (.env support)

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/AskPDF.git
   cd AskPDF
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API Key:**
   Create a `.env` file in the root directory and add your OpenAI API Key:
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 🎨 UI Aesthetics
The application features a custom CSS-driven design that prioritizes aesthetics and user experience. With its dark-mode radial gradients and glassmorphism sidebar, it feels more like a premium SaaS product than a standard data tool.
