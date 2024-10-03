import discord



class Embeds:
    async def quick_embed(self, ctx):
        color = 0xffd9cc
        title = title
        description = description


    async def justice_error(self, ctx, member):
        embed = discord.Embed(description=f"{member.display_name} is either in jail or dead. Please try again later.", color=0xffd9cc)
        return await ctx.respond(embed = embed, ephemeral = True)
    
    