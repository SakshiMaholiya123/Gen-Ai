from langchain_community import Chroma
from langchain_cohere import CohereEmbeddings
from langchain_core.documents import Document

documents=[
    Document(page_content="LangChain is a framework..."),
    Document(page_content="ChromaDB is a vector database..."),
    Document(page_content="Retrievers fetch relevant documents...")
]


embedding=CohereEmbeddings()

vector_store=Chroma.from_documents(
    documents=documents,
    embedding=embedding,
    collection_name='my_collection'

)

retriever=vector_store.as_retriever(search_kwargs={'k':2})

query='what is the use of chroma db?'

res=retriever.invoke(query)

for i,doc in enumerate(documents):
    print('-----------------')
    print(doc.page_content)