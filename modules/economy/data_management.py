import json

def load():
  try:
    with open("settings/users.json", "r") as u:
      return json.load(u)
  except FileNotFoundError:
    return {}

def _is_existing(self, userid):
    data = load()
    if str(userid) in data:
        pass    
    else:
        return None
    
def get(user_id, type):
    data = load()

    if not(isinstance(user_id, str)):
        user = str(user_id)

    if type == None:
      output = data[user]
    else:
      output = data[user][type]
   
    return output


def get_credits(user_id):
    return get(user_id, "credits")


def update(new_data):
  with open("settings/users.json", "r") as u:
    json.dump(new_data, u, indent=4)


def register(self, userID):
    data=load()
    users = data
    users[userID] = {}
    users[userID]["credits"] = 1000
    users[userID]["reputation"] = 0
    users[userID]["deaths"] = 0
    users[userID]["jailtime"] = 0
    update(users)















