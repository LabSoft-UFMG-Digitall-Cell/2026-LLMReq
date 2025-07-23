import requests

def get_route(route: str = "health"):
    """Send a GET request to the health endpoint and return the response.json."""
    url = "http://localhost:8000/" + route
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    print(get_route("health"))
