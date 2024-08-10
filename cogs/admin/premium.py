import discord
from discord.ext import commands
from discord.ui import Button, View
from aiohttp import ClientSession
import utils.database as database
import utils.transactions as transactions
import asyncio

bot_id = "757945524937818141"



class name_modal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Type name here..."))

    async def callback(self, interaction: discord.Interaction):
        '''
        Change server name
        '''
        
        new_name = self.children[0].value
        return new_name


class ShopButtons(discord.ui.View):
    

    @discord.ui.button(label="A", style=discord.ButtonStyle.primary, emoji="🅰") 
    async def name_callback(self, button, interaction):
        self.disable_all_items()
        '''
        Changes the name of the server
        '''
        amount = 5000

        transactions.transfer_credits(interaction.user.id, bot_id, amount)

        # changing name
        new_name = await interaction.response.send_modal(name_modal(title="Change Server Name")) 
        await interaction.guild.edit(name = new_name)


        embed = discord.Embed(description=f"✅ | Successfully changed to {new_name}", ephemeral = True)
        return await interaction.response.send_message(embed = embed)

    
    @discord.ui.button(label="B", style=discord.ButtonStyle.primary, emoji="🅱") 
    async def icon_callback(self, button, interaction):

        def check_user(message):
            return message.author == interaction.user

        self.disable_all_items()
        
        amount = 10000

        transactions.transfer_credits(str(interaction.user.id), str(bot_id), amount)

        embed = discord.Embed(description =  f"Send an image! You have 20 seconds. Only accepts .jpg, .png filetypes.", color = 0xf5e2e4, )

        await interaction.response.defer()
        await interaction.edit_original_response(embed = embed, view = None)

        try:


            msg = await self.bot.wait_for("message", check=check_user, timeout=20.0)

            
        except asyncio.TimeoutError:
            # User didn't send a message in 20 seconds
            embed = discord.Embed(description =  f"Transaction failed. Credits will be given back.", color = 0xf5e2e4)
            transactions.add_credits(str(interaction.user.id), amount)
            await interaction.response.defer()
            await interaction.edit_original_response(embed = embed, view = None)

        else:
            attachment = msg.attachments[0]

            if attachment.filename.endswith(('.jpg','.png','.jpeg')):
                icon = attachment.url
                async with ClientSession() as session:
                    async with session.get(icon) as response:
                        if response.status == 200:
                            icon_data = await response.read()
                            transactions.transfer_credits(interaction.user.id, bot_id, amount) #paying tribute
                            
                            await interaction.guild.edit(icon = icon_data)  #editing server icon
                            

                            #------- confirmation that image has been changed -------
                            embed = discord.Embed(description =  f"Server icon has been successfully changed by **{interaction.user.nick}**!", color = 0xf5e2e4)

                            await interaction.response.defer()
                            return await interaction.edit_original_response(embed=embed)


    @discord.ui.button(label="C", style=discord.ButtonStyle.primary, emoji="©") 
    async def nickname_callback(self, button, interaction):
        self.disable_all_items()
        '''
        Changes the name of the server
        '''
        amount = 500

        transactions.transfer_credits(interaction.user.id, bot_id, amount)

          # changing name
        new_name = await interaction.response.send_modal(name_modal(title="Change Nickname")) 
        await interaction.user.edit(nick=new_name)


        embed = discord.Embed(description=f"✅ | Successfully changed to {new_name}", ephemeral = True)
        return await interaction.response.send_message(embed = embed)

class Premium(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #self.image = utils.image("\cogs\img\cart.png")
        
    @commands.slash_command(name = "shop", description = "Premium Server Commands.")
    async def shop(self, ctx):
       
        embed = discord.Embed(title = "Premium Shop", color = 0xff8c69)
        
        goods = {"A | Change Server Name" : "```5000 ◉```",
                "B | Change Server Icon" : "```10000 ◉```",
                "C | Change Nickname" : "```500 ◉```"}
        
        for good, price in goods.items():
            embed.add_field(name=good, value = price, inline = False)
        
        embed.set_thumbnail(url='https://cdn3d.iconscout.com/3d/premium/thumb/cart-5590713-4652405.png?f=webp')
        
        return await ctx.respond(embed = embed, view  = ShopButtons())
    
    
      

        




        

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
                           
                            await ctx.guild.edit(icon = icon_data)  #editing server icon
                            

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

