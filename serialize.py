import json

# Data to be written
dictionary ={
      "id": "04",
        "name": "sunil",
          "department": "HR"
}

print(json.dumps(dictionary, indent=4, sort_keys=True))

{
    "department": "HR",
    "id": "04",
    "name": "sunil"
}
