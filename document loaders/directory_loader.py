from langchain_community.document_loaders import DirectoryLoader

loader=DirectoryLoader(path='D:\Gen-Ai\document loaders\documents',
                       glob='*.pdf')

doc=loader.load()

print(doc)