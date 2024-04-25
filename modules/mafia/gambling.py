import discord #upm package(py-cord)
from random import randint
import json
import asyncio
import modules.data_management as pc
import modules.mafiaSetup as ms

from discord.ext import tasks, commands

class Gambling(commands.Cog):
	def __init__(self, bot):
		
		self.bot = bot

	gambling = SlashCommandGroup("gambling", "A place to spend your credits!")
#-------------------------------------------------------------------------------
	@gambling.command(name = "aon", description = "All or Nothing.")
	async def allornothing(self, ctx, multiplier:int):
		user = ctx.author
		credits = pc.getCredits(userID)

		if credits <= 0:
			return await pc.poorError(ctx)   #check if poor
		
		bet = credits
		pc.take(user, bet)
		msg = await pc.qEmbed(ctx, "You bet all your credits...")
		
		msg.delete()
		outcome = randint(0, multiplier + 2)

		await asyncio.sleep(3)

		if outcome == 0:
			await ctx.send(" =^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^= \n")
			await ctx.send(".☆彡(ノ^ ^)ノ **CONGRATULATIONS** ヘ(^ ^ヘ)☆彡\n")

			await ctx.send(".                        ⚅  J A C K P O T  ⚅          ")
			
			bet *= multiplier

			pc.pay(user, bet)

			return await pc.qEmbed(ctx, f"💳 **| You won a total of {bet} credits.**")
			
		else:
			return await pc.qEmbed(ctx, "Nothing happens. You lost **all** your credits thanks to your gambling addiction.")
		
		
	@gambling.command(name = "coinflip", description = "Toss a coin.")
	async def coinflip(self, ctx, bet:int):
		user = ctx.author
		credits = pc.getCredits(user)
		if bet > credits:
			return await pc.poorError(ctx)
		elif bet >= 250:
			return await pc.qEmbed(ctx,"You cannot bet more than **250 credits** in coinflip.")
		else:
			msg = await ctx.send(" :coin: **| Tossing the coin...**")
			await asyncio.sleep(3)
			if pc.chancePercent(452) == False:
				pc.pay(user, bet)				
			else:
				pc.take(user, bet)
				await msg.edit(content = f" :coin: **| The coin landed upside down and you lost.**")		
			

def setup(bot):
	bot.add_cog(Gambling(bot))