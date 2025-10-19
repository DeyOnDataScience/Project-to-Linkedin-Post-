import requests
from credential import NOTION_DB_ID, NOTION_HEADERS
from datetime import datetime

date = datetime.now().isoformat()
def save_to_notion(content: str, topic: str, status: str = "Draft"):
	# Step 1: Create the page in the database
	create_url = "https://api.notion.com/v1/pages"
	data = {
		"parent": {"database_id": NOTION_DB_ID},
		"properties": {
			"Title": {"title": [{"text": {"content": topic[:50]}}]},
			"Status": {"status": {"name": status}},
			"Upload Date":{"date": {"start": date}}
		}
	}
	res = requests.post(create_url, headers=NOTION_HEADERS, json=data)
	page = res.json()
	page_id = page.get("id")

    # Step 2: Add block inside the page (when we click open it shows up in a paragraph of a new page)

	if page_id:
		block_url = f"https://api.notion.com/v1/blocks/{page_id}/children"
		block_data = {
			"children": [
				{
					"object": "block",
					"type": "paragraph",
					"paragraph": {
						"rich_text": [
							{"type": "text", "text": {"content": content}}
						]
					}
				}
			]
		}
		res2 = requests.patch(block_url, headers=NOTION_HEADERS, json=block_data)
		return res2.json()

	return page