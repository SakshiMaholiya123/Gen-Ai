from langchain_community.document_loaders import TextLoader
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatMistralAI(model='mistral-small-latest')

prompt=PromptTemplate(
    template='give the five main points from the {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

loader=TextLoader('D:\Gen-Ai\document loaders\data.txt',encoding='utf-8')

doc=loader.load()

print(doc)

chain=prompt | model | parser

print(chain.invoke({'topic':doc[0].page_content}))