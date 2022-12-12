import discord #upm package(py-cord)
import time
import json
import asyncio
import paiconomy as pc

from discord.ui import Button, View
from discord.ext import tasks, commands
from discord.commands import SlashCommandGroup

class Economy(commands.Cog):
	def __init__(self, bot):
		self.bot = bot	

	economy = SlashCommandGroup("economy", "idk what to put here")
	
#----------Commands---------
	@economy.command(name = "balance", description = "How much money you got.")
	async def bal(self, ctx:discord.ApplicationContext, user: discord.Member = None):
		if user == None:
			user = ctx.author
		else:
			pass
		balance = pc.GetBalanceSheet(user)
		return await ctx.respond(embed = balance)

	@economy.command(name = "profile", description = "Your ID i guess.")
	async def profile(self, ctx:discord.ApplicationContext, user: discord.Member = None):
		if user == None:
			user = ctx.author
		else:
			pass

		profile = pc.OpenProfile(user)
		
		return await ctx.respond(embed = profile)

#---------  income --------
	@economy.command(name = "daily", description = "Your daily dose of internet.")
	async def daily(self, ctx:discord.ApplicationContext, user: discord.Member = None):
		amount = pc.randomNumber(500, 1000)
		pc.pay(user, amount)
		embed = discord.Embed(description =  f"Paibank gives {amount}◉ to {user.display_name}.", color = 0xf5e2e4)
		return await ctx.send(embed = embed)

def setup(bot):
	bot.add_cog(Economy(bot))

