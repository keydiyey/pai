import discord #upm package(py-cord)
import random
import asyncio
import requests
import json

from discord.ext import commands

class Miscellaneous(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


#----------- commands
	
	
	@commands.slash_command(name = "ppmeter", description = "pp how long?")
	async def ppmeter(self, ctx, user : discord.Member):
		p = random.randint(0,15)
		dick = "8"+ "="*p + "D"
		
		embed = discord.Embed(title = f"{user.display_name}'s PP", description= f"{dick}", color=0xffd9cc)
		
		return await ctx.respond(embed = embed)

	@commands.slash_command(name="joke", description="gets a joke ig?")
	async def joke(self, ctx):
		r = requests.get("https://v2.jokeapi.dev/joke/Any")
		jokes = json.loads(r.content)

		try:
			setup = jokes['setup']
			delivery = jokes['delivery']
		except KeyError as e:
			setup = None
			delivery = jokes['joke']

		finally:
			embed = discord.Embed(title = setup, description= f"🤡 | {delivery}", color=0xffd9cc)
			await ctx.respond(embed = embed)
			
		


	@commands.slash_command(name="8b", description="eight ball!")
	async def eightball(self, ctx, *, question):		
		with open("./assets/data/eightball.json", "r") as eb:
			responses = json.load(eb)

		n = random.randint(0, len(responses) - 1)
		message = responses[n]

		await asyncio.sleep(random.randint(1,3))

		embed = discord.Embed(title = question, description= f"🎱 | {message}", color=0xffd9cc)
		
		await ctx.respond(embed = embed)


	@commands.slash_command(name = "inspire", description = "generate inspirational messages!")
	async def inspire(self, ctx):
		url = "http://inspirobot.me/api?generate=true"
		response = requests.get(url)

		if response.status_code == 200:
			url = response.content.decode('utf-8')
			embed = discord.Embed(description =f"Inspirational message for **{ctx.author.mention}**.", color=0xffd9cc)
			embed.set_image(url = url)
			await ctx.respond(embed = embed)

		else:
			embed = discord.Embed(description =f"Encountered an error while fetching url.", color=0xffd9cc)
			return await ctx.send(embed = embed)

	@commands.slash_command(name = "urban",description = "uhh dick shawn awry" )
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

		await ctx.respond(embed = embed)


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
	