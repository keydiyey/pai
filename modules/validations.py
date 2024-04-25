import discord
from data_management import load_users


async def has_permissions(ctx, permissions):
    """Checks if the author of the message has the specified permissions."""
    return all(perm in ctx.author.permissions for perm in permissions)

async def is_in_guild(ctx):
    """Checks if the command was invoked in a guild."""
    return ctx.guild is not None

async def is_admin(ctx):
    """Checks if the author of the message has the administrator permission."""
    return await has_permissions(ctx, (discord.Permissions.administrator,))


async def has_account(user_id):
    """Validates acount registration in Momiji Northland Bank"""
    return await str(user_id) in load_users()
