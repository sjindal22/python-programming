import csv

def csvParser(file):

  with open(file, 'r') as f:
    csvFile = csv.reader(f, delimiter=",")
    
    header = next(csvFile)
    print(header)

    for people in csvFile:
      if(int(people[1]) >= 30):
        print("Name: {name}, City: {city}".format(name=people[0], city=people[2]))
      
csvParser("sample_input.csv")
