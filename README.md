# 🛠 MCP Agent for ServiceNow Change Management

This project provides a **Migration Conversion Platform (MCP) agent** built using [LangChain](https://www.langchain.com/) and [LangGraph](https://www.langgraph.ai/) frameworks. It integrates with **ServiceNow** to automate **change request creation** via a conversational agent (like Azure Copilot or OpenAI).

---

## 🚀 Features

- Uses `LangChain` + `LangGraph` to build an LLM-powered agent
- Integrates with ServiceNow REST APIs
- Provides a custom tool to create change requests
- Ready to use from within VS Code with prompts

---

## 📦 Requirements

- Python 3.10 or later
- OpenAI API Key
- A ServiceNow instance (with credentials + API access)

---

## 🔧 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Siths/mcp-agent-servicenow.git
   cd mcp-agent-servicenow
   
2. **Create a Virtual Environment**

    ```bash
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows
    
3. **Set Up Environment Variables**
***Create a .env file with the following content:***
```bash
.env
OPENAI_API_KEY=your_openai_api_key
SERVICENOW_INSTANCE=https://your_instance.service-now.com
SERVICENOW_USERNAME=your_username
SERVICENOW_PASSWORD=your_password

4.  ** Install required Python packages **
pip install -r requirements.txt

5. ** Run the MCP Agent Server **
``bash .env
python run_server.py

6. ** In Co-Pilot change it to agent mode **
***Following are the sample prompots to create change request:***

Create a ServiceNow change request to deploy PostgreSQL-to-Oracle conversion for inventory system, scheduled for 9 PM Friday. Mark it as a high priority.

Sample SNOW Screen shot - Create/Change Changement
![Alt Text]([https://github.com/yourusername/repo-name/blob/main/assets/image.png](https://github.com/Siths/mcp-agent-servicenow/blob/main/asset.png)


![ServiceNow Change Request Demo](https://github.com/Siths/mcp-agent-servicenow/blob/main/asset.png "Demo of MCP Agent creating a change request")

