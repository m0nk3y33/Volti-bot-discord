import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.command(pass_context=True)
async def move(ctx, member: discord.Member, *,channel: discord.VoiceChannel ):
  role = discord.utils.get(ctx.guild.roles, id=933775101839679508)

  if role in ctx.guild.roles:

    await ctx.send("Nie da się pokonać szefa :))")

  else:
    await member.move_to(channel)


@bot.command()
async def psychomove(ctx, member: discord.Member, start_channel: discord.VoiceChannel, end_channel: discord.VoiceChannel, ilosc: int):

  for i in range(ilosc):
      await member.move_to(start_channel)
      await member.move_to(end_channel)





def setup(cmd):
    cmd.add_command(psychomove)
    cmd.add_command(move)
