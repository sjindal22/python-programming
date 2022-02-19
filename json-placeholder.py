import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
print(response)

jsonData = json.loads(response.text)

def checkTodo(json_data):

  #if json_data["completed"] == "false":
  check = json_data["completed"] 
  userID = json_data["userId"]
  return check and userID

l1 = list(filter(checkTodo, jsonData))
print(l1)
