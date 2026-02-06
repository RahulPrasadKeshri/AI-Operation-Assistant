from tools.weather_tool import get_weather
from tools.github_tool import search_repo

def execute(plan):
    results = []
    for step in plan["steps"]:
        if step["tool"] == "weather":
            results.append(get_weather(step["input"]))
        if step["tool"] == "github":
            results.append(search_repo(step["input"]))
    return results