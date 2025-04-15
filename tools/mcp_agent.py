from langgraph.prebuilt import create_react_agent
from langchain.agents import AgentExecutor

from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from dotenv import load_dotenv
from tools.servicenow_tool import servicenow_tool  # your custom Tool
import os

OPENAI_API_KEY = "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"

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")



llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    api_key=OPENAI_API_KEY
)

# Correct way to create agent with latest langgraph
agent = create_react_agent(
    llm,
    tools=[servicenow_tool])
#agent = agent_node.create_agent()

agent_executor = AgentExecutor(agent=agent, tools=[servicenow_tool], verbose=True)
