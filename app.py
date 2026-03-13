# importing dependencies
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_groq import ChatGroq
from htmlTemplates import css, bot_template, user_template

# creating custom template to guide llm model
custom_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language.
Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""

CUSTOM_QUESTION_PROMPT = PromptTemplate.from_template(custom_template)

# extracting text from pdf
def get_pdf_text(docs):
    text=""
    for pdf in docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

# converting text to chunks
def get_chunks(raw_text):
    text_splitter=CharacterTextSplitter(separator="\n",
                                        chunk_size=1000,
                                        chunk_overlap=200,
                                        length_function=len)   
    chunks=text_splitter.split_text(raw_text)
    return chunks

# using all-MiniLm embeddings model and faiss to get vectorstore
def get_vectorstore(chunks):
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                     model_kwargs={'device':'cpu'})
    vectorstore=FAISS.from_texts(texts=chunks,embedding=embeddings)
    return vectorstore

# generating conversation chain  
def get_conversationchain(vectorstore):
    llm=ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.2)
    memory = ConversationBufferMemory(memory_key='chat_history', 
                                      return_messages=True,
                                      output_key='answer') # using conversation buffer memory to hold past information
    conversation_chain = ConversationalRetrievalChain.from_llm(
                                llm=llm,
                                retriever=vectorstore.as_retriever(),
                                condense_question_prompt=CUSTOM_QUESTION_PROMPT,
                                memory=memory)
    return conversation_chain

# generating response from user queries and displaying them accordingly
def handle_question(question):
    response=st.session_state.conversation({'question': question})
    st.session_state.chat_history=response["chat_history"]
    for i,msg in enumerate(st.session_state.chat_history):
        if i%2==0:
            st.write(user_template.replace("{{MSG}}",msg.content,),unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}",msg.content),unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="AskPDF - Intelligent Document Chat", page_icon=":books:", layout="wide")
    st.write(css, unsafe_allow_html=True)
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    # Sidebar layout
    with st.sidebar:
        st.title("📚 AskPDF")
        st.markdown("---")
        st.subheader("Your Documents")
        docs = st.file_uploader(
            "Upload PDFs and click 'Process'", 
            accept_multiple_files=True,
            help="You can upload multiple PDF files to chat with them simultaneously."
        )
        
        if st.button("Process Documents"):
            if not docs:
                st.warning("Please upload at least one PDF file.")
            else:
                with st.spinner("🚀 Processing your documents..."):
                    try:
                        # get the pdf
                        raw_text = get_pdf_text(docs)
                        # get the text chunks
                        text_chunks = get_chunks(raw_text)
                        # create vectorstore
                        vectorstore = get_vectorstore(text_chunks)
                        # create conversation chain
                        st.session_state.conversation = get_conversationchain(vectorstore)
                        st.success("Done! You can now ask questions.")
                    except Exception as e:
                        st.error(f"An error occurred: {e}")

    # Main area layout
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.title("Chat with Multiple PDFs 📚")
        st.markdown("##### *Extract insights and answers from your documents instantly.*")
        st.write("---")
        
        question = st.text_input("Ask a question about your documents:", placeholder="e.g., What is the main conclusion of the study?")
        
        if question:
            if st.session_state.conversation:
                handle_question(question)
            else:
                st.info("Please upload and process your documents first using the sidebar.")

        # Display chat history in a centered container if it exists
        if st.session_state.chat_history:
             # handle_question already writes to the main area, 
             # but we want to make sure the flow feels natural.
             pass

if __name__ == '__main__':
    main()
