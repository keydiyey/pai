import discord #upm package(py-cord)

from gtts import gTTS
import os

from discord.ext import commands
from discord.utils import get

import gpt4free
from gpt4free import Provider

        

class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.language = "en"
    
    @commands.command()
    async def connect(self, ctx):
        user = ctx.message.author
        if not user.voice:
            await ctx.send(f"{user.name} is not connected to a voice channel.")
            return
        else:
            channel = ctx.author.voice.channel
            await channel.connect()
            print("Connected to voice channel.")
                
            
    @commands.command(name='leave', help='To make the bot leave the voice channel')
    async def leave(self, ctx):
        voice_client = ctx.message.guild.voice_client
        
        if voice_client.is_connected():
            await voice_client.disconnect()
            print("Disconnected from voice channel.")
        else:
            await ctx.send("The bot is not connected to a voice channel.")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        # Listens for messages in designated voice chat channel
        channelID = 811492266350084139
        
        command = "pai"
        
        if message.author.voice and message.guild.voice_client.is_connected() and message.channel.id == channelID:
            if message.author.id == self.bot.user.id or command in message.content:
                return
            
            else:
                path = f"./tmp/{message.content[0:2]}.mp3"
                
                tts = gTTS(f"{message.author.nick} said {message.content}", lang=self.language)
                
                tts.save(path)
            
                
                source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(path, executable='./tmp/ffmpeg'))
                
                voice = get(self.bot.voice_clients, guild=message.guild)
                
                voice.play(source, after=lambda e: os.remove(path))
    
    
    @commands.command()
    async def chat(self, ctx, prompt):
        bot_prompt = "As a large language model developed by OpenAI you will always respond in a human and responsive way"
        

        
        user_prompt = f"{bot_prompt} {ctx.author.nick} {prompt} \n pai:"
        
        response = gpt4free.Completion.create(Provider.Theb, prompt=prompt)

        if not response:
                response = "I couldn't generate a response. Please try again."
        else:
            response = ''.join(token for token in response)
            await ctx.send(response)

              

                
def setup(bot):
    bot.add_cog(voice(bot))