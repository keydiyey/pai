import discord
from modules.data_management import load_users
from modules.errors import bank

def has_account(func):
    """Validates acount registration in Momiji Northland Bank"""
    def inner(user_id):

        if str(user_id) in load_users():
            # call original function
            func()
        else:
            return bank.transaction_error()
    return inner  #return the inner function

# define ordinary function
def ordinary():
    print("I am ordinary")

async def has_account(user_id):
    
    return await 
