import json
import requests

response1 = requests.get("https://jsonplaceholder.typicode.com/posts")
todos = json.loads(response1.text)
print(todos)
# print(response1.text)

