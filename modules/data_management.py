import json

#------------------------- Loading Data
def load(PATH:str):
	try:
		with open(PATH, "r") as u:
			return json.load(u)
	except FileNotFoundError:
		return {}
	
def load_users():
	return load("/assets/data/users.json")

def load_bank():
	return load("/assets/data/bank.json")



#-------------------------- Fetch Data Requests
def get(user_id, type, data):
	if not(isinstance(user_id, str)):
			user = str(user_id)

	if type == None:
		output = data[user]
	else:
		output = data[user][type] 
	return output

def get_credits(user_id):
	data = load_users()
	get(user_id, "credits", data)

def get_funds(user_id):
	data = load_bank()
	get(user_id, "funds", data)
	pass





#----------------------------- Finalize Changes
def update(new_data):
	with open("settings/users.json", "r") as u:
		json.dump(new_data, u, indent=4)















