import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")



@bot.command()
async def mute(ctx,member: discord.Member):
  role = discord.utils.get(ctx.guild.roles, name="TEST")

  if role in ctx.author.roles:
    await member.edit(mute=True)

  elif ctx.author.guild_permissions.administrator:
    await member.edit(mue=True)

  else:
    
    await ctx.send(f"{ctx.author} Nie masz uprawnień do tej komendy")
    #await member.edit(deafen=True)
   

@bot.command()
async def silent(ctx, member: discord.Member):
  role = discord.utils.get(ctx.guild.roles, name="TEST")

  if role in ctx.author.roles:
    await member.edit(mute=True)
    await member.edit(deafen=True)

  elif ctx.author.guild_permissions.administrator:
    await member.edit(mue=True)
    await member.edit(deafen=True)

  else:
    await ctx.send(f"{ctx.author} Nie masz uprawnień do tej komendy")


@bot.command()
async def unmute(ctx,member: discord.Member):
  role = discord.utils.get(ctx.guild.roles, name="TEST")

  if role in ctx.author.roles:
    await member.edit(mute=False)

  elif ctx.author.guild_permissions.administrator:
    await member.edit(mue=False)

  else:
    
    await ctx.send(f"{ctx.author} Nie masz uprawnień do tej komendy")
    #await member.edit(deafen=True)
   
@bot.command()
async def unsilent(ctx,member: discord.Member):
  role = discord.utils.get(ctx.guild.roles, name="TEST")

  if role in ctx.author.roles:
    await member.edit(mute=False)
    await member.edit(deafen=False)

  elif ctx.author.guild_permissions.administrator:
    await member.edit(mute=False)
    await member.edit(deafen=False)

  else:
    
    await ctx.send(f"{ctx.author} Nie masz uprawnień do tej komendy")
    #await member.edit(deafen=True)
   


def setup(cmd):
  cmd.add_command(unsilent)
  cmd.add_command(unmute)
  cmd.add_command(silent)
  cmd.add_command(mute)
  