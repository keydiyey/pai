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
	UID =str(UID)
	MID = str(MID)
	data = db.load()
	date = round(datetime.now().timestamp())

	marriage_data = data[UID]['marriage'] 

	marriage_data |=  {MID : date} 

	return db.update(data)

async def delete(UID):
	UID =str(UID)
	data = db.load()

	marriage_data = data[UID]['marriage'] 

	marriage_data.pop(UID)

	return db.update(data)


class marriage_buttons(discord.ui.View):
	def __init__(self, *items, timeout = 180, disable_on_timeout = False, bot, user, member):
		super().__init__(*items, timeout=timeout, disable_on_timeout=disable_on_timeout)
		self.bot = bot
		self.user = user
		self.member = member

	async def interaction_check(self, interaction: discord.Interaction):
		return self.member.id == interaction.user.id

	# Checking User Profile
	@discord.ui.button(label="Yes", style=discord.ButtonStyle.green, emoji="✅") 
	async def accept_callback(self, button, interaction):
		# interaction.user should be member
		try:
			
			await add(self.user.id, self.member.id)
			await add(self.member.id, self.user.id)

			title = "Congratulations on being married!"

			url = "https://64.media.tumblr.com/7f3f0b5602d99cd40a4488c5ec88c687/9470f7fcbd4ac983-dc/s540x810/48777ed15657c50efe8d10436922e5315d21a0f8.gif"

			embed = discord.Embed(title=title, color = 0xf5e2e4)
			embed.set_image(url=url)

			await interaction.response.defer() # do not delete future kj need to defer before editing embed for some reason 

			return await interaction.edit_original_response(embed = embed, view = None)
			
		except Exception as e:
			print(e)

		

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
						description="Do you take this woman to be your wife, to live together in (holy) matrimony, to love her, to honor her, to comfort her, and to keep her in sickness and in health, forsaking all others, for as long as you both shall live?",
						color = 0xf5e2e4)
		embed.set_thumbnail(url="https://pbs.twimg.com/media/GFn9BZVawAAP_eJ.png")
		
		return await ctx.respond(embed = embed, view = marriage_buttons(timeout=60, bot=self.bot, user=user, member=member))

		

		

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