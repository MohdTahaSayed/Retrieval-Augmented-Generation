
from langchain.chains import RetrievalQA

def create_qa_chain(llm, vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )
    return qa_chain

query = "[ Your Query ]"
result = qa_chain.invoke({"query": query})

print("🧠 Answer:\n", result['result'])
print("\n📚 Sources:")
for doc in result['source_documents']:
    print("-", doc.metadata['source'])

