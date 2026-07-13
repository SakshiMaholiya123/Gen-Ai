from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,List
from pydantic import BaseModel,Field

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

#Schema
class Review(BaseModel):
    summary:str=Field(description="A brief summary about the review")
    sentiment:str
    pros:Optional[List[str]]=Field(default=None,description="list the pros")
    cons:Optional[List[str]]=Field(default=None,description="list the cons")


structured_model=model.with_structured_output(Review)

res=structured_model.invoke("The laptop is working fine for learning and coding. It handles basic tasks well, but it becomes slow when running heavy applications like local AI models or PySpark. Overall, it is good for regular development and cloud-based AI work")

print(res)