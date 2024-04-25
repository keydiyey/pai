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



def AddUserBalance(user, arg, amount):
	userID = str(user.id)
	users = GetUserList()
	users[userID][arg] -= amount
	arg = users[userID][arg] 

	write(users, "data/user_info.json")


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


async def localImage(embed, directory:str):
	
	file = discord.File(os.getcwd() + directory, filename='image.png')  
	embed.set_thumbnail(url='attachment://image.png')
	return file
	
#--------------- qEmbed ------
async def qEmbed(ctx, description):
	embed = discord.Embed(description =  description, color = 0xf5e2e4)
	return await ctx.respond(embed = embed)







