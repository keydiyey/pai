import discord #upm package(py-cord)
import json
import asyncio
import modules.paiconomy as pc

from random import randint
from discord.ext import tasks, commands

def url(emote):
	emotes = pc.read("data/roleplay.json")
	n = len(emotes[emote])
	i = randint(0, n - 1)
	url = emotes[emote][i]
	return url

def chance():
	x = randint(0, 3)
	y = randint(0, 3)
	if x == y:
		return True
	else: 
		return False

def chancePercent(GlobalChance):
	x = randint(0, 1000)
	if x > GlobalChance:
		return True
	else:
		return False


def statusTime():
	time = randint(15, 180)
	return time

class Setup():
	def __init__(self, prisonerRole, deadRole, civilianRole):
		self.prisonerRole = prisonerRole
		self.deadRole = deadRole
		self.civilianRole = civilianRole

	async def CreateRole(self, guild, name, color):
		role = await guild.create_role(name=name, color=color, mentionable=False)
		return
	
	async def CreateChannel(self):
		channel = await guild.create_text_channel()
		return

class Status():
	def __init__(self, user, member, guild):
		self.user = user
		self.member = member
		self.guild = guild
		self.statusTime = statusTime()
		self.prisonerRole = discord.utils.get(self.guild.roles, name = "Prisoner")
		self.deadRole = discord.utils.get(self.guild.roles, name = "Dead")
		self.civilianRole = discord.utils.get(self.guild.roles, name = "Civilian")

	def Description(self, type, title, emote = discord.embeds.EmptyEmbed, culprit = None, victim = None):
		with open("data/GlobalEvents.json", encoding = "utf8") as je:
			data = json.load(je)
		text = data[type][title]

		embed = discord.Embed(description = text.format(culprit = culprit, victim = victim), color = discord.Colour.random())
		embed.set_image(url = emote)
		return embed
	
	

	async def CheckPermissions(self):
		if self.deadRole in self.user.roles:
			killPerm = True
			prisonPerm = False
			killable = False
		elif self.prisonerRole in self.user.roles:
			killPerm = False
			prisonPerm = True
			killable = True
		else:
			killPerm = True
			prisonPerm = True
			killable = True
	
		return killPerm, prisonPerm, killable

	async def ChangeStatus(self, user, role_added, role_removed):
		await user.add_roles(role_added)		
		await user.remove_roles(role_removed)
		await asyncio.sleep(self.statusTime)
		if role_added in self.user.roles:
			await user.add_roles(role_removed)		
			await user.remove_roles(role_added)
		else:
			pass
		return

	async def ChangeToPrisoner(self, culprit):
		await self.ChangeStatus(culprit, self.prisonerRole, self.civilianRole)
		return
	
	async def ChangeToDead(self, victim):
		await self.ChangeStatus(victim, self.deadRole, self.civilianRole)
		return

	async def bailed(self, user, prisoner, amount):
		if self.deadRole in self.prisoner.roles:
			return

		pc.take(user, amount)
		await culprit.remove_roles(self.prisonerRole)
		await culprit.add_roles(self.civilianRole)		
		return	

	async def resurrection(self, user, culprit, amount):
		if self.deadRole in self.user.roles:
			return

		pc.take(user, amount)
		await culprit.remove_roles(self.deadRole)
		await culprit.add_roles(self.civilianRole)		
		return
		
	async def jailChance(self, ctx, culprit):
			if chance() == True: #chances that a user will get jailed
				embed = self.Description("events", "Caught",culprit = culprit.nick)
				await ctx.send(embed = embed)
				await self.ChangeToPrisoner(culprit)
				return await ctx.send(embed = self.Description("events", "JailTimeDone",culprit = culprit.nick))
			else:
				embed = self.Description("events", "Escaped",culprit = culprit.nick)
				return await ctx.send(embed = embed)

		
