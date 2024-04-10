import discord
from test import losuj_pomysl
from discord.ext import commands
import random
from settings import settings

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def pomysl(ctx):
    wylosowany_pomysl = losuj_pomysl()
    await ctx.send(wylosowany_pomysl)





bot.run(settings["TOKEN"])
