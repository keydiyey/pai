
# Discord Packages
import discord 
from discord.ext import tasks, commands

import utils.users as users


class User(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(name = "profile", description= "🍁 check your profile")
	async def profile(self, ctx, user:discord.Member):
		UID = user.id
		data = users.User(str(UID))


		embed = discord.Embed(title= user.display_name, color = 0xf5e2e4)

		embed.add_field(name="Credits", value= data.credits, inline=True)
		embed.add_field(name="Divorce Counter", value=data.divorce, inline=True)
		embed.add_field(name="", value="", inline=False) # placeholder

		embed.add_field(name="Jail time", value= data.jailtime, inline=True)
		embed.add_field(name="Deaths", value="0", inline=True)

		# marital status will output as list so...
		text = ""

		for key, value in data.marriage.items():

			wife = ctx.guild.get_member(int(key))

			text += f"{wife.display_name}  💍 <t:{value}:R> \n" 
			
		embed.add_field(name="Marital Status", value=text, inline=False)

		embed.set_image(url= data.banner)

		embed.set_thumbnail(url = user.display_avatar.url)
		embed.set_footer(text=f"ID : {UID}")

		return await ctx.respond(embed = embed, view = None)
	

def setup(bot):
	bot.add_cog(User(bot))