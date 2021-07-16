import requests

BASE_URL = "http://127.0.0.1:5000/"

response = requests.get(BASE_URL+"helloworld/8333/67")
print(response.json())