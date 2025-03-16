import discord
import asyncio
from random import randint

class Punishment:
	def __init__(self, role):
		self.role = role
		self.probability = 0.128
		self.min_timeout = 30
		self.max_timeout = 180

	async def execute(self, interaction, n, member):
		if n <= self.probability:
			try:
				# add punishment role
				await member.add_roles(self.role)
				
				# waiting for timeout
				await asyncio.sleep(randint(self.min_timeout, self.max_timeout))

				# remove role
				await member.remove_roles(self.role)

				# alert members
				embed = discord.Embed(
						description=f"Please welcome **{member.display_name}** to society. 🙇🏻‍♂️", 
						color=0xffd9cc)
				await interaction.respond(embed = embed)
			
			except Exception as e:
				return print(e)
		else:
			return





		