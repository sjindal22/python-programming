from getpass import getpass
import requests

response = requests.get("https://api.github.com/search/repositories")
doc = response.json()
print(doc['documentation_url'])
print(doc['errors'][0]['code'])

res = requests.get('https://api.github.com/user', auth=('username', getpass()))

'''
O/P:
https://docs.github.com/v3/search
missing
Password: 
'''
