import discord #upm package(py-cord)
import random
import time
import json
import asyncio

from math import floor
from discord.ext import tasks, commands

class Error(commands.Cog):
	def __init__(self, bot):
		
		self.bot = bot



	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandNotFound):
			pass

		elif isinstance(error, commands.MissingRequiredArgument):
			embed = discord.Embed(description = f"Seems like you missed a required argument. If you are gambling, try betting something!" ,color = discord.Color.red())
			await ctx.send(embed=embed, delete_after = 3)

		elif isinstance(error, commands.CheckFailure):
			embed = discord.Embed(description = f"You are either dead or in jail. You are helpless. Repent on your sins and someone might help you.")
			await ctx.send(embed=embed, delete_after = 3)
			
		elif isinstance(error, commands.CommandOnCooldown):
			cd = int(error.retry_after)
			
			if 60 < cd < 60*60 :
				time = str(floor(cd/60)) + " min. " + str(floor(cd%60)) + " sec."

			elif 60*60 < cd :
				time = str(floor(cd/(60*60))) + " hr(s). " + str(floor((cd%(60*60))/60)) + " min. " + str(floor(((cd%(60*60))%60)/60)) + "sec."
			
			else:
				time = str(round(cd)) + " second(s)."

			embed = discord.Embed(description = f"Wait {ctx.author.name}! This command is on cooldown. Please wait {time}" ,color = discord.Color.red())
			await ctx.send(embed=embed, delete_after = 3)
		else:
			print(error)



def setup(bot):
	bot.add_cog(Error(bot))