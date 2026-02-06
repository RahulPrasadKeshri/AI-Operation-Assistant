from llm.llm_client import ask_llm

def verify(raw):
    prompt = f"Clean and summarize this data nicely: {raw}"
    return ask_llm(prompt)
