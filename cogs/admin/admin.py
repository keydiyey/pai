import discord #upm package(py-cord)
from discord.ext import commands


class Administrator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member = discord.Member, *, reason = None):
        embed = discord.Embed()

        if reason == None:
            await member.kick()
            desc = f"**{member}** has been kicked for **no reason**."
        else:
            await member.kick(reason=reason)
            desc = f"**{member}** has been kicked for {reason}."
            
        embed.set_author(name = member, icon_url = member.avatar_url)


    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(f"Pong! {self.bot.latency*1000:,.0f} ms.")

    @commands.command()
    async def ghostping(self, ctx, user:discord.Member):
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Administrator(bot))