from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


template1=PromptTemplate(template="write a detailed report on {topic}",
                         input_variables=['topic'])

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. \n {text}',
    input_variables=['text']
)


parser=StrOutputParser()

chain=template1|model|parser|template2|model|parser

res=chain.invoke({"topic":"black hole"})

print(res)
# prompt1 = template1.invoke({'topic':'black hole'})

# result = model.invoke(prompt1)

# prompt2 = template2.invoke({'text':result.content})

# result1 = model.invoke(prompt2)

# print(result1.content)