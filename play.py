import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.command()
async def play(ctx):
  await ctx.send("Kiedyś kurwo będę grał muzyczkę")


def setup(cmd):
    cmd.add_command(play)
