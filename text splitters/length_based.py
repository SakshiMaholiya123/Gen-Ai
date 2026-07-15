from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader

loader=PyMuPDFLoader('D:\Gen-Ai\document loaders\RAG_Overview_2_3_Pages.pdf')

doc=loader.load()


# text="""Introduction
# Retrieval-Augmented Generation (RAG) is a technique that combines information retrieval with
# large language models (LLMs). Instead of relying only on the model's training data, RAG retrieves
# relevant information from external sources such as PDFs, websites, databases, and knowledge
# bases, then provides that information to the LLM before it generates an answer. This improves
# factual accuracy and allows AI systems to answer questions using private or up-to-date information.
# How RAG Works
# A typical RAG pipeline begins by loading documents using document loaders. The documents are
# split into smaller chunks using a text splitter. Each chunk is converted into a vector representation
# called an embedding and stored in a vector database. When a user asks a question, the query is
# also converted into an embedding. A retriever searches the vector database for the most similar
# chunks. These retrieved chunks are added to the prompt sent to the LLM, which then generates a
# context-aware response."""
splitter=CharacterTextSplitter(chunk_size=100,
                               chunk_overlap=0)

result=splitter.split_documents(doc)
print(result[0].page_content)


