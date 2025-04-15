from fastapi import FastAPI, Request
from tools.mcp_agent import agent
import uvicorn

app = FastAPI()

@app.post("/run")
async def run_agent(req: Request):
    body = await req.json()
    prompt = body.get("prompt", "")
    result = agent.run(prompt)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run("run_server:app", host="127.0.0.1", port=8000, reload=True)
