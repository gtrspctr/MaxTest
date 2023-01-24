import requests
import json

url = "https://alrobison.com/users"
req = requests.get(url)
json_data = json.loads(req.text)

class User:
    def __init__(self,
                 id,
                 name,
                 username,
                 email,
                 address,
                 phone,
                 website,
                 company):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.street = address["street"]
        self.suite = address["suite"]
        self.city = address["city"]
        self.zipcode = address["zipcode"]
        self.latitude = address["geo"]["lat"]
        self.longitude = address["geo"]["lng"]
        self.phone = phone
        self.website = website
        self.comp_name = company["name"]
        self.comp_catchphrase = company["catchPhrase"]
        self.comp_bs = company["bs"]

    @classmethod
    def create_user(cls):
        return cls(**json_data)

user_list = []
for data in json_data:
    user_list.append(User(**data))

for user in user_list:
    print(user.name)
    print()