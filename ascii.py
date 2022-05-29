import discord, pyfiglet
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command()
async def ascii(ctx,*,args):
  await ctx.message.delete()
  text = pyfiglet.figlet_format(args)
  await ctx.send(f'```{text}```')



def setup(cmd):
  cmd.add_command(ascii)