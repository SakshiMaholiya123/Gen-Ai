from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,List
from pydantic import BaseModel,Field

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

#Schema
json_schema={
  "title": "Review",
  "type": "object",
  "properties": {
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
  },
  "required": [ "summary","sentiment"]
}

structured_model=model.with_structured_output(json_schema)

res=structured_model.invoke("The laptop is working fine for learning and coding. It handles basic tasks well, but it becomes slow when running heavy applications like local AI models or PySpark. Overall, it is good for regular development and cloud-based AI work")

print(res)