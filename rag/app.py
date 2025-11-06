## Data Ingestion
from langchain_community.document_loaders import TextLoader
loader= TextLoader("speech.txt")
text_documents= loader.load()
# print(text_documents)

import os 
from dotenv import load_dotenv
load_dotenv()
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../chatbot', '.env'))

os.environ["OLLAMA_API_KEY"]= os.getenv("OLLAMA_API_KEY")
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY") 