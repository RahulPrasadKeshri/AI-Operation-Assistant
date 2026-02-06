from fastapi import FastAPI
from agents.planner import create_plan
from agents.executor import execute
from agents.verifier import verify
import json

app = FastAPI()

@app.post("/run")
def run(task: str):
    plan = json.loads(create_plan(task))
    raw = execute(plan)
    final = verify(raw)
    return {"result": final}