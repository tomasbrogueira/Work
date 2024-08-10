from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import tiktoken
import os

env_path = './venv/.env'

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

num_tokens_from_string("tiktoken is great!", "cl100k_base")





def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text





def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks



def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    
    "for local embeding use huggingface instructor-xl"
    #embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore



def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(model='gpt-4', temperature=0.1)
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain





def handle_user_input(user_input, conversation_chain):
    "Might be a problem remembering the new input"
    if user_input == "quit":
        conversation_chain.stop()
        return
    response = conversation_chain(user_input)
    print(response.text)







def main():
    load_dotenv(dotenv_path=env_path)

    pdf_docs = ["./data/1.pdf", "./data/2.pdf", "./data/3.pdf"]
    
    text = get_pdf_text(pdf_docs)
    text_chunks = get_text_chunks(text)
    
    
    vectorstore = get_vectorstore(text_chunks)
    
    
    
    conversation_chain = get_conversation_chain(vectorstore)
    conversation_chain.start()
    
    
    while True:
        user_input = input(">>> ")
        handle_user_input(user_input, conversation_chain)
        if user_input == "quit":
            break







if __name__ == "__main__":
    main()