from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import tiktoken
from ConversationBufferMemory import ConversationBufferMemory


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

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
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(model='gpt-4', temperature=0.1)
    memory = ConversationBufferMemory(
        memory_key='conversation_memory.json', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_user_input(user_input, conversation_chain, memory):
    if user_input == "quit":
        conversation_chain.stop()
        return

    memory.remember(user_input)  # Remember the user input
    response = conversation_chain(user_input)
    print(response.text)



def main():
    load_dotenv()
    pdf_docs = ["./data/1.pdf", "./data/2.pdf", "./data/3.pdf"]
    
    text = get_pdf_text(pdf_docs)
    text_chunks = get_text_chunks(text)
    
    vectorstore = get_vectorstore(text_chunks)
    
    user_conversation_chains = {}  # Dictionary to store conversation chains for different users
    
    while True:
        user_id = input("Enter user ID: ")  # Unique identifier for each user
        
        if user_id not in user_conversation_chains:
            # If the user doesn't have a conversation chain yet, create a new one
            user_conversation_chains[user_id] = get_conversation_chain(vectorstore)
            user_conversation_chains[user_id].start()
        
        memory = ConversationBufferMemory(memory_key=f'conversation_memory_{user_id}.json', return_messages=True)
        
        while True:
            user_input = input(">>> ")
            handle_user_input(user_input, user_conversation_chains[user_id], memory)
            if user_input == "quit":
                break
        
        if user_input == "quit":
            del user_conversation_chains[user_id]  # Remove the conversation chain when user quits
            break

if __name__ == "__main__":
    main()
