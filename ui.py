import discord
import cogs.admin.premium as premium
import utils
import json

class TempData:
    async def __init__(self, interaction):
        self.user = interaction.user
        self.guild = interaction.guild
        self.client = interaction.client
        
        self.message = interaction.message
        self.tempRole = discord.utils.get(self.guild.roles, name = "Trader")


class PremiumView(discord.ui.View):
    @discord.ui.button(label = "A", style=discord.ButtonStyle.primary)
    async def A_cb(self, button, interaction):
       
        with open('./data/user_info.json', encoding = "utf8") as a:
            data = json.load(a)
            
        user = utils.member(data.user)
        price = 5000
        
        
        embed = discord.Embed(title = "Premium Shop", description =  f"Please type the new name for the server!", color = 0xf5e2e4)
        
        await interaction.message.edit(embed = embed, view = None, file = None)
    
        server_name = await data.client.wait_for("message", check=lambda message: message.author == TempData.user)
        

        '''
        if user.credits >= price:
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
