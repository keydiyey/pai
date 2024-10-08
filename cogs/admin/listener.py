import discord #upm package(py-cord)
import asyncio

from random import randint
from discord.ext import commands

class Listeners(commands.Cog):
	def __init__(self, bot):
		
		self.bot = bot

	async def punishment(self, ctx, member, role, timeout):
		
		# role adding here
		try:

			await member.add_roles(role)

			# waiting for timeout
			await asyncio.sleep(timeout)

			if role in member.roles:		
				await member.remove_roles(role)
		except Exception as e:
			print(e)
		finally:
			return	
		
	@commands.Cog.listener()
	async def on_message(self,message: discord.Message):
		if len(message.split())
		member = message.author
		timeout = randint(20,120)

		inmate = discord.utils.get(member.guild.roles, name = "Inmate")
		deceased = discord.utils.get(member.guild.roles, name = "Deceased")

		chance = 6	
		kill_list = ["crush",
			   		"ass",
					"backshots",
					"bottom",
					"yearn",
					"hihi",
					"touch",
					"feet",
					"toes",
					"meow",
					"bark",
					"basement",
					"greatest",
					"symphony",
					"yearn"] 

		
		 # Make sure we won't be replying to ourselves.
		if message.author.id == self.bot.user.id:
			return

		if any(word in kill_list for word in message.content.split()):

			# ① Check if member is jailed or dead
			if any(role in member.roles for role in [inmate, deceased]):
				embed = discord.Embed(description=f"{member.display_name} is either in jail or dead. Please try again later.", color=0xffd9cc)
				return await message.reply(embed = embed, ephemeral = True)

			# ① Gacha time for victim
			if randint(0,100) <= chance: #percent success

				timeout = randint(20,120)
				description = f" **{member.display_name} has been assassinated for speaking the truth! `{timeout} sec`**"
				embed = discord.Embed(title = "🚨", description=description, color=0xffd9cc)
				await message.reply(embed = embed)

				# role adding here
				try:
					await self.punishment(ctx = message, member = member, role = deceased, timeout = timeout)
				except Exception as e:
					print(e)
				else:
					embed = discord.Embed(title = "🚨",description = f"**{member}** has been resurrected.🏳", color = 0xf5e2e4)
					await message.reply(embed = embed)

def setup(bot):
	bot.add_cog(Listeners(bot))