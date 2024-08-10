import utils.database as dm
import utils.wrappers as wrappers


def add_credits(UID, amount):
	data = dm.load()
	data[UID]["credits"] += amount
	dm.update(data)

def deduct_credits(UID, amount = None):
	data = dm.load()
	data[UID]["credits"] -= amount
	dm.update(data)

@wrappers.check_transfer_credits
def transfer_credits(giver_id, receiver_id, amount = None, permax = None):
	if permax != None:
		credits = dm.get_credits(giver_id)
		amount = credits * permax	
	deduct_credits(giver_id, amount)
	add_credits(receiver_id, amount)
	return


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
