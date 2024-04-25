import discord #upm package(py-cord)
import data_management as pc
from utils.utils import *
from discord.ext import tasks, commands



# Handles Bot to Discord Integration with Embeds
# Creates Embed GUIs


class Economy(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		

	#----------Commands---------	
	@commands.command(name = "profile", description = "How much money you got.")
	async def profile(self, ctx, user: discord.Member = None):
		if user == None:
			user = member(ctx.author)
   
		userid = user.id
		profileData = self.database.fetchUser(userid)
    
		if profileData != None:
			
			desc = f'''**Credits** {profileData[1]} ◉ 
   					\n**Reputation**  {profileData[2]} 
         			\n\n **Deaths**  {profileData[3]} \n **Jailed** {profileData[4]} '''
			profile = discord.Embed(title = user.display_name,description =  desc, color = 0xf5e2e4)
			profile.set_thumbnail(url = user.display_avatar.url)
			await ctx.reply(embed = profile)

		else:
			pass
		


def setup(bot):
	bot.add_cog(Economy(bot))

