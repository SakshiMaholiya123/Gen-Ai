from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings=CohereEmbeddings(model="embed-multilingual-v3.0")

vector=embeddings.embed_query("you are going to learn gen ai")

print(vector)