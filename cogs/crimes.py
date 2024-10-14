
import discord 
from discord import option
from discord.ext import commands

from random import randint
import asyncio
import json

from utils import imageutil


# Known Bugs and Status
# ✅ adding of roles for punishment
# ✅ pre-checking of roles 
# ✅ removal of roles for punishment
# ✅ double response?
# ✅ cooldown doesnt work too damn
# ✅ cooldown error message
# ⬜ integration doesnt work?

class Crimes(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
		self.probability = 23.4
		self.min_timeout = 20
		self.max_timeout = 120

	def init_roles(self):
		try:
			with open('config.json', 'r', encoding="utf-8") as data:
				config = json.load(data)

			guild = discord.utils.get(self.bot.guilds, name=config["guild"]["name"])
			inmate_role = discord.utils.get(guild.roles, name = "Inmate")
			deceased_role = discord.utils.get(guild.roles, name = "Deceased")
			role_list = [inmate_role, deceased_role]

			return inmate_role, deceased_role, role_list 

		except Exception as e:
			print("Crimes Cogs Error : ", e)

	async def punishment(self, ctx, n, member, role):

		if n <= self.probability:
			try:
				await member.add_roles(role)
				
				# waiting for timeout
				await asyncio.sleep(randint(self.min_timeout, self.max_timeout))

				await member.remove_roles(role)
				embed = discord.Embed(
						description=f"Please welcome **{member.display_name}** to society. 🙇🏻‍♂️", 
						color=0xffd9cc)
				await ctx.send(embed = embed)
				
			except Exception as e:
				return print(e)
		else:
			return


	@commands.slash_command(name = "jail", description = "jail another member!")
	@commands.cooldown(1, 30, commands.BucketType.user)
	@option("member", description="Enter someone's name", required=True)
	async def jail(self, ctx:discord.ApplicationContext, member: discord.Member):
		
		user = ctx.user
		inmate_role, deceased_role, role_list = self.init_roles()
		description = f"The accusations were proven false. **{member.display_name}** will not be jailed!"
		footer_description = f"{user.display_name} has escaped!"
	
		# ①Check if user has roles 
		if any(role in user.roles for role in role_list) or any(role in member.roles for role in role_list):
			embed = discord.Embed(description=f"You or target member is already dead or in jail. Please try again later.", color=0xffd9cc)
			return await ctx.respond(embed = embed, ephemeral = True)
		
		x = randint(0,100)
		y = randint(0,100)

		if x <= self.probability:
			description = f"**{member.display_name}** will now be jailed at 😳 **Horny Jail** 😳"
			
		if y <= self.probability:
			footer_description = f"{user.display_name} will be jailed at 😳 Horny Jail 😳 for false accusations."

		title = f"🚨 {user.display_name} has called the police on {member.display_name}! 🚨"

		embed = discord.Embed(
						title=title, 
						description=description, 
						color=0xffd9cc)
		embed.set_image(url = imageutil.get_jail_gif())
		embed.set_footer(text=footer_description)
		await ctx.respond(embed = embed)

		# ① Gacha time

		task_1 = asyncio.create_task(self.punishment(ctx = ctx, n = x, member = member, role = inmate_role))

		task_2 = asyncio.create_task(self.punishment(ctx = ctx, n = y, member = user, role = inmate_role))


		return await asyncio.gather(task_1, task_2)  # Wait for both tasks to finish
		
def setup(bot):
	bot.add_cog(Crimes(bot))
 
 
 
 