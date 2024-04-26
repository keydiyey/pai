
# Discord Packages
import discord 
from discord.ext import tasks, commands

import modules.transactions as transaction
from modules.errors import bank_error

name = { "en":"Momiji Bank", "jp":"紅葉銀行"}


class amount_modal(discord.ui.View):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.add_item(discord.ui.InputText(label="How much?"))

	async def callback(self, interaction: discord.Interaction):
		amount = self.children[0].value
		return await amount


class bank_buttons(discord.ui.View): 
	@discord.ui.button(label="Deposit", style=discord.ButtonStyle.success, emoji="➕") 
	async def deposit_callback(self, button, interaction):
		user = interaction.user
		modal = amount_modal(title="Modal via Slash Command")
		
		try:
			amount = await interaction.send_modal(modal) # Asks how much
		except:
			return await interaction.response.edit_message(embed = bank_error()) # Error handling

		transaction.deposit(user.id, amount)    # runs transaction
		
		return await interaction.response.edit_message("You clicked the withdraw!")
	
	@discord.ui.button(label="Withdraw", style=discord.ButtonStyle.success, emoji="➖") 
	async def withdraw_callback(self, button, interaction):

		user = interaction.user
		transaction.withdraw(user.id)
		await interaction.response.send_message("You clicked the withdraw!") 
		


class Bank(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(name = "bank", description= "🍁 紅葉銀行 | Momiji Northland Bank")
	async def bank(self, ctx):
		description = '''Welcome to Momiji Northland Bank! We're happy to assist you with your finances. Today, would you like to make a deposit or withdraw some credits? With a deposit, you can add funds to your account. If you're looking to take out some credits, a withdrawal can be made to use for whatever you need.'''

		embed = discord.Embed(title="🍁 Momiji Northland Bank", description=description)

	
		embed.set_image(url="https://drive.google.com/file/d/1sGDhjpLgBKoW89Bt7HS37ZPzB2A6RidQ/view?usp=drive_link")

		if "subtitle" not in record or record["subtitle"] != "French":
			add_french_subtitles(record) # or whatever

		await ctx.respond(embed = embed, view=bank_buttons())


	
		
	  


def setup(bot):
	bot.add_cog(Bank(bot))