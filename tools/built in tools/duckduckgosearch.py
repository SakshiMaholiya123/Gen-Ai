from langchain_community.tools import DuckDuckGoSearchResults

search_tool=DuckDuckGoSearchResults()

result=search_tool.invoke('ipl news')
print(result)