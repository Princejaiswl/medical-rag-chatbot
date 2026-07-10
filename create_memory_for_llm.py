from urllib import response
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_chroma import Chroma
from uuid import uuid4
from langchain_core.documents import Document
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate



# data_path = "./data"

def create_doc(data_path):
    loader = DirectoryLoader(path=data_path, glob="**.pdf", loader_cls=PyPDFLoader)
    documents=loader.load()

    print(type(documents)) 
    print(len(documents))
    # print(type(documents[0]))
    # print(documents[0])
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
    )
    splits = text_splitter.split_documents(documents)
    # print(len(splits))
    # print(splits[0])
    return splits



