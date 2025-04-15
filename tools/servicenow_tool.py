from langchain.tools import Tool
import requests
from config import SERVICENOW_INSTANCE, SERVICENOW_USERNAME, SERVICENOW_PASSWORD, SERVICENOW_TABLE

SERVICENOW_INSTANCE = "https://dev281366.service-now.com"
SERVICENOW_USERNAME = "sitha"
SERVICENOW_PASSWORD = "PASSWORD"
SERVICENOW_TABLE = "change_request"

OPENAI_API_BASE = "https://api.openai.com/v1"
OPENAI_API_KEY = "OPENAPI_OPEN_KEY"
OPENAI_API_VERSION = "2023-05-15"
OPENAI_API_MODEL = "gpt-3.5-turbo"
OPENAI_API_TIMEOUT = 60
OPENAI_API_PROXY = None  # Set this to your proxy if needed
# Optional: Uncomment and set the following variables if you want to use a proxy
# PROXY_HOST = "your_proxy_host"


def create_change_request(input: str) -> str:
    lines = input.split("\n")
    short_desc = lines[0]
    description = "\n".join(lines[1:]) or "Change request created via LangChain MCP agent."

    payload = {
        "short_description": short_desc,
        "description": description,
        "category": "Software",
        "priority": "2"
    }

    response = requests.post(
        f"{SERVICENOW_INSTANCE}/api/now/table/{SERVICENOW_TABLE}",
        json=payload,
        auth=(SERVICENOW_USERNAME, SERVICENOW_PASSWORD),
        headers={"Content-Type": "application/json", "Accept": "application/json"}
    )

    if response.status_code == 201:
        return f"Change Request Created: {response.json()['result']['number']}"
    else:
        return f"Error: {response.text}"

servicenow_tool = Tool(
    name="create_servicenow_change",
    func=create_change_request,
    description="Use this to file a ServiceNow change request. Input format: first line = short desc, rest = long description."
)

if __name__ == "__main__":
    input_data = "Deploy PostgreSQL-to-Oracle conversion for inventory system\nScheduled for 9 PM Friday. Marked as high priority."
    result = create_change_request(input_data)
    print(result)
