from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langserve import add_routes
import uvicorn
import os 
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../chatbot', '.env'))

os.environ["OLLAMA_API_KEY"]= os.getenv("OLLAMA_API_KEY")
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY") 

app= FastAPI(
    title= "LangChain Server",
    version= "1.0.0",
    description= "API server for LangChain applications using Ollama model"
)


llm= Ollama(model="gpt-oss:120b-cloud", temperature=0)

prompt1= ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")
prompt2= ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words.")

add_routes(
    app,
    prompt1 | llm,
    path= "/ollama-essay"
)

add_routes(
    app,
    prompt2 | llm,
    path= "/ollama-poem"
)

if __name__== "__main__":
    uvicorn.run(app, host="localhost", port=8000)