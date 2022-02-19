import json

var = {  
      "Subjects": { 
                  "Maths":85, 
                  "Physics":90
                   } 
      } 

with open('sample-json.json', 'w') as f:
  json.dump(var, f)
  
with open('sample-json.json', 'r') as f:
  file_read = json.load(f)
  print(file_read)
