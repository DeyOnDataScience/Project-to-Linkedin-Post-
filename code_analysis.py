from credential import llm,llm1
import json
import re
from pathlib import Path
from typing import TypedDict, Dict, Any, List
from langchain.schema import HumanMessage
from langgraph.graph import StateGraph, END
from repo_clone import download_repo1,del_repo


class AgentState(TypedDict):
	folder_path: str
	files: List[Dict[str, str]]
	analysis: Dict[str, Any]
	content: Dict[str, Any]



def file_loader(state: AgentState) -> AgentState:
	folder_path = state.get("folder_path")
	base = Path(folder_path)
	files_data = []

	print(f"\nLoader] Scanning folder: {folder_path}")

	if not base.exists():
		raise FileNotFoundError(f"Folder not found: {folder_path}")

	for file in base.rglob("*.py"):
		try:
			content = file.read_text(encoding="utf-8")
			files_data.append({
				"name": str(file.relative_to(base)),
				"content": content
			})
		except Exception as fe:
			print(f"Skipped {file}: {fe}")

	print(f"Loaded {len(files_data)} Python files.")
	return {**state, "files": files_data}



def analyzer_agent(state: AgentState) -> AgentState:
	files = state.get("files", [])
	print(f"\n[Analyzer] Analyzing {len(files)} files...")

	if not files:
		return {**state, "analysis": {"summary": "No Python files found."}}

	combined_text = "\n\n".join(
		[f"# File: {f['name']}\n{f['content'][:2000]}" for f in files]
	)

	prompt = f"""
You are a code analyst. Analyze the following Python files and produce a JSON summary:
- File purpose
- Functions & classes
- Logic flow & dependencies
- Key insights

Files:
{combined_text[:6000]}

Respond in JSON:
{{
  "summary": "...",
  "important_points": ["..."],
  "suggested_actions": ["..."]
}}
"""

	try:
		response = llm.invoke([HumanMessage(content=prompt)])
		content = response.content
		match = re.search(r'\{.*\}', content, flags=re.S)
		data = json.loads(match.group(0)) if match else {"summary": content}
	except Exception as e:
		data = {"summary": "Analysis failed", "error": str(e)}

	return {**state, "analysis": data}



def content_agent(state: AgentState) -> AgentState:
	analysis = state.get("analysis")
	folder_path = state.get("folder_path")

	print(f"\n[ContentAgent] Generating content for: {folder_path}")

	prompt = f"""
You are a senior technical writer.
Using the following analysis, create well-structured project documentation.

Analysis:
{json.dumps(analysis, indent=2)}

Respond strictly in JSON:
{{
  "title": "A concise title",
  "body": "Detailed markdown-style documentation",
  "tags": ["Relevant", "Topics"]
}}
"""

	try:
		response = llm1.invoke([HumanMessage(content=prompt)])
		content = response.content
		match = re.search(r'\{.*\}', content, flags=re.S)
		data = json.loads(match.group(0)) if match else {"raw": content}
	except Exception as e:
		data = {"error": str(e)}

	return {**state, "content": data}



def supervisor_printer(state: AgentState) -> AgentState:
	print("\n[Workflow Completed]")
	return state



workflow = StateGraph(AgentState)
workflow.add_node("loader", file_loader)
workflow.add_node("analyzer", analyzer_agent)
workflow.add_node("content", content_agent)
workflow.add_node("printer", supervisor_printer)
workflow.add_edge("loader", "analyzer")
workflow.add_edge("analyzer", "content")
workflow.add_edge("content", "printer")
workflow.add_edge("printer", END)
workflow.set_entry_point("loader")
app = workflow.compile()


