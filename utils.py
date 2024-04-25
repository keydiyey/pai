
import discord #upm package(py-cord)
import json
import os



class database:
    def load(self):
        with open('./data/user_info.json', encoding = "utf8") as a:
            self.data = json.load(a)
            
    def _is_existing(self, userid):
        self.load()
        if str(userid) in self.data:
            pass    
        else:
            return None

    def write(self, data, address):
        with open(address, "w") as info:
            json.dump(data, info, indent = 4)
        return
    
    def register(self, userID):
        self.load()
        users = self.data
        users[userID] = {}
        users[userID]["credits"] = 1000
        users[userID]["reputation"] = 0
        users[userID]["deaths"] = 0
        users[userID]["jailtime"] = 0
        self.write(users, "data/user_info.json")


     
class member:
    def __init__(self, user):
        self.ID = user.id
        self.nickname = user.nick 
        
        if database._is_existing(self.ID) != None:
            self.info =self.data[self.ID]
            self.credits = self.info["credits"]
            self.reputation = self.info["reputation"]
            self.deaths = self.info["deaths"]
            self.jailtime = self.info["jailtime"]
            print(2)
            
        else:
            pass
        
    async def account404(self, ctx, userid):
        message = '''Hello. It seems like you do not have a Pai Account yet. 
                    We will automatically create one for you with 1000 bonus credits. 
                    After this you may check your account and balance. 
                    Please enjoy your stay.'''
            
        self.database.register(userid)
        embed = discord.Embed(description =  message, color = 0xf5e2e4)
        
        return await ctx.respond(embed = embed)

    
    async def pay(self, amount):
        self.credits -= amount
    
    
    
    

class image:
    def __init__(self, directory):
        self.file = discord.File(os.getcwd() + directory, filename='image.png')  
    

    

    