from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from uuid import uuid4

def ingest_documents(splits):
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vector_store = Chroma(
        collection_name="ehr_data",
        embedding_function=embeddings,
        persist_directory="./chroma_langchain_db",

    )

    uuids = [str(uuid4()) for _ in range(len(splits))]

    vector_store.add_documents(documents=splits, ids=uuids)
    # print("Documents added to the vector store successfully.")
    # print(vector_store)
    # print(vector_store._collection.count())
    return vector_store

