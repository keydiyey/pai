import os
import discord
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
    'cogs.admin.admin',
    'cogs.admin.help',
    'cogs.admin.error',
    'cogs.admin.listener',

    #---------- commands -------------
    'cogs.fortune',
    'cogs.mafia',
    'cogs.premium',
    'cogs.miscellaneous',
    'cogs.tor',

    #----------- economy --------------
    'cogs.economy',
]

for cog in cogs:
    try:
        bot.load_extension(cog)
        print(cog + " was loaded.")
    except Exception as e:
        print(e)


@bot.command(pass_context=True)
async def reload(ctx,cog):
    try:
        await bot.reload_extension(f'{cog}')

    except Exception as e:
        print(f"\n {e}")
    

bot.run(TOKEN)
