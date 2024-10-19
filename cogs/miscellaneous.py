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
			setup = ""
			delivery = jokes['joke']

		finally:
			embed = discord.Embed(title = f"🤡 | {setup}", description= f"{delivery}", color=0xffd9cc)
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
		
	@commands.slash_command(name = "wait",description = "they dont love you like i love you" )
	async def wait(self, ctx):

		description_1 = r"""
						```
						✋🏻﹏﹏∧
						||~ω~｀ )
						/      ,✋🏻 
						(   ﹏  (
						`ヽ_) ヽ_)
						```
						"""
		
		description_2 = r"""
						```
						  ∧﹏﹏∧
    					 ( ・ω・ )
						 /    ♥ ,
						(   ﹏  (
						 ヽ_) ヽ_)
						```
						"""
		
		description_3 = r"""
				```
				     ∧﹏﹏∧
                    (・ω・  )
					, ♥     \
					 )  ﹏   )
					(_ノ  (_ノ
				```
				"""
		
		embed = discord.Embed(description = description_1, color=0xffd9cc)

		await ctx.response.defer()
		await ctx.respond(embed = embed)
		await asyncio.sleep(2)
		frames = [description_2, description_3]
		for i in range(3):
			for frame in frames:
				embed = discord.Embed(description = frame, color=0xffd9cc)
				await ctx.edit(embed=embed)
		
		return

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

def setup(bot):
	bot.add_cog(Miscellaneous(bot))
	