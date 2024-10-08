import discord #upm package(py-cord)
import asyncio

from random import randint
from discord.ext import commands

import utils.database as db

# Known Bugs and Status
# ✅ 
# ✅ pre-checking of roles 
# ✅ removal of roles for punishment
# ✅ double response?
# ✅ cooldown doesnt work too damn
# ✅ cooldown error message
# ⬜ integration doesnt work?


class Marriage(commands.Cog):
	def __init__(self, bot):
		
		self.bot = bot
	

	@commands.slash_command(name = "marry", description = "marry another member!")
	@commands.cooldown(1, 30, commands.BucketType.user)
	async def marry(self, ctx:discord.ApplicationContext, member: discord.Member):
		# open users data
		# add member to user id marriage list
		# add user to member marriage list
		# commit users data
		pass


	@commands.slash_command(name = "date", description = "marry another member!")
	@commands.cooldown(1, 30, commands.BucketType.user)
	async def date(self, ctx:discord.ApplicationContext, member: discord.Member):
		pass

	@commands.slash_command(name = "divorce", description = "marry another member!")
	@commands.cooldown(1, 30, commands.BucketType.user)
	async def divorce(self, ctx:discord.ApplicationContext, member: discord.Member):
		pass


def setup(bot):
	bot.add_cog(Marriage(bot))