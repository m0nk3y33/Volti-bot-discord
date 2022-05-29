import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="!")

@bot.command()
async def meme(ctx):
    mem = random.randint(1, 14)
    await ctx.send(file=discord.File('meme/' + str(mem) + '.png'))



def setup(cmd):
    cmd.add_command(meme)
