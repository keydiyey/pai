
# Discord Packages
import discord 
from discord.ext import tasks, commands

import modules.transactions as transaction


name = { "en":"Momiji Bank", "jp":"紅葉銀行"}


class amount_modal(discord.ui.View):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.add_item(discord.ui.InputText(label="Short Input"))

	async def callback(self, interaction: discord.Interaction):
		amount = self.children[0].value
		return await amount


class bank_buttons(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
	@discord.ui.button(label="Deposit", style=discord.ButtonStyle.success, emoji="➕") 
	async def deposit_callback(self, button, interaction):
		user = interaction.user
		modal = amount_modal(title="Modal via Slash Command")
		amount = await interaction.send_modal(modal)
		transaction.deposit(user.id, amount)
		await interaction.response.send_modal(amount_modal(title="Modal via Button"))
	
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

		file = discord.File("./assets/images/bank.png", filename="image.png")
		embed.set_image(url="attachment://image.png")



		await ctx.respond(embed = embed, file=file, view=bank_buttons())


	
		
	  


def setup(bot):
	bot.add_cog(Bank(bot))