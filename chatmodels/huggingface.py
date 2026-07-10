from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

llm=HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V4-Flash",task="text-generation")

model=ChatHuggingFace(llm=llm)

response=model.invoke("who are you?")

print(response.content)