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
				embed = discord.Embed(
						description=f"Please welcome **{member.display_name}** to society. 🙇🏻‍♂️", 
						color=0xffd9cc)
				await ctx.send(embed = embed)

		except Exception as e:
			print(e)
		finally:
			return	
		
	@commands.Cog.listener()
	async def on_message(self,message: discord.Message):
		message_list = message.content.split()
		member = message.author
		timeout = randint(20,120)
		
		if len(message_list) > 2:
			inmate = discord.utils.get(member.guild.roles, name = "Inmate")
			deceased = discord.utils.get(member.guild.roles, name = "Deceased")

			chance = 6	
			kill_list = ["crush",
						"ass",
						"backshots",
						"bark",
						"basement",
						"bottom",
						"crush",
						"feet",
						"heat",
						"hihi",
						"meow",
						"symphony",
						"toes",
						"touch",
						"victim",
						"yearn"] 

			
			# Make sure we won't be replying to ourselves.
			if message.author.id == self.bot.user.id:
				return

			if any(word in kill_list for word in message_list):

				# ① Check if member is jailed or dead
				if any(role in member.roles for role in [inmate, deceased]):
					return
					
				# ① Gacha time for victim
				if randint(0,100) <= chance: #percent success

					timeout = randint(20,120)
					description = f" **{member.display_name} has been assassinated for speaking the truth! `{timeout} sec`**"
					embed = discord.Embed(title = "🚨", description=description, color=0xffd9cc)
					await message.reply(embed = embed)

					# role adding here
					try:
						return await self.punishment(ctx = message, member = member, role = deceased, timeout = timeout)
					except Exception as e:
						print(e)

		elif message_list.count("meow") > 5:
			message.delete()
			return await self.punishment(ctx = message, member = member, role = deceased, timeout = timeout)

		

def setup(bot):
	bot.add_cog(Listeners(bot))