import discord #upm package(py-cord)
from random import randint
from utils.utils import *
import json
import asyncio
import modules.data_management as pc
import modules.mafiaSetup as ms

from discord.ext import tasks, commands

class Gambling(commands.Cog):
	def __init__(self, bot):
		
		self.bot = bot

#-------------------------------------------------------------------------------

	async def coinflip(self, ctx, bet:int):
     
		player = player(ctx.author)

		if bet_checker(player, bet) == False:
			return await pc.poorError(ctx)
		else:
			msg = await ctx.send(" :coin: **| Tossing the coin...**")
			await asyncio.sleep(3)
			if pc.chancePercent(452) == False:
				pc.pay(player.name, bet)				
			else:
				pc.take(player.name, bet)
				await msg.edit(content = f" :coin: **| The coin landed upside down and you lost.**")		
			

def setup(bot):
	bot.add_cog(Gambling(bot))
 
 
 
 