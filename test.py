import requests

url = "http://localhost:7071/webhook"
data = {"key": "value"}

resp = requests.get(url)
print(resp)

resp = requests.post(url, json=data)
print(resp)
print(resp.text)
