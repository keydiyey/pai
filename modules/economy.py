import discord #upm package(py-cord)
from utils.utils import *
from discord.ext import tasks, commands



# Handles Bot to Discord Integration with Embeds
# Creates Embed GUIs


class Economy(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name = "bank", description = "How much money you got.")
	async def bank(self, ctx, user: discord.Member = None):
		file = discord.File("./assets/images/bank.png", filename="image.png")
		embed = discord.Embed(color = 0xf5e2e4)
		embed.set_image(url="attachment://image.png" )
		await ctx.reply(embed = embed, file = file)

		profile = discord.Embed(title = "kj",description =  "yipeeee", color = 0xf5e2e4)
		await ctx.send(embed = profile)


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

