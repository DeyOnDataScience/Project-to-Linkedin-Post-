# Project Title
LLM Post Generator for Notion

## Project Description
This project utilizes Large Language Models (LLMs) to generate LinkedIn-style posts based on either a user-provided query or an analysis of a given code repository. The generated posts can then be saved to a Notion database.

## Installation Steps
To install and run this project, follow these steps:
1. Clone the repository using `git clone`.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Set up your environment variables for Notion API keys and LLM models by creating a `.env` file with the following format:
   ```
   NOTION_API_KEY=YOUR_NOTION_API_KEY
   NOTION_DB_ID=YOUR_NOTION_DB_ID
   GEMINI_API_KEY=YOUR_GEMINI_API_KEY
   GROQ_API_KEY=YOUR_GROQ_API_KEY
   ```
4. Run the application using `streamlit run main.py`.

## Usage Examples
The project provides two main functionalities:
* **Query-Based Post Generation**: Users can input a topic or query, and the LLM will generate a post based on this input.
* **Code-Based Post Generation**: Users can provide a code repository path, and the LLM will analyze the code and generate a post summarizing the project.

To use these functionalities, navigate to the application's web interface and follow the prompts.

## Features
* Generates LinkedIn-style posts based on user input or code analysis
* Saves generated posts to a Notion database
* Utilizes Large Language Models for post generation
* Provides a user-friendly web interface for input and post generation

## Folder Structure
The project is organized into the following folders and files:
* `repo_clone.py`: Handles cloning of repositories for code analysis
* `post_generator.py`: Generates posts based on user input or code analysis
* `code_analysis.py`: Analyzes code repositories and provides summaries for post generation
* `credential.py`: Stores environment variables and initializes LLM models
* `save_to_notion.py`: Handles saving generated posts to a Notion database
* `main.py`: The main application file, providing a web interface for user input and post generation

## Contribution
Contributions to this project are welcome. To contribute, please fork the repository, make your changes, and submit a pull request. Ensure that your changes are properly documented and follow the project's coding standards.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

