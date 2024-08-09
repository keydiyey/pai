import json

USERS_PATH = "./assets/data/users.json"



#------------------------- Loading Data
def load():
	try:
		with open(USERS_PATH) as u:
			return json.load(u)
	except FileNotFoundError:
		return print("Error: File not found.")

#----------------------------- Finalize Changes
def update(new_data):
	with open(USERS_PATH, "w") as u:
		json.dump(new_data, u, indent=4)

#----------------------------- Check if exists

def is_existing(UID):
	data = load()
	if str(UID) in data:
		return True    
	else:
		return False


#-------------------------- Fetch Data Requests
def get(UID, type=None):
	data = load()

	if not(isinstance(UID, str)):
		UID = str(UID)
	if type == None:
		output = data[UID]
	else:
		output = data[UID][type]
	return output

def get_credits(user_id):
	return get(user_id, "credits")

def get_reputation(user_id):
	return get(user_id, "reputation")

def get_deaths(user_id):
	return get(user_id, "deaths")

def get_jailtime(user_id):
	return get(user_id, "jailtime")



#--------------------------- Register new users in Bank

def register(UID):
	if not(isinstance(UID, str)):
		UID = str(UID)

	users = load()

	users[UID] = {}
	users[UID]["credits"] = 5000
	users[UID]["reputation"] = 0
	users[UID]["deaths"] = 0
	users[UID]["jailtime"] = 0



	update(users)

	










