from jsonschema import validate
import json 

def jsonValidation(json_blob, schema, json_document = None):

  try:
    validate(json_blob, schema)
    if json_document != None:
      datum = json.loads(json_document)
      print(type(datum))

  except ValueError as err:
    return False
  
  return True

schema = {
     "type" : "object",
     "properties" : {
         "price" : {"type" : "number"},
         "name" : {"type" : "string"},
     },
 }

json_doc = """{
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


json_blob = {"name" : "Eggs", "price" : 34.99}
print(jsonValidation(json_blob, schema, json_doc))
