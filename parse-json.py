from json import load as jsonLoad

def parseJson(file):

  with open(file, 'r') as f:
    jsonFile = jsonLoad(f)

    for people in jsonFile["people"]:
      if people["age"] >= 30:
        print("Name: {name}, City: {city}".format(name=people["name"], city=people["city"]))


parseJson("sample_input.json")
