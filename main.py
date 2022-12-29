# import library
import discord
import datetime
from discord.ext import commands
from datetime import datetime

# custom pagination menu using new discord buttons
from pagination.pagination import create_results_navigation

# helper functions for web scraping
from scraping.scraping import *

# import utility helper functions
from utils.utils import send_error_embed
from utils.constants import HEADERS

# discord 2.0 requires these intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix="$", intents=intents)
client.remove_command('help')

# bot status
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    print('Bot is Running....')

    await client.tree.sync()
    
# error handling for command not found
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found. Type `!help` to see all commands.')

# Do you want flag ?
@client.hybrid_command()
@commands.guild_only()
async def flag(ctx):
    if ctx.guild and ctx.guild.id == 1050590155498606613:
        await ctx.send("This command can't be used in this server.")
    elif ctx.guild and "Admin" not in [role.name for role in ctx.author.roles]:
        await ctx.send("You don't have permission to use this command.")
    else:
        await ctx.send("REDACTED")
        
# bot token
client.run("YOUR TOKEN")
 
        
        
