import discord #upm package(py-cord)
import requests
import sys, traceback
import os
import time
import server
import utils.database as pc
from discord.ext import commands

class Passive(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	


	@commands.Cog.listener()
	async def on_ready(self):
		return


def setup(bot):
	bot.add_cog(Passive(bot))