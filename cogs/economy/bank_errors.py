import discord


class BankErrors:

  async def transaction_error(ctx):

    embed = discord.embed(title = "", description = "We're sorry, your transaction couldn't be completed. This could be due to several reasons, such as incorrect billing information, insufficient funds, or a temporary technical issue.")

    return await ctx.send(embed=embed, ephemeral = True)

  async def account_does_not_exist(ctx):
    embed = discord.embed(title = "", description = "We're sorry, your transaction couldn't be completed. This could be due to several reasons, such as incorrect billing information, insufficient funds, or a temporary technical issue.")

    return await ctx.send(embed=embed, ephemeral = True)