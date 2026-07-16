from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

documents=[
    Document(page_content="LangChain is a framework..."),
    Document(page_content="ChromaDB is a vector database..."),
    Document(page_content="Retrievers fetch relevant documents...")
]

embedding=CohereEmbeddings()

vector_store=FAISS.from_documents(
    documents=documents,
    embedding=embedding,
)

retriever=vector_store.as_retriever(search_kwargs={'k':2,'lambda_nult':0.7})

query='what is langchain?'

res=retriever.invoke(query)

for i,doc in enumerate(documents):
    print('-----------------')
    print(doc.page_content)