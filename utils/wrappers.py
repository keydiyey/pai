
import utils.database as database
from random import randint
import discord

def check_if_exists(func):
	def inner(**kwargs):
		UID = kwargs.get("UID")
		data = database.load()
		
		if str(UID) in data:
			func(**kwargs)

def check_transfer_credits(func):
	def inner(giver_id, receiver_id, amount = None):
		if amount <= database.get_credits(giver_id):
			func(giver_id=giver_id, receiver_id=receiver_id, amount = amount)
	return inner




def check_probability(func):
	def inner(probability, *args, **kwargs):
		if randint(0,100) <= probability: #percent success
			func(*args, **kwargs)
		else:
			return False
	return inner