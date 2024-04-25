import modules.data_management as dm


def add_credits(user_id, amount):
	credits = dm.get_credits(user_id)   # gets credit info
	credits += amount					# adding amount
	dm.update(credits)					# updates json file


def subtract_credits(user_id, amount):	
	credits = dm.get_credits(user_id)   # gets credit info
	credits -= amount					# subtract amount
	dm.update(credits)					# updates json file


def set_credits(user_id, amount):   	# ⚠ for admin only
	credits = dm.get_credits(user_id)   # gets credit info
	data = dm.get(user_id)[amount]		# calls data[user_id] and attaches new credit
	dm.update(data)						# updates json file


# BANK TRANSACTIONS 
def deposit(user_id, amount):
	funds = dm.get_funds(user_id)
	funds += amount
	dm.update(funds)

def withdraw(user_id, amount):
	funds = dm.get_funds(user_id)
	funds += amount
	dm.update(funds)
