import requests

response = requests.get("http://localhost:8000/health", headers={"accept": "application/json"})

if response.ok:
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    print("Health check completed.")