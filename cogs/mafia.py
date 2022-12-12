import discord #upm package(py-cord)
import asyncio

import paiconomy as pc
import mafiaSetup as ms

from discord.ext import tasks, commands

#------------------- Commands ----------------------
class Mafia(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.cooldown(1, 30, commands.BucketType.user)
	@commands.has_role('Civilian')
	@commands.command()
	async def jail(self, ctx, member: discord.Member = None):
		user = ctx.author
		guild = ctx.guild
	
		emote = ms.url("fbi")
		status = ms.Status(user, member, guild)
		killPerm, prisonPerm, killable = await status.CheckPermissions()

		if member == None or member == user:
			culprit = user
			embed = status.Description("actions", "TurnSelfIn", emote, culprit.nick)
		else:
			if prisonPerm == True:
				if ms.chance() == True:
					culprit = member
					victim = user
					embed = status.Description("actions", "CallPolice", emote, culprit.nick, victim.nick)
				else:
					culprit = user
					victim = member
					embed = status.Description("events", "FalseAccusations", emote, culprit.nick, victim.nick)
			else:
				await ctx.send("You do not have the permissions to do that for now.")
		
		await ctx.send(embed = embed)
		await status.ChangeToPrisoner(culprit)
		return await ctx.send(embed = status.Description("events", "JailTimeDone",culprit = culprit.nick))

	@commands.has_role('Civilian' or 'Prisoner')
	@commands.command()
	async def shoot(self, ctx, member: discord.Member = None):

		user = ctx.author
		guild = ctx.guild
	
		emote = ms.url("kill")
		status = ms.Status(user, member, guild)
		killPerm, prisonPerm, killable = await status.CheckPermissions()

		culprit = user
		victim = member

		if member == None or member == user:
			embed = status.Description("actions", "Sewercide", emote, culprit.nick)
		else:
			if killPerm == True: #checks if user can kill
				if ms.chancePercent(495) == True: #if kill is successful
					embed = status.Description("actions", "Kill", emote, culprit.nick, victim.nick)
					await ctx.send(embed = embed)
					await status.ChangeToDead(victim)
					return await ctx.send(embed = status.Description("events", "Resurrected",culprit = victim.nick))
					
				else: #if kill unsuccessfull
					embed = status.Description("events", "FailedMurder",culprit =  culprit.nick, victim = victim.nick)
					await ctx.send(embed = embed)
					return await status.jailChance(ctx, culprit)
			else:
				await ctx.send("You do not have the permissions to do that for now.")

#------------------ Bail
	@commands.command()
	async def bail(self, ctx, prisoner: discord.Member = None):
		user = ctx.author
		status = ms.Status(user, prisoner, guild)
		
		if pc.checkPoor(self, user, amount) == True:
			return await pc.poorError(ctx)

		if member == None or member == user:
			culprit = user
			await status.bailed(user, prisoner, amount)
		else:
			await status.bailed(user, prisoner, amount)

		return await pc.qEmbed(ctx, f"{prisoner.nick} has been bailed.")

	@commands.has_role('Civilian')
	@commands.command()
	async def ressurect(self, ctx, dead: discord.Member = None):
		user = ctx.author
		status = ms.Status(user, dead, guild)
		
		if pc.checkPoor(self, user, amount) == True:
			return await pc.poorError(ctx)

		if member == None or member == user:
			dead = user
			await status.bailed(user, dead, amount)
		else:
			await status.bailed(user, dead, amount)

		return await pc.qEmbed(ctx, f"{dead.nick} has been ressurected.")
			


def setup(bot):
	bot.add_cog(Mafia(bot))
