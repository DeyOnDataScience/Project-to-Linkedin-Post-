from code_analysis import full_work
from langchain.schema import HumanMessage
from credential import client


def code_based_generate_post(code_path:str,tone: str = "professional") -> str:
    # Import the generated variable from previous module
	analysis_content = full_work(code_path)

	prompt = f"""
You are a professional content creator and technical storyteller specializing in LinkedIn posts.

Using the analysis below, write an engaging and insightful LinkedIn post that summarizes the project.
- Keep tone: {tone}
- Limit: 1300 characters
- Be clear, inspiring, and technical where appropriate

Analysis:
{analysis_content}
"""
	messages = [HumanMessage(content=prompt)]
	response = client.invoke(messages)

	return response.content.strip()

def query_based_generate_post(query:str,tone: str = "professional") -> str:

# Generate a LinkedIn post from a simple user given query.
	prompt = f"""
You are a professional content creator and technical storyteller specializing in LinkedIn posts.

Using the analysis below, write an engaging and insightful LinkedIn post that summarizes the project.
- Keep tone: {tone}
- Limit: 1500 characters
- Be clear, inspiring, and technical where appropriate

Analysis:
{query}
"""
	messages = [HumanMessage(content=prompt)]
	response = client.invoke(messages)

	return response.content.strip()

