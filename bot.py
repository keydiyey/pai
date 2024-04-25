import os
import discord
import server
from cogwatch import watch
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix=commands.when_mentioned_or("pai ", "pai"),
                   intents=discord.Intents.all(),
                   help_command=None)

#'''''''''''''''''''''''''''''#
#      For Loading Cogs       #
#.............................#
cogs = [
    #----------- admin ---------------
    'cogs.admin.help',
    'cogs.admin.error',
    'cogs.admin.premium',
    'cogs.economy.bank',

    #---------- commands -------------
    'cogs.fortune',
    'cogs.roleplay',
   

    #----------- economy --------------

]

for cog in cogs:
    try:
        bot.load_extension(cog)
        print(f"⋙  {cog}")
    except Exception as e:
        print(f"⊗  {cog} : {e}")

@bot.listen()
async def on_ready():
    server.srv()
    print('----------------------------------\n')
    print('Welcome back Master!')
    print('Pai is now online! \n')
    
    await bot.change_presence(
        activity = discord.Activity(type = discord.ActivityType.watching, name = 'you make mistakes...'))

@bot.command(pass_context=False)
async def reload(cog):
    try:
        await bot.reload_extension(cog)
    except Exception as e:
        print(f"\n {e}")
    
bot.run(TOKEN)
