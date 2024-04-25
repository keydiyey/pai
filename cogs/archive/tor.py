import discord #upm package(py-cord)
import json
from random import randint
from discord.ext import tasks, commands



class QOTD(commands.Cog):
 
    def __init__(self, bot):
    
        self.bot = bot

    @commands.command()
    async def wyr(self, ctx):
        with open("data/qotd.json", "r") as qt:
            questions = json.load(qt)

        strings = questions['wyr']
        j = len(strings)
        i = randint(0, j - 1)
        
        embed = discord.Embed()
        embed.title = "Would you rather.."
        embed.description = str(strings[i])
        await ctx.send(embed=embed)

    @commands.command(aliases=["nhie"])
    async def neverhaveiever(self, ctx):
        with open("data/qotd.json", "r") as qt:
            questions = json.load(qt)

        strings = questions['nhie']
        j = len(strings)
        i = randint(0, j - 1)
        
        embed = discord.Embed()
        embed.title = "Never have I ever.."
        embed.description = strings[i]
        await ctx.send(embed=embed)

    @commands.command()
    async def truth(self, ctx, *, member: discord.Member):

        user = ctx.author

        # Get and pick random string
        with open("data/qotd.json", "r") as qt:
            questions = json.load(qt)

        strings = questions['truths']
        j = len(strings)
        i = randint(0, j - 1)

        k = len(ctx.guild.members)
        m = randint(0, k - 1)
        other = ctx.guild.members[m].mention

        embed = discord.Embed()
        embed.title = f"{user.name} asked {member.name}"
        embed.description = strings[i].format(name=other)
        await ctx.send(embed=embed)

    @commands.command()
    async def dare(self, ctx, *, member: discord.Member):         
        user = ctx.author

        with open("data/qotd.json", "r") as qt:
            questions = json.load(qt)

        strings = questions['dares']
        j = len(strings)
        i = randint(0, j - 1)

        k = len(ctx.guild.members)
        m = randint(0, k - 1)
        other = ctx.guild.members[m].mention

        embed = discord.Embed()
        embed.title = f"{user.name} dared {member.name}"
        embed.description = strings[i].format(name=other)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(QOTD(bot))