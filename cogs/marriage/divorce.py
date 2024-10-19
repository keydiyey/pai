import discord #upm package(py-cord)
import asyncio

from discord.ext import commands

import utils.database as db
import utils.users as users


async def delete(UID, MID):
	UID =str(UID)
	MID =str(MID)
	data = db.load()

	marriage_data = data[UID]['marriage'] 
	marriage_data.pop(MID)

	data[UID]['divorce'] += 1

	return db.update(data)

class divorce_dropdown(discord.ui.Select):
	def __init__(self, bot, user):
		self.bot = bot
		self.user = user

		data = users.User(str(user.id))

		options = []
		

		for key, value in data.marriage.items():
			wife = user.guild.get_member(int(key))
			
			option = discord.SelectOption(label= wife.display_name, value=key)

			options.append(option)
		
		super().__init__(
			placeholder="Choose a wife...",
			min_values=1,
			max_values=1,
			options=options,
		)
		
	async def callback(self, interaction): # the function called when the user is done selecting options
		try:
			await delete(self.user.id, self.values[0])
			await delete(self.values[0], self.user.id)

			member = self.user.guild.get_member(int(self.values[0]))
			

			title = f"{self.user.display_name} has divorced {member.display_name}!"

			url = "https://64.media.tumblr.com/c43660aca9972831fb48cb3724eb427d/dd9eb2d6592050ac-43/s640x960/008953517cdfa3457c1034aa1b9acdd0c4784f9e.gif"

			embed = discord.Embed(title=title, color = 0xf5e2e4)
			embed.set_image(url=url)

			await interaction.response.defer() # do not delete future kj need to defer before editing embed for some reason 

			return await interaction.edit_original_response(embed = embed, view = None)

		except Exception as e:
			return print(e)
			

class divorce_view(discord.ui.View):
	def __init__(self, bot, user=None):
		super().__init__(divorce_dropdown(bot, user))
		self.user = user

	async def interaction_check(self, interaction: discord.Interaction):
		return self.user.id == interaction.user.id

class Divorce(commands.Cog):
	def __init__(self, bot):
		
		self.bot = bot
	
	@commands.slash_command(name = "divorce", description = "divorce your wife!")
	@commands.cooldown(1, 30, commands.BucketType.user)
	async def divorce(self, ctx:discord.ApplicationContext):
		user = ctx.user

		embed = discord.Embed(title=f"Divorce?")
		embed.set_image(url="https://64.media.tumblr.com/8b0f58e322f5274f0b77ba2a0c32915f/4d168491a5adb779-da/s540x810/352506d402ca85e789841cb0a792c34002e7f868.gifv")
		
		return await ctx.respond(embed = embed, view = divorce_view(self.bot, user))


def setup(bot):
	bot.add_cog(Divorce(bot))