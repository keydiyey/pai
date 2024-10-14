import json

USERS_PATH = "./assets/data/users.json"



#------------------------- Loading Data
def load():
	try:
		with open(USERS_PATH, "r", encoding="utf-8") as u:
			return json.load(u)
	except FileNotFoundError:
		return print("Error: File not found.")

#----------------------------- Finalize Changes
def update(new_data):
	with open(USERS_PATH, "w") as u:
		try:
			json.dump(new_data, u, indent=4)
		except Exception as e:
			print(e)
		

#----------------------------- Check if exists

def is_existing(UID):
	data = load()
	if str(UID) in data:
		return True    
	else:
		return False



#--------------------------- Register new users in Bank

def register(UID):
	if not(isinstance(UID, str)):
		UID = str(UID)

	users = load()

	users[UID] = {}
	users[UID]["credits"] = 5000
	users[UID]["divorce"] = 0
	users[UID]["deaths"] = 0
	users[UID]["jailtime"] = 0



	update(users)

	










