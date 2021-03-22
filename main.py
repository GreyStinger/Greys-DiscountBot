import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

prefix = '!='
bot = commands.Bot(command_prefix=prefix, description='Grey\'s Watchdog')


@bot.command()
async def say(ctx, arg='Please tell me what you would like me to say...'):
    await ctx.send(arg)


@bot.command()
async def hi(ctx):
    await ctx.send(f'Hello there.')


@bot.event
async def on_ready():
    game = discord.Activity(type=discord.ActivityType.watching, name="Greys Server")
    await bot.change_presence(activity=game, status=discord.Status.idle)
    print(f'On ready triggered and status is set. Logged in with {bot.user}')


bot.run('secret')
