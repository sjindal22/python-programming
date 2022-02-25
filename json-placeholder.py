import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")

jsonData = json.loads(response.text)
#print(json.dumps(jsonData, indent=4, sort_keys=True))

def checkTodo(json_data):

  check = json_data["completed"]
  userID = json_data["userId"]
  return check and userID

l1 = list(filter(checkTodo, jsonData))
print(l1)
