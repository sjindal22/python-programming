import csv
import heapq
import math

def printBipedalDinosaursOrderBySpeed(filePathDinoInfo, filePathAddInfo):
    
    bipedalDinosaurs = {}
    rows = []
    g = 9.8
    speed = 0
    
    with open(filePathAddInfo, 'r') as f:
        freader = csv.reader(f, delimiter=",")
    
        for row in freader:
          rows.append(row)
        
        for dataset in rows[1:]:
          if dataset[2] == "bipedal":
            bipedalDinosaurs[dataset[0]] = [float(dataset[1])]
    
    with open(filePathDinoInfo, 'r') as infoFile:
        infoFileReader = csv.reader(infoFile, delimiter=",")
   
        rows = [] 
        
        for row in infoFileReader:
          rows.append(row)
        
        for dataset in rows[1:]:
          if dataset[0] in bipedalDinosaurs.keys():
            bipedalDinosaurs[dataset[0]].append(float(dataset[1]))
            STRIDE_LENGTH, LEG_LENGTH = bipedalDinosaurs[dataset[0]][0], bipedalDinosaurs[dataset[0]][1]
            speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * g)
            bipedalDinosaurs[dataset[0]] = speed


    heap = [(value, key) for key, value in bipedalDinosaurs.items() if not (isinstance(value, list))]
    fastest = heapq.nlargest(len(heap), heap)  # O(n + mlogn)
    print(*[name for speed, name in fastest], sep='\n')

printBipedalDinosaursOrderBySpeed('dataset1.csv', 'dataset2.csv')
