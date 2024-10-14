import discord #upm package(py-cord)
import asyncio

from random import randint
from discord.ext import commands
from datetime import datetime


import utils.database as db

# Known Bugs and Status
# ✅ 
# ⬜ 


async def add(UID, MID):
	data = db.load()
	date = datetime.now().timestamp()

	marriage_data = data[UID]['marriage'] 

	marriage_data |=  {MID : date} 

	return db.update(data)

async def delete(UID):
	data = db.load()

	marriage_data = data[UID]['marriage'] 

	marriage_data.pop(UID)

	return db.update(data)


class marriage_buttons(discord.ui.View):

	# Checking User Profile
	@discord.ui.button(label="Yes", style=discord.ButtonStyle.green, emoji="✅") 
	async def accept_callback(self, button, interaction):
		return True

	@discord.ui.button(label="No", style=discord.ButtonStyle.red, emoji="❎") 
	async def reject_callback(self, button, interaction, member, amount):
		return False

class Marriage(commands.Cog):
	def __init__(self, bot):
		
		self.bot = bot
	

	@commands.slash_command(name = "marry", description = "marry another member!")
	@commands.cooldown(1, 30, commands.BucketType.user)
	async def marry(self, ctx:discord.ApplicationContext, member: discord.Member):
		user = ctx.user
		embed = discord.Embed(title=f"{user.display_name} has proposed to {member.display_name}!",
						description="Do you take this woman to be your wife, to live together in (holy) matrimony, to love her, to honor her, to comfort her, and to keep her in sickness and in health, forsaking all others, for as long as you both shall live?")
		
		decision = ctx.respond(embed = embed, view = marriage_buttons(timeout=60))

		try:
			if decision == True:
				await add(user.id, member.id)
				await add(member.id, user.id)
				url = "https://64.media.tumblr.com/7f3f0b5602d99cd40a4488c5ec88c687/9470f7fcbd4ac983-dc/s540x810/48777ed15657c50efe8d10436922e5315d21a0f8.gif"
				title = "Congratulations on being married!"

			else:
				url = "https://animesher.com/entry/pastel-colors-anime-gif-spirited-away-2031329/"
				embed = discord.Embed(description=f"You or target member is already dead or in jail. Please try again later.", color=0xffd9cc)
				title = f"{member.display_name} has rejected {user.display_name}'s proposal!"

		except Exception as e:
			print(e)
		
		embed = discord.Embed(title=title)
		
		await ctx.response.defer() # do not delete future kj need to defer before editing embed for some reason 

		return await ctx.edit_original_response(embed = embed, view = None)

		

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