from langchain_community.retrievers import WikipediaRetriever

retriever=WikipediaRetriever(top_k_results=2)

query='geopolitical history of india and pakistan is perspective of china'

docs=retriever.invoke(query)

for i,doc in enumerate(docs):
    print(f"{doc.page_content}")
    print('-----------------')