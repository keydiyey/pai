import json
from random import randint
import discord #upm package(py-cord)
import os

#---------- Errors --------------
async def generalError(ctx):
	embed = discord.Embed(title = "That did not worked well...",description =  "The command will not proceed due to some conflict but this is not on us. Probably try again after a while.", color = 0xf5e2e4)
	
	return await ctx.send(embed = embed)

async def poorError(ctx):
	embed = discord.Embed(title = "That did not worked well...",description =  "You do not have enough balance in your account.", color = 0xf5e2e4)
	
	return await ctx.send(embed = embed)

#--------------------

def chance():
	x = randint(0, 3)
	y = randint(0, 3)
	if x == y:
		return True
	else: 
		return False

def chancePercent(GlobalChance):
	x = randint(0, 1000)
	if x > GlobalChance:
		return True
	else:
		return False
def randomNumber(lower:int, higher:int):
	x= randint(lower, higher)
	return x

def statusTime():
	time = randint(15, 180)
	return time

def read(address):
	with open(address, encoding = "utf8") as a:
		data = json.load(a)
	return data

def write(data, address):
	with open(address, "w") as info:
		json.dump(data, info, indent = 4)
	return

def GetInfo(user, type):
	if isinstance(user, str):
		userID = user
	else:
		userID = str(user.id)
	data = read("data/user_info.json")
	info = data[userID][type]
	return info

def GetUserList():
	UserList = read("data/user_info.json")
	return UserList

def GetCredits(user):
	credits = GetInfo(user, "credits")
	return credits

def GetReputation(user):
	rep = GetInfo(user, "rep")
	return rep

def GetVault(user):
	vault = GetInfo(user, "vault")
	return vault

def AddUserBalance(user, arg, amount):
	userID = str(user.id)
	users = GetUserList()
	users[userID][arg] -= amount
	arg = users[userID][arg] 

	write(users, "data/user_info.json")

def checkPoor(self, user, amount):
		credits = pc.GetCredits(user)
		if credits >= amount:
			return False
		else:
			return True

def take(user, amount):
	userID = str(user.id)
	users = GetUserList()
	users[userID]["credits"] -= amount
	credits = users[userID]["credits"] 

	write(users, "data/user_info.json")

def pay(user, amount):
	userID = str(user.id)
	users = GetUserList()
	users[userID]["credits"] += amount
	credits = users[userID]["credits"] 

	write(users, "data/user_info.json")

def AddCounter(user, type, amount):
	userID = str(user.id)
	users = GetUserList()
	users[userID]["counter"][type] -= amount 
	type = users[userID]["counter"][type]

	write(users, "data/user_info.json")

def OpenAccount(userID, guildID):
	""" Opens your Yuen account. """
	try:
		users = getUserInfo()
		users[userID] = {}
		users[userID]["credits"] = 1000
		users[userID]["rep"] = 0
		users[userID]["counter"] = {}
		users[userID]["counter"]["jailed"] = 0
		users[userID]["counter"]["death"] = 0

		write(users, "data/user_info.json")
	
	except Exception as e:
		print(e)
	return
	
def OpenProfile(user):
	userID = str(user.id)
	users = GetUserList()
	credits = users[userID]["credits"]
	rep = users[userID]["rep"]

	jailed = users[userID]["counter"]["jailed"]
	deaths = users[userID]["counter"]["death"]

	desc = f"**Credits** {credits} ◉ \n**Reputation**  {rep} \n\n **Deaths**  {deaths} \n **Jailed** {jailed} "
	profile = discord.Embed(title = user.display_name,description =  desc, color = 0xf5e2e4)
	profile.set_thumbnail(url = user.display_avatar.url)
	return profile


def GetBalanceSheet(user):
	credits = GetInfo(user, "credits")
	desc = f"**Credits** {credits} ◉ "
	balance = discord.Embed(title = f" {user.name}'s Balance ", description = desc, color = 0xf5e2e4)
	balance.set_thumbnail(url = user.display_avatar.url)
	return balance

async def localImage(embed, directory:str):
	
	file = discord.File(os.getcwd() + directory, filename='image.png')  
	embed.set_thumbnail(url='attachment://image.png')
	return file
	
#--------------- qEmbed ------
async def qEmbed(ctx, description):
	embed = discord.Embed(description =  description, color = 0xf5e2e4)
	return await ctx.respond(embed = embed)







