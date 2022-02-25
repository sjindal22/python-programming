from getpass import getpass
import requests
import json

response = requests.get("https://api.github.com/search/repositories")
doc = response.json()
#doc1 = json.loads(response.text)
#doc1 = json.dumps(doc1, indent=4)
#print(doc1)
print(doc['documentation_url'])
print(doc['errors'][0]['code'])

#res = requests.get('https://api.github.com/user', auth=('username', getpass()))

'''
O/P:
https://docs.github.com/v3/search
missing
Password: 
'''
