import requests
import json

url = "https://alrobison.com/users"
req = requests.get(url)
json_data = json.loads(req.text)

total_items = len(json_data)
obj_attributes = []
total_attributes = len(obj_attributes)

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
        self.company_name = company["name"]
        self.company_catchphrase = company["catchPhrase"]
        self.company_bs = company["bs"]

#    @classmethod
#    def create_user(cls):
#        return cls(**json_data)

user_list = []
for data in json_data:
    user_list.append(User(**data))

for key, value in user_list[0].__dict__.items():
	obj_attributes.append(key)
	total_attributes += 1

def parseInput(choice, min, max):
	try:
		choice = int(choice)
		if isinstance(choice, int) and choice >= min and choice <= max:
			return True
		else:
			return False
	except:
		return False

def requestAll():
	for item in json_data:
		print(item)
		print()

def requestValue():
	# Clear screen
	for i in range(50):
		print()

	choice = ""
	while True:
		print("Of which key would you like the value?")
		counter = 1
		for attr in obj_attributes:
			print(str(counter) + ". " + attr)
			counter += 1
		choice = input("Enter a number: ")

		if parseInput(choice, 1, 14):
			choice = int(choice)
			break
		else:
			# Clear screen
			for i in range(50):
				print()
			print("Not a valid option.")
			print("Please enter a number corresponding with")
			print("your desired action.")
			print()
			print()
"""
	match choice:
		case 1:
"""

def changeValue():
	pass

def deletePair():
	pass

def deleteAll():
	pass

#main
def main():
	choice = ""

	# Clear screen
	for i in range(50):
		print()

	while True:
		print("What would you like to do?")
		print("1. View entire key-value structure.")
		print("2. View the value for a key.")
		print("3. Specify a value to be stored under a key.")
		print("4. Delete a key-value pair.")
		print("5. Clear the entire key-value structure.")
		choice = input("Enter a number: ")

		# Parse input
		if parseInput(choice, 1, 5):
			choice = int(choice)
			break
		else:
			# Clear screen
			for i in range(50):
				print()
			print("Not a valid option.")
			print("Please enter a number corresponding with")
			print("your desired action.")
			print()
			print()

	match choice:
		case 1:
			requestAll()
		case 2:
			requestValue()
		case 3:
			changeValue()
		case 4:
			deletePair()
		case 5:
			deleteAll()

main()

