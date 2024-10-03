
import discord 
from discord import option
from discord.ext import commands

from random import randint
import asyncio
import json


import utils.transactions as transactions

# Known Bugs and Status
# ✅ adding of roles for punishment
# ✅ pre-checking of roles 
# ✅ removal of roles for punishment
# ✅ double response?
# ✅ cooldown doesnt work too damn
# ✅ cooldown error message
		

class Crimes(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.probability = 0.234
		self.min_timeout = 20
		self.max_timeout = 120

	async def quick_embed(self, ctx, description, url = None):
		embed = discord.Embed(title = "🚨 ALERT 🚨", description = description, url=url, color=0xffd9cc)
		embed.set_thumbnail(url = ctx.user.display_avatar.url)
		return await ctx.send(embed = embed)

	async def image(self, event):
		with open("/assets/data/gifs.json" , "r") as file:
			data = json.load(file)
			n = randint(0,len(data[event]))
			url = data[event][n]

		return url

	async def error_embed(self, ctx):
		embed = discord.Embed(title="⚠ | Error ", description="There has been a problem with this command.", color=0x00ff00)
		return await ctx.send(embed = embed, ephemeral = True)


	async def punishment(self, ctx, member, role, timeout):
		
		# role adding here
		try:

			await member.add_roles(role)

			# waiting for timeout
			await asyncio.sleep(timeout)

			if role in member.roles:		
				await member.remove_roles(role)
			else:
				return await self.error_embed(ctx)
			
		except Exception:
			return
		finally:
			return
		

	@commands.slash_command(name = "jail", description = "jail another member!")
	@commands.cooldown(1, 30, commands.BucketType.user)
	@option("member", description="Enter someone's name", required=True)
	async def jail(self, ctx:discord.ApplicationContext, member: discord.Member):
		
		user = ctx.user

		inmate = discord.utils.get(member.guild.roles, name = "Inmate")
		deceased = discord.utils.get(member.guild.roles, name = "Deceased")

		title = f"{user.display_name} has called the police on {member.user}!"
		
		# ①Check if user has roles 
		if any(role in user.roles for role in [inmate, deceased]) or any(role in member.roles for role in [inmate, deceased]):
			embed = discord.Embed(description=f"You or target member is already dead or in jail. Please try again later.", color=0xffd9cc)
			return await ctx.respond(embed = embed, ephemeral = True)

		
		# ① Gacha time
		if randint(0,1) <= self.probability: #percent success of jailing another member
			try:
				await self.punishment(ctx = ctx, member = member, role = inmate)
			except Exception:
				return await self.error_embed(ctx)
		else:
			description = f"**{member.display_name} escaped!**"

		# ① Gacha time for jailing murderer
		if randint(0,1) <= self.probability: #percent success of 
			timeout = randint(20,120)
			description = f" **{user.display_name} has been caught for false accusations against {member.display_name} and will be put in jail for `{timeout}` seconds!**"

			# role adding here
			try:
				await self.punishment(ctx = ctx, member = user, role = inmate, timeout = timeout)
			except Exception:
				return
			else:
				embed = discord.Embed(title = "🚨",description = f"**{user}** has finished serving their sentence.🏳", color = 0xf5e2e4)
				return await ctx.send(embed = embed)

		else:
			description = f"**{user.display_name} escaped!**"
			embed = discord.Embed(description=description, color=0x00ff00)
			return await ctx.send(embed = embed)

	@commands.slash_command(name = "kill", description = "murder another member!")
	@commands.cooldown(1, 30, commands.BucketType.user)
	@option("member", description="Enter someone's name", required=True)
	async def kill(self, ctx:discord.ApplicationContext, member: discord.Member):

		inmate = discord.utils.get(member.guild.roles, name = "Inmate")
		deceased = discord.utils.get(member.guild.roles, name = "Deceased")
		
		
		# ① Check if member is jailed or dead
		if any(role in member.roles for role in [inmate, deceased]):
			embed = discord.Embed(description=f"{member.display_name} is either in jail or dead. Please try again later.", color=0xffd9cc)
			return await ctx.respond(embed = embed, ephemeral = True)

		# ① Gacha time for victim
		if randint(0,1) <= self.probability: #percent success
			timeout = randint(20,120)
			description = f" **{member.display_name} has been murdered! `{timeout} sec`**"
			embed = discord.Embed(title = "🚨", description=description, color=0xffd9cc)
			await ctx.respond(embed = embed)

			# role adding here
			try:
				await self.punishment(ctx = ctx, member = member, role = deceased, timeout = timeout)
			except Exception:
				return await self.error_embed(ctx)
			else:
				embed = discord.Embed(title = "🚨",description = f"**{member}** has been resurrected.🏳", color = 0xf5e2e4)
				await ctx.send(embed = embed)

		# ① Gacha time for jailing murderer
		# ① Check if user is jailed or dead
		user = ctx.user
		if any(role in user.roles for role in [inmate, deceased]):
			embed = discord.Embed(description=f"{user.display_name} is either in jail or dead. Please try again later.", color=0xffd9cc)
			return await ctx.respond(embed = embed, ephemeral = True)

		if randint(0,1) <= self.probability: #percent success
			timeout = randint(20,120)
			description = f" **{user.display_name} has been caught for trying to murder {member.display_name} and will be put in jail for `{timeout}` seconds!**"
			embed = discord.Embed(title = "🚨", description=description, color=0xffd9cc)
			await ctx.respond(embed = embed)

			# role adding here
			try:
				await self.punishment(ctx = ctx, member = user, role = inmate, timeout = timeout)
			except Exception:
				return await self.error_embed(ctx)
			else:
				embed = discord.Embed(title = "🚨",description = f"**{user}** has finished serving their sentence.🏳", color = 0xf5e2e4)
				return await ctx.send(embed = embed)

		else:
			description = f"**{user.display_name} escaped!**"
			embed = discord.Embed(description=description, color=0x00ff00)
			return await ctx.send(embed = embed)
		

	

		
def setup(bot):
	bot.add_cog(Crimes(bot))
 
 
 
 