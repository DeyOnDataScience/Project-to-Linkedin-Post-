import os
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load secrets
load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DB_ID = os.getenv("NOTION_DB_ID")


os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Initialize LLMs
try:
	llm = ChatGroq(model="deepseek-r1-distill-llama-70b")
	llm1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
	client = ChatGroq(model="openai/gpt-oss-120b",
				  temperature=0.7,
				  max_tokens=500)

except Exception as e:
	raise RuntimeError(f"Failed to initialize LLMs: {e}")
# Defining Notion Headers
NOTION_HEADERS = {
	"Authorization": f"Bearer {NOTION_API_KEY}",
	"Content-Type": "application/json",
	"Notion-Version": "2022-06-28"
}
