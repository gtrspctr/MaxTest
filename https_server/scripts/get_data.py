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

# Take json dicts and create python objects
user_list = []
for data in json_data:
    user_list.append(User(**data))

# Get user object attributes
# Will use these for requests
for key, value in user_list[0].__dict__.items():
	obj_attributes.append(key)
	total_attributes += 1

# clearScreen() simply prints a blank line 50 times
# to help keep these easy to read.
def clearScreen():
	for i in range(50):
		print()

# parseIntAndRange() attempts to change a string into an integer.
# If successful, it checks if integer is between min and max.
# if unsuccessful, it will catch an error and return false
def parseIntAndRange(choice, min, max):
	try:
		choice = int(choice)
		if isinstance(choice, int) and choice >= min and choice <= max:
			# choice is an integer and it's in the correct range
			return True
		else:
			# choice is an integer but NOT in the correct range
			return False
	except:
		# choice cannot be turned into an integer
		return False

# requestAll() simply prints a dump of all json_data,
# with each dict separated by a blank space for
# readability.
def requestAll():
	for item in json_data:
		print(item)
		print()

# requestValue() asks the user which json dict they
# would like to update. It lists the 'names' of the
# dicts.
# It uses a while loop and parseIntAndRange() to verify
# input is valid.
# Then asks the user which value they would like to 
# update by giving them the keys for the specified
# user. Again, uses while loop and parseIntAndRange()
# It then asks the user for the new value.
# Then uses all the user input to figure out which
# object/attribute to change, and updates the value.
def requestValue():
	clearScreen()

	# Ask user which object to update
	data_choice = ""
	while True:
		print("Which user would you like to update?")
		counter = 1
		for user in user_list:
			print(str(counter) + ". " + user.name)
			counter += 1
		data_choice = input("Enter a number: ")

		if parseIntAndRange(data_choice, 1, 10):
			data_choice = int(data_choice)
			break
		else:
			print("Not a valid option.")
			print("Please enter a number corresponding with")
			print("your desired action.")
			print()
			print()

	print()
	print()

	# Ask user which key to update
	key_choice = ""
	while True:
		print("Which key would you like to update?")
		counter = 1
		for attr in obj_attributes:
			print(str(counter) + ". " + attr)
			counter += 1
		key_choice = input("Enter a number: ")

		if parseIntAndRange(key_choice, 1, 14):
			key_choice = int(key_choice)
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

	print()
	print()
	
	attr = obj_attributes[key_choice-1]
	#print(str(user_list[data_choice-1]).attr)
	print(str(user_list[data_choice-1]).__dir__[key_choice-1])
	print("")

def changeValue():
	## USE ABOVE FUNCTION HERE
	# Ask user for updated value
	value_choice = input("Enter the updated value: ")

	# Whichever number user chooses, minus by 1 for array index
	attr = obj_attributes[key_choice-1]
	print()
	print("Old value: " + str(attr))
	user_list[data_choice-1].attr = value_choice
	print("New value: " + value_choice)

	# NEED TO POST HERE

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
		if parseIntAndRange(choice, 1, 5):
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

