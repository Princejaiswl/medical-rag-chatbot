from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate




def ask_question(vector_store, user_input):
    results = vector_store.similarity_search(query=user_input, k=3)
    for doc in results:
        print(f"* {doc.page_content} [{doc.metadata}]")

    context="\n\n".join([doc.page_content for doc in results])
    # print("Context:",context)


    template = ChatPromptTemplate(
        [
            ("system", "You are a helpful medical AI bot. Answer ONLY using the provided context.If the answer is not present in the context, say: I don't know."),
            ("human", "context:{context} \n question:{user_input}"),
        ]
    )

    prompt_value = template.invoke(
        {
            "context": context,
            "user_input":  user_input,
        }
    )
    print("Prompt Value:", prompt_value)

    llm = ChatOllama(
        model="qwen2.5:3b",
        temperature=0)
    response = llm.invoke(prompt_value)
    # print("Response:", response.content)
    return response.content
