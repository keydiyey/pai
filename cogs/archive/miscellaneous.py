import discord #upm package(py-cord)
import random
import asyncio
import requests
import json

from datetime import datetime, timedelta
from responses import responses

from discord.ext import commands

numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣",
		   "6⃣", "7⃣", "8⃣", "9⃣", "🔟")

class Miscellaneous(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


#----------- commands
	

	@commands.command()
	async def say(self, ctx, *, message):
		try:
			await ctx.message.delete()
			await ctx.send(message)
		except Exception as e:
			print(f"\n{e}")

	@commands.command()
	async def drink(self, ctx, user : discord.Member):

		try:
			await ctx.message.delete()
			embed = discord.Embed(
					color=discord.Color.green()
					)
			embed.add_field(name="Water Reminder!", value=f"Please drink water {user.mention}.")
			
		except Exception as e:
			print(f"\n{e}")

		await ctx.send(embed=embed)


	@commands.command(aliases=["?"])
	async def CallPai(self, ctx):
		user = ctx.author
		try:
			await ctx.send(responses.paiRes(user))
		except Exception as e:
			print(f"\n{e}")

	@commands.slash_command(name = "ppmeter", description = "pp how long?", guild_ids = [803432151097147444])
	async def ppmeter(self, ctx, user : discord.Member):
		p = random.randint(0,15)
		d = "8"+ "="*p + "D"
		try:
			if p < 1:
				m = f"{user.mention} no pp kekw \n" + d
		
			elif 0<p<5:
				m = f"{user.mention} small pp \n" + d
				
			elif 0<p<5:
				m = f"{user.mention} small pp \n" + d      

			else:
				m = f"{user.mention} big pp \n" + d

			await ctx.send(m)
		except Exception as e:
			print(f"\n {e}")

	@commands.slash_command(name="ship", description="Check your compatibility!", guild_ids = [803432151097147444])
	async def ship(self, ctx, user: discord.Member = None, member: discord.Member = None):
		
		p = random.randint(0,100)

		if p == 0:
			emoji = "💀"
		elif 1 < p < 25:
			emoji = "🤡"
		elif 26 < p < 50:
			emoji = "💔"
		elif 51 < p < 75:
			emoji = "💓"
		elif 76 < p < 99:
			emoji = "💕"
		elif p == 100:
			emoji = " **Soulmates** 💖"			

		if user == None:
			description = f"**You and I are {p} % compatible**. {emoji}"
		elif user == self.bot:
			description = f"**You and I are {p} % compatible.** {emoji}"
		elif user == ctx.author and member == None:
			description = "**How sad...** 😟"
		elif user == ctx.author and member == ctx.author:
			description = "**How sad...** 😟"
		elif member == None:
			description = f"**You and {user.mention} are {p} % compatible.** {emoji}"
		else:
			description = f"**{user.mention} and {member.mention} are {p} % compatible.** {emoji}"

		embed = discord.Embed(description = description, color = 0xf5e2e4)
		await ctx.respond(embed = embed)

	@commands.slash_command(name="howgay", description="Check your gayness!", guild_ids = [803432151097147444])
	async def howgay(self, ctx, user: discord.Member):
		try:
			p = random.randint(0,100)
			await ctx.respond(f"{user.mention} is " + str(p) + "%" + " gay.")

		except Exception as e:
			await ctx.send(e)

	@commands.command(aliases = ['f', 'F'])
	async def frespects(self, ctx, *, arg):
		try:
			await ctx.message.delete()
			c = await ctx.send(f'Press :regional_indicator_f: to pay respects for {arg}.')
			await c.add_reaction("🇫")
		except Exception as e:
			print(f"\n{e}")

	@commands.cooldown(1, 7, commands.BucketType.user)
	@commands.command()
	async def joke(self, ctx):
		r = requests.get("https://v2.jokeapi.dev/joke/Any")
		jokes = json.loads(r.content)

		try:
			url = jokes['joke']
			await ctx.send(url)

		except KeyError:
			url = jokes['setup']
			ans = jokes['delivery']
			await ctx.send(url)
			await asyncio.sleep(random.randint(3,5))
			await ctx.send(ans)

	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command(name = "8b")
	async def eightball(self, ctx, *, arg):

		wait = [
				"Dialing God....",
				"Asking Satan....",
				"Checking Google for answers...",
				"Asking your mom lmao...",
				"Posting on r/askreddit...",
				"Asking on Quora...",
				"Dialing your ex lmao..."
			]

		msg = await ctx.send(wait[random.randint(0,3)])
		
		with open("data/eightball.json", "r") as eb:
			responses = json.load(eb)

		n = random.randint(0, len(responses) - 1)
		message = responses[n]

		await asyncio.sleep(random.randint(1,3))

		await msg.edit(content = f"🎱 | {message}")

	@commands.command()
	async def inspireme(self, ctx):
		url = "http://inspirobot.me/api?generate=true"
		response = requests.get(url)

		if response.status_code == 200:
			url = response.content.decode('utf-8')
			embed = discord.Embed(description =f"Inspirational message for {ctx.author.mention}.")
			embed.set_image(url = url)
			await ctx.send(embed = embed)

		else:
			return await ctx.send("Encountered an error while fetching url.")

	@commands.command(aliases = ["ub", "dict", "define"])
	async def urban(self, ctx, *, term):
		url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

		querystring = {"term":str(term)}

		headers = {
			'x-rapidapi-key': "8ae5707b06mshd3a284cf6a5bc48p126f27jsne7c61f58303f",
			'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
			}

		response = requests.request("GET", url, headers=headers, params=querystring)

		a = json.loads(response.content)

		ll = len(a["list"])

		n = random.randint(0, ll-1)
		word = a["list"][n]["word"]
		definition = a["list"][n]["definition"]
		example =  a["list"][n]["example"]
		
		embed = discord.Embed(title = f"{word}", description = definition, color = 0x80cebe)
		embed.add_field(name = "Example" , value = example)

		await ctx.send(embed = embed)


	@commands.command()
	async def box(self, ctx):
		with open("data/fortune.json", "r") as winfo:
			fortunes = json.load(winfo)

		random.shuffle(fortunes["fortune"])

		n = random.randint(0, len(fortunes["fortune"])-1)

		fortune = fortunes["fortune"][n]


		msg = await ctx.send(".")
		for n in range(3):
			await asyncio.sleep(1)
			await msg.edit(content = ".        ＿＿＿＿\n     /       /        / |\n    |￣￣￣￣|   |\n    |＿＿＿＿| /")
			await asyncio.sleep(1)

			if n == 2:
				await msg.edit(content = f"**{fortune}**\n        ∧＿∧＿＿\n  ／(´･ω･`)   /  \ \n／|￣￣￣￣|\ /\n    |＿＿＿＿|／")
			else:	
				await msg.edit(content = f".\n        ∧＿∧＿＿\n  ／(´･ω･`)   /  \ \n／|￣￣￣￣|\ /\n    |＿＿＿＿|／")


def setup(bot):
	bot.add_cog(Miscellaneous(bot))
	