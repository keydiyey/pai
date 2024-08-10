
# Discord Packages
import discord 
from discord.ext import tasks, commands

import utils.transactions as transaction
from cogs.economy.bank_errors import BankErrors as bank_error
import utils.database as database

name = { "en":"Momiji Bank", "jp":"紅葉銀行"}

def bank_embed(description):
	embed = discord.Embed(title="🍁 Momiji Northland Bank", description = description)
	embed.set_image(url="https://i.imgur.com/ajCEmdh.png?1")

	return embed



class bank_buttons(discord.ui.View):

	# Checking User Profile
	@discord.ui.button(label="Profile", style=discord.ButtonStyle.blurple, emoji="👤") 
	async def profile_callback(self, button, interaction):
		user = interaction.user
		UID = user.id

		desc = f'''**Credits** {database.get_credits(UID)} ◉ 
				\n**Reputation**  {database.get_reputation(UID)} 
				\n\n **Deaths**  {database.get_deaths(UID)} 
				\n **Jailtime** {database.get_jailtime(UID)} '''
		profile = discord.Embed(description =  desc, color = 0xf5e2e4)
		profile.set_thumbnail(url = "https://static.wikia.nocookie.net/gokurakugai/images/3/37/Gokurakugai_Troubleshooter_Agency_Logo.png/revision/latest/scale-to-width/360?cb=20221023100708")
		profile.set_author(name = user.display_name, icon_url = user.display_avatar.url)

		await interaction.response.defer() #need to defer before changing for some reason

		return await interaction.edit_original_response(embed = profile, view = None)

	@discord.ui.button(label="Send Credits", style=discord.ButtonStyle.blurple, emoji="⬆") 
	async def transfer_callback(self, button, interaction, member, amount):
			user = interaction.user
			transaction.transfer_credits(user.id, member.id, amount)
		
class Bank(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(name = "bank", description= "🍁 紅葉銀行 | Momiji Northland Bank")
	async def bank(self, ctx:discord.ApplicationContext):
		data = database.load()
		
		if str(ctx.author.id) in data:
			description = '''Welcome to Momiji Northland Bank! We're happy to assist you with your finances. Today, would you like to take a look at your profile or send some credits to another member?'''
			embed = bank_embed(description)

			await ctx.respond(embed = embed, view = bank_buttons())			

		else:	
			database.register(ctx.author.id)
			description = '''It seems like you do not have an account. You have been automatically registered to the system.'''
			embed= bank_embed(description)
			await ctx.respond( embed = embed, view = bank_buttons())
			
def setup(bot):
	bot.add_cog(Bank(bot))







