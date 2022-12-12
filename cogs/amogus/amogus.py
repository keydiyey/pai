import discord #upm package(py-cord)
import asyncio

import paiconomy as pc
import mafiaSetup as ms

from discord.ext import tasks, commands


#------------------- Commands ----------------------
class Amogus(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	async def start(ctx):
		await ctx.send("@everyone amogus has started f{num} of imposters are among us.")
		
		return

	def imposter(ctx, guild):
		members = discord.Guild.members()

		return
	
	

def setup(bot):
	bot.add_cog(Amogus(bot))