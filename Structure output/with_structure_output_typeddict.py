from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,List

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

#Schema
class Review(TypedDict):
    summary:Annotated[str,"A brief summary about the review"]
    sentiment:str
    pros:Annotated[Optional[List[str]],"list the pros"]
    cons:Annotated[Optional[List[str]],"list the cons"]

structured_model=model.with_structured_output(Review)

res=structured_model.invoke("The laptop is working fine for learning and coding. It handles basic tasks well, but it becomes slow when running heavy applications like local AI models or PySpark. Overall, it is good for regular development and cloud-based AI work")

print(res)