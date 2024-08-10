
import discord 
from discord import option
from discord.ext import tasks, commands
import utils.transactions as transactions
from random import randint

from modules.setup import Role




prob_rob = 0.234
prob_jail = 0.15

class Crimes(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

#-------------------------------------------------------------------------------
	
	@commands.cooldown(1, 30, commands.BucketType.user)
	@commands.slash_command(name = "rob", description = "rob another member!")
	@option("member", description="Enter someone's name", required=True)
	async def rob(self, ctx:discord.ApplicationContext, member: discord.Member):
		guild = ctx.guild
		user = ctx.author
		user_id = user.id
		member_id = member.id

		inmate = Role(name = "Inmate",  guild = guild, can_kill = False, can_jail = False, is_imprisonable = False)
		deceased = Role(name = "Deceased",  guild = guild, can_jail = False, is_killable = False, is_imprisonable = False)

		if randint(0,100) <= prob_rob: #percent success
			# transfering credits
			transactions.transfer_credits(member_id, user_id, permax = randint(0.1,1))
			description = f"💰 | Successfully robbed {member.nick}!"
		else:
			description = f" ❌ | You failed to rob {member.nick}"
			

		# Jail time chance
		if randint(0,100) <= prob_jail: #percent success
			description = description + f" **However, {user.nick} has been caught!**"
			await ctx.respond(embed = embed)
		
			embed = inmate.penalty(user, randint(20,120))

		else:
			description = description + f" **However, {user.nick} escaped!**"
			
        
		return await ctx.respond(embed = embed)

def setup(bot):
	bot.add_cog(Crimes(bot))
 
 
 
 