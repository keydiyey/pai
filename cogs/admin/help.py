import discord #upm package(py-cord)
from discord.ext import commands



class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(name = "help", description = "Get some help.")
	async def help(self, ctx:discord.ApplicationContext):
		'''ephemeral = true'''
		embed = discord.Embed(color = 0xff8c69)
		embed.set_author(name = "Pai Commands List", icon_url = str(self.bot.user.avatar.url))
		embed.add_field(name="/Bank 🏦",
                value="Check profile or send money to another member.",
                inline=True)
		embed.add_field(name="/Fortune 🧧",
						value="Check your luck today!",
						inline=True)
		embed.add_field(name="/Rob 🦹‍♀️",
						value="Commit tomfoolery.",
						inline=True)
		return await ctx.respond(embed=embed, ephemeral = True)

	@commands.slash_command(name = "changelog", description = "What's New?")
	async def changelog(self, ctx:discord.ApplicationContext):
		embed = discord.Embed(title = 'Changelog Pai 2.0', description = "Since Discord will migrate from text commands to slash commands the bot needs to be updated. However, I accidentally deleted the original pai source code so I am doing everything from a backup. Anyways....", color = 0xff8c69)
		embed.add_field(name="Premium shop added!", value="Ever wanted to do a little trolling? Now you can. In exchange for credits you can spice up the server in ways you like. Add roles to yourself or mute a member, etc!", inline=False)
		embed.add_field(name="Reputation and Murder(Mafia) dlc", value="Kill or be killed. Call the police when you witness a murder. Just know that the odds are against your favor.", inline=False)
		embed.add_field(name="Fortune", value="Genshin Impact's bamboo fortune telling slip is now here! Check it at /fortune.", inline=False)
		embed.add_field(name="Other updates...", value="Slowly migrating to slash commands. We added buttons too. Soon we will add your mom.", inline=False)
		return await ctx.respond(embed=embed)


def setup(bot):
	bot.add_cog(Help(bot))
	
	