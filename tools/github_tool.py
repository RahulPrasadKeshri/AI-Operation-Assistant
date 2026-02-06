import requests

def search_repo(query):
    url = f"https://api.github.com/search/repositories?q={query}"
    return requests.get(url).json()
