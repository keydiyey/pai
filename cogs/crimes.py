
import discord 
from discord import option
from discord.ext import commands

from random import randint
import asyncio
import json

from utils import imageutil

from punishment import Punishment


class Crimes(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
		self.probability = 23.4
		self.min_timeout = 20
		self.max_timeout = 120

		try:
			with open('config.json', 'r', encoding="utf-8") as data:
				config = json.load(data)

			self.guild = discord.utils.get(self.bot.guilds, name=config["guild"]["name"])
			self.inmate_role = discord.utils.get(self.guild.roles, name = "Inmate")
			self.deceased_role = discord.utils.get(self.guild.roles, name = "Deceased")
			self.role_list = [self.inmate_role, self.deceased_role]

		except Exception as e:
			print("Crimes Cogs Error : ", e)


	@commands.slash_command(name = "jail", description = "jail another member!")
	@commands.cooldown(1, 30, commands.BucketType.user)
	@option("member", description="Enter someone's name", required=True)
	async def jail(self, ctx:discord.ApplicationContext, member: discord.Member):

		user = ctx.user
		role_list = self.init_roles()
		inmate_role = role_list[0]
		
		description = f"The accusations were proven false. **{member.display_name}** will not be jailed!"
		footer_description = f"{user.display_name} has escaped!"

		jail = Punishment()
	
		# Check if user or member has any existing game roles 
		if any(role in user.roles for role in role_list) or any(role in member.roles for role in role_list):
			embed = discord.Embed(description=f"You or target member is already dead or in jail. Please try again later.", color=0xffd9cc)
			return await ctx.respond(embed = embed, ephemeral = True)
		

		x = randint(0,100)
		y = randint(0,100)

		tasks = []

		if x <= self.probability:
			description = f"**{member.display_name}** will now be jailed at 😳 **Horny Jail** 😳"
			tasks.append(asyncio.create_task(jail.execute(ctx = ctx, n = x, member = member, role = inmate_role)))

		if y <= self.probability:
			footer_description = f"{user.display_name} will be jailed at 😳 Horny Jail 😳 for false accusations."
			tasks.append(asyncio.create_task(jail.execute(ctx = ctx, n = y, member = user, role = inmate_role)))

		title = f"🚨 {user.display_name} has called the police on {member.display_name}! 🚨"

		embed = discord.Embed(
						title=title, 
						description=description, 
						color=0xffd9cc)
		embed.set_image(url = imageutil.get_jail_gif())
		embed.set_footer(text=footer_description)
		await ctx.respond(embed = embed)

		return await asyncio.gather(*tasks)  # Wait for both tasks to finish
		
def setup(bot):
	bot.add_cog(Crimes(bot))
 
 
 
 