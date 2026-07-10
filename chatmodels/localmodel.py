from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

llm=HuggingFacePipeline.from_model_id(model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",task="text-generation")

chat_model=ChatHuggingFace(llm=llm)

res=chat_model.invoke("what is data science?")

print(res.content)