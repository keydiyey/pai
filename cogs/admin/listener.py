import discord #upm package(py-cord)
import requests
import sys, traceback
import os
import time
import srv
import paiconomy as pc

from discord.ext import commands

class Passive(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		srv.srv()
		print('----------------------------------\n')
		print('Welcome back Master!')
		print('Pai is now online! \n')
		
		await self.bot.change_presence(
			activity = discord.Activity(type = discord.ActivityType.watching, name = 'you make mistakes...'))

	async def on_member_join(self,member):
		pc.OpenAccount(member.id)
		await member.send(f"Welcome to the server, {member.mention}! Enjoy your stay here. An account for you has automatically been created if you still do not have one. Ask 'pai help' for more details.")

	@commands.Cog.listener()
	async def on_ready(self):
		return


def setup(bot):
	bot.add_cog(Passive(bot))