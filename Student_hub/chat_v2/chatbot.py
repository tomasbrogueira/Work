import os
from openai import OpenAI

from llama_index import (
    GPTVectorStoreIndex,
    ServiceContext,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
    )

from llama_index.prompts.base import ChatPromptTemplate
from llama_index.llms.base import ChatMessage, MessageRole
from llama_index.llms import OpenAI


os.environ["OPENAI_API_KEY"] = 'sk-...'

OpenAI.api_key = os.environ["OPENAI_API_KEY"]

import nest_asyncio

nest_asyncio.apply()








"""
llm_index = GPTVectorStoreIndex.from_documents(
    documents,
    service_context=ServiceContext.from_defaults(
        model_id="gpt4",
        index_name="llama_index",
        similarity_function="dot_product",
        similarity_top_k=4,
    ),
)
"""


documents = SimpleDirectoryReader(input_dir="./data/").load_data()



# initialize simple vector indices


service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt4", temperature=0.05))


"""
index_set = {}
for doc in documents:
    storage_context = StorageContext.from_defaults()
    curr_index = GPTVectorStoreIndex.from_documents(documents=[doc],
                                                service_context=service_context,
                                                storage_context=storage_context)
    "doc.id"
    index_set[doc] = curr_index

    #storage_context.persist(persist_dir="./data/")

"""

index = GPTVectorStoreIndex.from_documents(documents=documents, service_context=service_context)


"""
query_engine = load_index_from_storage(storage_context).as_query_engine(similarity_top_k=4)
response = query_engine.query(input_text)
"""




TEXT_QA_SYSTEM_PROMPT = ChatMessage(
    content=(
        "You are an expert Q&A system that is trusted around the world.\n"
        "Always answer the query using the provided context information, "
        "and not prior knowledge.\n"
        "Some rules to follow:\n"
        "1. Never directly reference the given context in your answer.\n"
        "2. Avoid statements like 'Based on the context, ...' or "
        "'The context information ...' or anything along "
        "those lines."
    ),
    role=MessageRole.SYSTEM,
)

TEXT_QA_PROMPT_TMPL_MSGS = [
    TEXT_QA_SYSTEM_PROMPT,
    ChatMessage(
        content=(
            "Context information is below.\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "Given the context information and not prior knowledge, "
            "answer the query.\n"
            "Query: {query_str}\n"
            "Answer: "
        ),
        role=MessageRole.USER,
    ),
]

CHAT_TEXT_QA_PROMPT = ChatPromptTemplate(message_templates=TEXT_QA_PROMPT_TMPL_MSGS)


print(
    index.as_query_engine(
        text_qa_template=CHAT_TEXT_QA_PROMPT
    ).query("What is StudentHub?")
)