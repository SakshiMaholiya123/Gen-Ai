from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


schema=[
    ResponseSchema(name='fact_1',description='fact 1 about the topic'),
    ResponseSchema(name='fact_1',description='fact 1 about the topic'),
    ResponseSchema(name='fact_1',description='fact 1 about the topic')
]

parser=StructuredOutputParser.from_response_schema(schema)

template=PromptTemplate(
    template="GIVE 2 FACTS ABOUT{topic}\n{format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain=template | model | parser

res=chain.invoke({'topic':'black hole'})

print(res)