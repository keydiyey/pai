import discord #upm package(py-cord)
import random
import json

from discord.ui import Button, View
from discord.ext import commands


def slip():
    try:
        with open("assets/data/fortunes.json", "r") as slip:
            slips = json.load(slip)
        fortune = random.choice(("Great", "Good", "Modest", "Misfortune", "Great Misfortune"))

        if fortune == "Great Misfortune":
            y = slips[fortune][0]
        else:
            z = len(slips[fortune])-1
            x = random.randint(0,z)
            y = slips[fortune][x]

        return fortune, y
    except Exception as e:
        print(e)
        

class SlipButton(Button):
    try:
        async def callback(self,interaction):
            f = slip()
            title = f[0]
            desc = f[1]

            embed2 = discord.Embed(title = title, description = desc, color = 0xf5e2e4)
            embed2.set_thumbnail(url = "https://static.wikia.nocookie.net/gensin-impact/images/b/b0/Item_Fortune_Slip_Opened.png/revision/latest/scale-to-width-down/256?cb=20210725221204")
            await interaction.reply.edit_message(embed = embed2, view = None)
    except Exception as e:
        print(e)

class Fortune(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name = "fortune", description = "Check your luck today!")
    @commands.cooldown(1, 60*60*24, commands.BucketType.user)
    async def fortune(self, ctx):
        try:
            title = "Fortune Slip Box"
            text = f"There's a chance every day to receive a fortune slip…\nThe procedure is as follows: shake a bamboo slip from Fortune Slip Box, and exchange that bamboo slip for a Fortune Slip with Pai.\nWould you like to try your luck today?"
            slip_button = SlipButton(label = "Take a slip...", style = discord.ButtonStyle.green)

            embed = discord.Embed(title = title, description = text, color = 0xf5e2e4)
            embed.set_thumbnail(url = "https://static.wikia.nocookie.net/gensin-impact/images/d/db/Item_Bamboo_Slip.png/revision/latest/scale-to-width-down/256?cb=20210802140112")
            
            view = View()
            view.add_item(slip_button)

            await ctx.send(embed = embed, view = view)
            
        except Exception as e:
            embed = discord.Embed(title = title, description = "You are on cooldown.", color = 0xf5e2e4)
            await ctx.send(embed = embed, view = None)


def setup(bot):
    bot.add_cog(Fortune(bot))