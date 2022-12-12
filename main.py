import os
os.system("pip install py-cord==2.0.0b1")
import discord #upm package(py-cord)
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=commands.when_mentioned_or("pai ", "pai"),
                   intents=discord.Intents.all(),
                   help_command=None)

#'''''''''''''''''''''''''''''#

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
    'cogs.p2w',
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
@commands.has_permissions(administrator=True)
async def shutdown(ctx):
    try:
        await ctx.send("Pai is now offline.")
        await bot.close()
    except Exception as e:
        print(f"\n {e}")

    print('Pai is now offline.')


bot.run(TOKEN)
