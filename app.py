import streamlit as st
from create_memory_for_llm import create_doc
from ehr_ingest import ingest_documents
from ehr_rag_pipeline import ask_question


@st.cache_resource
def load_data():
    splits = create_doc(data_path="C:\\Users\\Princuu\\Desktop\\Rag\\data")
    vector_store = ingest_documents(splits)    #context 
    return vector_store
vector_store = load_data()
st.title("Medical report AI Chatbot")
st.write("This is a patient medical report AI chatbot that can answer questions based on the present reports.")



user_input = st.chat_input("Enter your question:")


if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    response = ask_question(vector_store, user_input)
    with st.chat_message("assistant"):
        st.write(response)






# response = ask_question(vector_store, user_input)
# print(response)    