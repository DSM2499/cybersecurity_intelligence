from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def get_llama3_client():
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found. Please check your .env file.")
    
    llm = ChatGroq(
        model_name = "llama3-70b-8192",
        temperature = 0.0,
        api_key = groq_api_key,
    )
    
    print("✅ Groq Llama 3 client initialized.")
    return llm