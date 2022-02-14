import json

def parseJson(json_data):
  
  allEmployees = []
  json_reader = json.loads(json_data)
  employees = json_reader['employees']
  for employee in employees:
    allEmployees.append(employee['name'])
  return allEmployees

json_data = """{
  "employees":
    [
      {
        "name": "Alice",
        "role": "dev",
        "nbr": 1
      },
      {
        "name": "Bob",
        "role": "dev",
        "nbr": 2
      }
    ],
  "firm":
    {
      "name": "Charlie's Waffle Emporium",
      "location": "CA"
    }
}"""
print(parseJson(json_data))

'''
json.loads -> takes in a native string, byte or array of byte containing json
documents as a parameter.
O/P:
['Alice', 'Bob']
'''
