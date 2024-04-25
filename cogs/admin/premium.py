import discord
from discord.ext import commands
from discord.ui import Button, View
from aiohttp import ClientSession

import utils.utils as utils


class A(Button):
    async def callback(self, interaction):
        self.user = interaction.user
        self.guild = interaction.guild
        self.client = interaction.client
        self.message = interaction.message
       
        
        embed = discord.Embed(title = "Premium Shop", description =  f"Please type the new name for the server!", color = 0xf5e2e4)
        await interaction.message.edit(embed = embed, view = None, file = None)
        server_name = await self.client.wait_for("message", check=lambda message: message.author == self.user)
        print(server_name)
        

class Premium(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.image = utils.image("\cogs\img\cart.png")
        

    @commands.command(name = "shop", description = "Premium Server Commands.")
    async def shop(self, ctx):
       
        embed = discord.Embed(title = "Premium Shop", color = 0xff8c69)
        
        goods = {"A | Change Server Name" : "```5000 ◉```",
                "B | Change Server Icon" : "```10000 ◉```",
                "C | Add/Replace Emote" : "```500 ◉```",
                "D | Add/Replace Soundboard": "```500 ◉```"}
        
        for good, price in goods.items():
            embed.add_field(name=good, value = price, inline = False)
        
        embed.set_thumbnail(url='attachment://image.png')
        
        a = A(label = "A", style = discord.ButtonStyle.green)
        
        view = View()
        view.add_item(a)
        
        return await ctx.reply(file = self.image.file, embed = embed, view  = view())
      

        




        

        '''
        if user.credits >= self.price:
            user.pay(price)

            await user.add_roles(data.tempRole)		
            await interaction.guild.edit(name = server_name)
            await user.remove_roles(data.tempRole)

            embed = discord.Embed(description =  f"Server name has been changed to **{server_name}**!", color = 0xf5e2e4)
            return await interaction.reply(embed = embed)

        else:
            embed = discord.Embed(description =  f"You do not have enough money.", color = 0xf5e2e4)
            return await interaction.reply(embed = embed, ephemeral = True)
    '''
     

'''		
    @change.command(name="icon", description="Change the server icon!")
    async def icon(self, ctx:discord.ApplicationContext):
        user = ctx.author
        guild = ctx.guild
        trader = discord.utils.get(guild.roles, name = "Trader")

        temp = utils.member(user)

        price = 5000

        
        if temp.credits >= price:

            embed = discord.Embed(description =  f"Send an image!", color = 0xf5e2e4)
            await ctx.reply(embed = embed)
            msg = await self.bot.wait_for("message", check=None, timeout=20.0)
            attachment = msg.attachments[0]

            if attachment.filename.endswith(('.jpg','.png','.jpeg')):
                icon = attachment.url
                async with ClientSession() as session:
                    async with session.get(icon) as response:
                        if response.status == 200:
                            icon_data = await response.read()
                            pc.take(user, price) #paying tribute
                            await user.add_roles(trader)		   #add permissions to enable server edit
                            await ctx.guild.edit(icon = icon_data)  #editing server icon
                            await user.remove_roles(trader)        #removing permissions
                            

                            #------- confirmation that image has been changed -------
                            embed = discord.Embed(description =  f"Server icon has been successfully changed by **{user.nick}**!", color = 0xf5e2e4)
                            await msg.respond(embed = embed)
                        else:
                            await pc.generalError(ctx)
            else:
                await pc.generalError(ctx)
        else:
            await pc.poorError(ctx)
    

    '''
                

def setup(bot):
    bot.add_cog(Premium(bot))

