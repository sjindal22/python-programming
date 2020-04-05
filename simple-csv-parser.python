import csv

# Program 1

def csvParser1(filename):

  with open(filename, 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

# Print each row while the file is opened

    for row in readCSV:
      print(row)

csvParser1('dataset1.csv')


# Code Type 2

def csvParser2(filename):

  rows = []

  with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
      rows.append(row)

  print("The fields are {}".format(rows[0]))
  print(f"The rows are {rows[1:]}")

 
csvParser2('dataset1.csv')

"""
['NAME', 'LEG_LENGTH', 'DIET']
['Hadrosaurus', '1.4', 'herbivore']
['Struthiomimus', '0.72', 'omnivore']
['Velociraptor', '1.8', 'carnivore']
['Triceratops', '0.47', 'herbivore']
['Euoplocephalus', '2.6', 'herbivore']
['Stegosaurus', '1.50', 'herbivore']
['Tyrannosaurus Rex', '6.5', 'carnivore']
The fields are ['NAME', 'LEG_LENGTH', 'DIET']
The rows are [['Hadrosaurus', '1.4', 'herbivore'], ['Struthiomimus', '0.72', 'omnivore'], ['Velociraptor', '1.8', 'carnivore'], ['Triceratops', '0.47', 'herbivore'], ['Euoplocephalus', '2.6', 'herbivore'], ['Stegosaurus', '1.50', 'herbivore'], ['Tyrannosaurus Rex', '6.5', 'carnivore']]
"""
