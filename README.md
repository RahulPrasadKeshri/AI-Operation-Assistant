# AI-Operation-Assistant

## Setup
pip install -r requirements.txt
Create .env from .env.example

## Run
uvicorn main:app --reload

## APIs Used
- GitHub Search API
- OpenWeather API
- OpenAI LLM

## Example Prompt
"Find popular Python repos and tell me weather in Delhi"

## Architecture
Planner → JSON plan  
Executor → calls APIs  
Verifier → validates output  

## Limitations
Sequential execution, no caching

~AI Operations Assistant – Multi-Agent GenAI System

This project implements an AI-powered Operations Assistant that converts natural language tasks into structured plans, executes real-world API actions, and verifies results using a multi-agent architecture.

-The system uses:
A Planner Agent powered by an LLM to generate step-by-step JSON execution plans
An Executor Agent to invoke real third-party APIs (GitHub, Weather)
A Verifier Agent to validate completeness and correctness of outputs

-It demonstrates:
Agent-based reasoning
Structured LLM outputs and tool calling
End-to-end autonomous task execution

-Key Capabilities
✔ Natural language task understanding
✔ Multi-agent orchestration
✔ Real API integrations
✔ Local runnable AI system

-Example Task
“Find trending AI repositories and show current weather in Mumbai”

-Tech Stack:
Python
FastAPI
OpenAI LLM
GitHub API
OpenWeather API

