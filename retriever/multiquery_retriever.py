from langchain_community.vectorstores import Chroma
from langchain_cohere import CohereEmbeddings
from langchain_core.documents import Document
from langchain_mistralai import ChatMistralAI
from langchain.retrievers.multi_query import MultiQueryRetriever


documents=[
    Document(page_content="LangChain is a framework..."),
    Document(page_content="ChromaDB is a vector database..."),
    Document(page_content="Retrievers fetch relevant documents..."),
    Document(page_content="Pinecone is a managed cloud vector database designed for production AI applications."),
    Document(page_content="Retrieval-Augmented Generation (RAG) combines information retrieval with LLMs to generate accurate answers."),
    Document(page_content="Text splitters divide large documents into smaller chunks before generating embeddings."),
    Document(page_content="Prompt engineering is the practice of designing effective prompts to improve LLM responses."),
    Document(page_content="Transformers use the self-attention mechanism to understand relationships between words in a sequence."),
    Document(page_content="Sentence Transformers generate high-quality sentence embeddings for semantic search."),
    Document(page_content="Hugging Face provides pre-trained transformer models for NLP and generative AI tasks."),
    Document(page_content="OpenAI's text-embedding-3-small model is widely used for semantic search and RAG systems."),
    Document(page_content="Max Marginal Relevance (MMR) retrieves documents that are both relevant and diverse."),
    Document(page_content="A MultiQuery Retriever generates multiple variations of a user's question using an LLM."),
    Document(page_content="Vector databases store embeddings and perform similarity searches using distance metrics."),
    Document(page_content="Cosine similarity measures the angle between two embedding vectors to determine semantic similarity."),
    Document(page_content="Metadata such as source, author, and page number can be stored alongside document embeddings.")
]


embedding=CohereEmbeddings()

vector_store=Chroma.from_documents(
    documents=documents,
    embedding=embedding,
    collection_name='collection'

)

retriever=vector_store.as_retriever(search_kwargs={'k':2})

multi_query_retriver=MultiQueryRetreiever.from_llm (
    vector_store.as_retriever({'search_kwargs':2},
                              llm=ChatMistralAI(model='mistral-small-latest'))
)

query='How can I improve retrieval in my RAG application?'

res=retriever.invoke(query)
result=multi_query_retriver.invoke(query)

for i,doc in enumerate(res):
    print('-----------------')
    print(doc.page_content)

print('======================')


for i,doc in enumerate(multi_query_retriver):
    print('-----------------')
    print(doc.page_content)
