import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE+'Helloworld/somasundaram/31')

print(response.json())

