import requests
import json
import asyncio

import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup

class Roleplay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def getURL(self, url):
        r = requests.get(url)
        actions = json.loads(r.content)
        action = actions["url"]
        return action
        
    async def rpEmbed(self, ctx, user, action, fullAction, member):
        gif = self.getURL(f"https://api.otakugifs.xyz/gif?reaction={action}")
        embed = discord.Embed(description = f"✨ **{user.display_name}** {fullAction} **{member.display_name}** ✨", color = discord.Colour.random())
        embed.set_image(url = gif) 
        return await ctx.send(embed = embed)    
        
    @commands.command()
    async def airkiss(self, ctx, member: discord.Member = None):
        user = ctx.author
        action = "airkiss"
        fullAction = "has blown a kiss for"
        await self.rpEmbed(ctx, user, action, member)
       
    @commands.command()
    async def angrystare(self, ctx, member: discord.Member = None):
        user = ctx.author
        action = "angrystare"
        fullAction = "stared angrily at"
        await self.rpEmbed(ctx, user, action, fullAction, member)
           
    @commands.command()
    async def bite(self, ctx, member: discord.Member = None):
        user = ctx.author
        action = "bite"
        fullAction = "has bitten"
        await self.rpEmbed(ctx, user, action, fullAction, member)
        
    @commands.command()
    async def bleh(self, ctx, member: discord.Member = None):
        user = ctx.author
        action = "bleh"
        fullAction = "mocked"
        await self.rpEmbed(ctx, user, action, fullAction, member)

    @commands.command()
    async def blush(self, ctx, member: discord.Member = None):
        user = ctx.author
        action = "blush"
        fullAction = "blushes."
        await self.rpEmbed(ctx, user, action, fullAction, None)
        
    @commands.command()
    async def brofist(self, ctx, member: discord.Member = None):
        user = ctx.author
        action = "brofist"
        fullAction = "bros4life with"
        await self.rpEmbed(ctx, user, action, fullAction, member)
        
    @commands.command()
    async def celebrate(self, ctx, member: discord.Member = None):
        user = ctx.author
        action = "celebrate"
        if member == None: fullAction = "is celebrating"
        else: fullAction = "is celebrating with"
        await self.rpEmbed(ctx, user, action, fullAction, member)
        
    @commands.command()
    async def cheers(self, ctx, member: discord.Member = None):
        user = ctx.author
        action = "cheers"
        fullAction = "cheers"
        await self.rpEmbed(ctx, user, action, fullAction, member)

    @commands.command()
    async def clap(self, ctx, member: discord.Member = None):
        user = ctx.author
        action = "clap"
        fullAction = "is clapping for"
        await self.rpEmbed(ctx, user, action, fullAction, member)

    @commands.command()
    async def clap(self, ctx, member: discord.Member = None):
        user = ctx.author
        action = "clap"
        fullAction = "is clapping for"
        await self.rpEmbed(ctx, user, action, fullAction, member)
        
    @commands.command()
    async def confused(self, ctx, member: discord.Member = None):
        user = ctx.author
        action = "clap"
        fullAction = "is clapping for"
        await self.rpEmbed(ctx, user, action, fullAction, member)

    @commands.command()
    async def cool(self, ctx, member: discord.Member = None):    
        user = ctx.author
        action = "cool"
        fullAction = "cool"
        await self.rpEmbed(ctx, user, action, fullAction, member)
            
    @commands.command()
    async def cry(self, ctx, member: discord.Member = None):     
        user = ctx.author
        action = "cry"
        fullAction = "is crying."
        await self.rpEmbed(ctx, user, action, fullAction, None)
            
    @commands.command()
    async def cuddle(self, ctx, member: discord.Member):  
        user = ctx.author
        action = "cuddle"
        fullAction = "is cuddling with"
        await self.rpEmbed(ctx, user, action, fullAction, member)
            
    @commands.command()
    async def dance(self, ctx, member: discord.Member = None):   
        user = ctx.author
        action = "dance"
        if member == None: fullAction = "is dancing"
        else: fullAction = "is dancing with"
        await self.rpEmbed(ctx, user, action, fullAction, member)
        
    @commands.command()
    async def drool(self, ctx, member: discord.Member = None):   
        user = ctx.author
        action = "drool"
        fullAction = "zzzzz amimir shorreeee"
        await self.rpEmbed(ctx, member, action, fullAction, None)
        
    @commands.command()
    async def evillaugh(self, ctx, member: discord.Member = None):
        user = ctx.author
        action = "evillaugh"
        fullAction = "is laughing ominously"
        await self.rpEmbed(ctx, user, action, fullAction, None)
        
    @commands.command()
    async def facepalm(self, ctx):        
        action = "facepalm"
        fullAction = "what the hellll omhagod nooway"
        await self.rpEmbed(ctx, None, action, fullAction, None)
        
    @commands.command()
    async def handhold(self, ctx, member: discord.Member):
        user = ctx.author
        action = "handhold"
        fullAction = "is holding the hands of"
        await self.rpEmbed(ctx, user, action, fullAction, member)
        
    @commands.command()
    async def happy(self, ctx):   
            user = ctx.author
            action = "happy"
            fullAction = "is full of sunshines"
            await self.rpEmbed(ctx, user, action, fullAction, None)
            
    @commands.command()
    async def headbang(self, ctx,):
        user = ctx.author
        action = "headbang"
        fullAction = "idk what to put here"
        await self.rpEmbed(ctx, None, action, fullAction, None)
        
    @commands.command()
    async def hug(self, ctx, member: discord.Member):     
        user = ctx.author
        action = "hug"
        fullAction = "is hugging"
        await self.rpEmbed(ctx, user, action, fullAction, member)
            
    @commands.command()
    async def kiss(self, ctx, member: discord.Member):    
        user = ctx.author
        action = "kiss"
        fullAction = "kisses"
        await self.rpEmbed(ctx, user, action, fullAction, member)
            
    @commands.command()
    async def laugh(self, ctx, member: discord.Member = None):   
        user = ctx.author
        action = "laugh"
        if member == None: fullAction = "WAHAHAHAHAAHA"
        else: fullAction = "is laughing at"
        await self.rpEmbed(ctx, user, action, fullAction, member)
            
    @commands.command()
    async def lick(self, ctx, member: discord.Member):    
        user = ctx.author
        action = "lick"
        fullAction = "licks"
        await self.rpEmbed(ctx, user, action, fullAction, member)
        
    @commands.command()
    async def love(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "love"
            fullAction = "💘"
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def mad(self, ctx, member: discord.Member = None):     
            user = ctx.author
            action = "mad"
            if member == None: fullAction = "is angry"
            else: fullAction = "is angry at"
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def nervous(self, ctx, member: discord.Member = None): 
            user = ctx.author
            action = "nervous"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def no(self, ctx, member: discord.Member = None):      
            user = ctx.author
            action = "no"
            fullAction = "no."
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def nom(self, ctx, member: discord.Member = None):     
            user = ctx.author
            action = "nom"
            fullAction = "noms"
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def nosebleed(self, ctx, member: discord.Member = None):
            user = ctx.author
            action = "nosebleed"
            fullAction = ""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def nuzzle(self, ctx, member: discord.Member = None):  
            user = ctx.author
            action = "nuzzle"
            fullAction = ""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def nyah(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "nyah"
            fullAction = "nyah"
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def pat(self, ctx, member: discord.Member = None):     
            user = ctx.author
            action = "pat"
            fullAction = "patted"
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def peek(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "peek"
            fullAction = "takes a peek at"
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def pinch(self, ctx, member: discord.Member = None):   
            user = ctx.author
            action = "pinch"
            fullAction = "pinches"
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def poke(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "poke"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def pout(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "pout"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def punch(self, ctx, member: discord.Member = None):   
            user = ctx.author
            action = "punch"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def roll(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "roll"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def run(self, ctx, member: discord.Member = None):     
            user = ctx.author
            action = "run"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def sad(self, ctx, member: discord.Member = None):     
            user = ctx.author
            action = "sad"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def scared(self, ctx, member: discord.Member = None):  
            user = ctx.author
            action = "scared"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def shrug(self, ctx, member: discord.Member = None):   
            user = ctx.author
            action = "shrug"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def shy(self, ctx, member: discord.Member = None):     
            user = ctx.author
            action = "shy"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def sigh(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "sigh"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def sip(self, ctx, member: discord.Member = None):     
            user = ctx.author
            action = "sip"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def slap(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "slap"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def sleep(self, ctx, member: discord.Member = None):   
            user = ctx.author
            action = "sleep"
            fullAction =''
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def slowclap(self, ctx, member: discord.Member = None):        
            user = ctx.author
            action = "slowclap"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def smack(self, ctx, member: discord.Member = None):   
            user = ctx.author
            action = "smack"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def smile(self, ctx, member: discord.Member = None):   
            user = ctx.author
            action = "smile"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def smug(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "smug"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def sneeze(self, ctx, member: discord.Member = None):  
            user = ctx.author
            action = "sneeze"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def sorry(self, ctx, member: discord.Member = None):   
            user = ctx.author
            action = "sorry"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def stare(self, ctx, member: discord.Member = None):   
            user = ctx.author
            action = "stare"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def stop(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "stop"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def surprised(self, ctx, member: discord.Member = None):
            user = ctx.author
            action = "surprised"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def sweat(self, ctx, member: discord.Member = None):   
            user = ctx.author
            action = "sweat"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def thumbsup(self, ctx, member: discord.Member = None):        
            user = ctx.author
            action = "thumbsup"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def tickle(self, ctx, member: discord.Member = None):  
            user = ctx.author
            action = "tickle"
            fullAction =""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def tired(self, ctx, member: discord.Member = None):   
            user = ctx.author
            action = "tired"
            fullAction = ""
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def wave(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "wave"
            fullAction = "wave"
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def wink(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "wink"
            fullAction = "winks at"
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def woah(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "woah"
            fullAction = "woah"
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def yawn(self, ctx, member: discord.Member = None):    
            user = ctx.author
            action = "yawn"
            fullAction = "yawns"
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def yay(self, ctx, member: discord.Member = None):     
            user = ctx.author
            action = "yay"
            fullAction = "yay"
            await self.rpEmbed(ctx, user, action, fullAction, member)
    @commands.command()
    async def yes(self, ctx, member: discord.Member = None):     
            user = ctx.author
            action = "yes"
            fullAction = "agrees"
            await self.rpEmbed(ctx, user, action, fullAction, member)

#--------------- Help ------------------------------  
    roleplay = SlashCommandGroup("rp", "for your rp needs")
    
    @roleplay.command(name = "help", description = "pai <command> <member>")
    async def help(self, ctx):
        cog = self.bot.get_cog('Roleplay')
        commands = cog.get_commands()

        description = ""
        
        for c in commands:
                description += c.name + "       "
        
        embed = discord.Embed(title = "Roleplay Commands", description =  description, color = 0xf5e2e4)
        return await ctx.respond(embed = embed)
    
def setup(bot):
	bot.add_cog(Roleplay(bot))