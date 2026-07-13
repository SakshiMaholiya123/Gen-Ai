from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


parser=JsonOutputParser()

template=PromptTemplate(
    template="give me the name,age and city of a fictional person \n {format_instructions}",
    input_variables=[],
    partial_variables={'format_information':parser.get_format_instructions()}
)
chain=template | model | parser
res=chain.invoke({})
print(res)