# Example with sample_input.json file

from json import load as jsonLoad

def parseJson(file):

  with open(file, 'r') as f:
    jsonFile = jsonLoad(f)

    for people in jsonFile["people"]:
      if people["age"] >= 30:
        print("Name: {name}, City: {city}".format(name=people["name"], city=people["city"]))


parseJson("sample_input.json")

print("-----Next example-----")
# Example with apod.json file

def nasaDataParse(file):

  with open(file, 'r') as f:
    jsonData = jsonLoad(f)

    return(jsonData["explanation"])

print(nasaDataParse("apod.json"))

