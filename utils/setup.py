import discord #upm package(py-cord)
import asyncio


class Role:
	# Initializes individual role permissions
	def __init__(self, name, guild, can_kill = True, can_jail = True, is_killable = True, is_imprisonable = True):
		self.role = discord.utils.get(guild.roles, name = name)

		# [Permissions]
		self.can_kill = can_kill
		self.can_jail = can_jail
		self.is_killable = is_killable
		self.is_imprisonable = is_imprisonable

	async def penalty(self, user, timeout):

		await user.add_roles(self.role)

		# waiting for timeout
		await asyncio.sleep(timeout)

		if self.role in self.user.roles:		
			await user.remove_roles(self.role)
			embed = discord.Embed(description = f"**{user}** has finished serving their sentence.🏳", color = 0xf5e2e4)
			

		return embed



		
