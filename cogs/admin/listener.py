import discord #upm package(py-cord)
import requests
import sys, traceback
import os
import time
import server
import modules.data_management as pc
from discord.ext import commands

class Passive(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	

	async def on_member_join(self,member):
		pc.OpenAccount(member.id)
		await member.send(f"Welcome to the server, {member.mention}! Enjoy your stay here. An account for you has automatically been created if you still do not have one. Ask 'pai help' for more details.")

	@commands.Cog.listener()
	async def on_ready(self):
		return


def setup(bot):
	bot.add_cog(Passive(bot))