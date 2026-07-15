from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('D:\Gen-Ai\document loaders\RAG_Overview_2_3_Pages.pdf')

doc=loader.load()

print(doc)