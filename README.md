# LinkedIn Post Generator
## Project Description
The LinkedIn Post Generator is a Python-based project that utilizes Large Language Models (LLMs) to generate engaging and insightful LinkedIn posts. The project consists of multiple modules, including code analysis, post generation, and Notion integration.

## Installation Steps
To install the project, follow these steps:
1. Clone the repository using `git clone`.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up your environment variables by creating a `.env` file with the following keys:
	* `NOTION_API_KEY`
	* `NOTION_DB_ID`
	* `GOOGLE_API_KEY`
	* `GROQ_API_KEY`
4. Load the environment variables using `load_dotenv()`.

## Usage Examples
The project provides two main functionalities:
### Code-Based Post Generation
1. Enter the path of the code repository you want to analyze.
2. Click the "Click to Analyze for a Post" button to generate a LinkedIn post based on the code analysis.
3. The generated post will be displayed, and you can save it to your Notion database by clicking the "Save to Notion" button.

### Query-Based Post Generation
1. Enter a topic or query you want to generate a post about.
2. Click the "Generate Content" button to generate a LinkedIn post based on the query.
3. The generated post will be displayed, and you can save it to your Notion database by clicking the "Save to Notion" button.

## Features
* Code analysis using LLMs to generate insightful posts
* Query-based post generation for topics or queries
* Notion integration to save generated posts to your database
* Streamlit-based interface for easy usage

## Folder Structure
The project consists of the following folders and files:
* `repo_clone.py`: Module for cloning repositories and deleting temporary files.
* `post_generator.py`: Module for generating LinkedIn posts based on code analysis or queries.
* `code_analysis.py`: Module for analyzing code and generating summaries.
* `credential.py`: Module for loading environment variables and initializing LLMs.
* `save_to_notion.py`: Module for saving generated posts to Notion database.
* `main.py`: Main module for running the Streamlit application.

## Contribution
Contributions to the project are welcome. To contribute, please fork the repository, make your changes, and submit a pull request.

## Acknowledgments
The project utilizes the following libraries and frameworks:
* `langchain` for LLM integration
* `streamlit` for building the user interface
* `notion` for integrating with the Notion API and Database
* `langchain-google-genai` for integrating with the Google API
* `groq` for integrating with the Groq API
