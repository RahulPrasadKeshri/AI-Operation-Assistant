from llm.llm_client import ask_llm

def create_plan(task):
    prompt = f"""
Return JSON only.

User task: {task}

Format:
{{
 "steps": [
   {{"tool": "weather", "input": "Delhi"}},
   {{"tool": "github", "input": "AI agents"}}
 ]
}}
"""
    return ask_llm(prompt)
