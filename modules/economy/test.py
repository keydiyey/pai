import json


def load_data():
  try:
    with open("settings/users.json", "r") as u:
      return json.load(u)
  except FileNotFoundError:
    return {}

def get(user_id, type):
    if not(isinstance(user_id, str)):
        user = str(user_id)

    data = load_data()
    output = data[user][type]
   
    return output


def get_user_credits(user_id):
    return get(user_id, "credits")



