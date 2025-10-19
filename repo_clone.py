import subprocess
from pathlib import Path
import shutil
# Cloning from repo url and saving in a temporary file
def download_repo1(repo_url: str) -> str:
	dest_dir = "temp"
	subprocess.run(["git", "clone", repo_url, dest_dir], check=True)
	return str(Path(dest_dir).resolve())
# Deleting the made temporary file
def del_repo(path_repo: str):
	try:
		shutil.rmtree(path_repo)
		print("Temporary File Deleted")
	except Exception as e:
		print(f"Error found while cleaning up..{e}")
 