import os
import discord
import server
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
    "cogs.miscellaneous",
    'cogs.admin.listener',
    #'cogs.economy.bank',

    #---------- commands -------------
    'cogs.fortune',
    'cogs.roleplay',
   

    #-----------  --------------
    #'cogs.crimes'

]

for cog in cogs:
    try:
        bot.load_extension(cog)
        print(f"⋙  {cog}")
    except Exception as e:
        print(f"⊗  {cog} : {e}")

@bot.event
async def on_connect():
    if bot.auto_sync_commands:
        await bot.sync_commands()
        print('----------------------------------\n')
        print(f"{bot.user.name}'s commands synced!\n")

@bot.listen()
async def on_ready():
    server.srv()

    print('Welcome back Master!')
    print('Pai is now online! \n')
    
    await bot.change_presence(status=discord.Status.idle,
                              activity = discord.Activity(type = discord.ActivityType.watching,
                                                           name = 'you make mistakes...'))

@bot.command(pass_context=False)
async def reload(cog):
    try:
        await bot.reload_extension(cog)
    except Exception as e:
        print(f"\n {e}")
    
bot.run(TOKEN)
