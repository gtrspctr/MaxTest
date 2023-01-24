import requests
import json

url = "https://alrobison.com/users"

req = requests.get(url)
json_str = reg.text
print(len(json_str))

