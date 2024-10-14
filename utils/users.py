import json
import utils.wrappers as wrappers

USERS_PATH = "./assets/data/users.json"

def load():
		try:
			with open(USERS_PATH, "r", encoding="utf-8") as u:
				return json.load(u)
		except FileNotFoundError:
			return print("Error: File not found.")
	
def get(UID, type=None):
	#print("at get")
	data = load()
	UID = str(UID)
	if type == None:
		output = data[UID]
	else:
		output = data[UID][type]
	return output

class User:
	def __init__(self, uid):
		#print("@init")
		self.credits = get(uid, "credits")
		self.reputation = get(uid, "reputation")
		self.jailtime = get(uid, "jailtime")
		self.deaths = get(uid, "deaths")
		self.marriage = get(uid, "marriage")
		self.banner = get(uid, "banner")

	
