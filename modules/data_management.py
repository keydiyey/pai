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




#-------------------------- Fetch Data Requests
def get(UID, data, type=None):
	if not(isinstance(UID, int)):
			UID = int(UID)

	if type == None:
		output = data[0][UID]
	else:
		output = data[0][UID]
	return output

def get_credits(user_id):
	data = load()
	get(user_id, data, "credits")


#--------------------------- Register new users in Bank

def register(UID):
	users = load()
	print(users)
	users[UID] = {}
	users[UID]["credits"] = 1000
	users[UID]["funds"] = 0
	users[UID]["reputation"] = 0
	users[UID]["deaths"] = 0
	users[UID]["jailtime"] = 0
	users[UID]["funds"] = 0

	update(users)

	





register(11111)









