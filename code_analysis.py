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



