import discord #upm package(py-cord)
import random
import time
import json
import asyncio
import paiconomy as pc
import mafiaSetup as ms

from aiohttp import ClientSession
from discord.ext import tasks, commands
from discord.commands import SlashCommandGroup


class Premium(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	premium = SlashCommandGroup("premium", "Pay to have temporary admin powers!")
	change = premium.create_subgroup("change", "Changing server attributes")

	@premium.command(name = "prices", description = "Pay2Win! Server Commands.")
	async def prices(self, ctx:discord.ApplicationContext):

	
		embed = discord.Embed(title = "Premium Shop", color = 0xff8c69)
		embed.add_field(name="Change Server Name", value="`5000 ◉`", inline=True)
		embed.add_field(name="Change Server Icon", value="`10000 ◉`", inline=True)
		embed.add_field(name="Replace Emote", value="`500 ◉`", inline=False)
		file = await pc.localImage(embed, "\cogs\img\cart.png")
		return await ctx.respond(file = file, embed = embed)

	@change.command(name="name",description="Change the server name!")
	async def name(self, ctx:discord.ApplicationContext, name):
		user = ctx.author
		guild = ctx.guild
		trader = discord.utils.get(guild.roles, name = "Trader")

		price = 5000
		credits = pc.GetCredits(user)
		if credits >= price:
			pc.pay(user, price)
			await user.add_roles(trader)		
			await ctx.guild.edit(name=name)
			await user.remove_roles(trader)
			embed = discord.Embed(description =  f"Server name has been changed to **{name}**!", color = 0xf5e2e4)
			return await ctx.respond(embed = embed)

		else:
			return await pc.poorError(ctx)
		
	@change.command(name="icon", description="Change the server icon!")
	async def icon(self, ctx:discord.ApplicationContext):
		user = ctx.author
		guild = ctx.guild
		trader = discord.utils.get(guild.roles, name = "Trader")

		price = 10000
		credits = pc.GetCredits(user)
		
		if price <= credits:

			embed = discord.Embed(description =  f"Send an image!", color = 0xf5e2e4)
			await ctx.respond(embed = embed)
			msg = await self.bot.wait_for("message", check=None, timeout=20.0)
			attachment = msg.attachments[0]

			if attachment.filename.endswith(('.jpg','.png','.jpeg')):
				icon = attachment.url
				async with ClientSession() as session:
					async with session.get(icon) as response:
						if response.status == 200:
							icon_data = await response.read()
							pc.take(user, price) #paying tribute
							await user.add_roles(trader)		   #add permissions to enable server edit
							await ctx.guild.edit(icon = icon_data)  #editing server icon
							await user.remove_roles(trader)        #removing permissions
							

							#------- confirmation that image has been changed -------
							embed = discord.Embed(description =  f"Server icon has been successfully changed by **{user.nick}**!", color = 0xf5e2e4)
							await msg.respond(embed = embed)
						else:
							await pc.generalError(ctx)
			else:
				await pc.generalError(ctx)
		else:
			await pc.poorError(ctx)
	

	
				

def setup(bot):
	bot.add_cog(Premium(bot))

