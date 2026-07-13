from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


class Person(BaseModel):
    name:str=Field(description='name of the person')
    age:int =Field(gt=18,description='age of the person')
    city:str=Field(description='name of the city')


parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="give the name and city of {place} person \n{format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt=template.invoke({'place':'british'})

res=model.invoke(prompt)

print(res)