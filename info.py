import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.command()
async def info(ctx,member: discord.Member):
  if ctx.author.guild_permissions.administrator:
    infoEmbed = discord.Embed(title="Informacje o użytkowniku", colour=member.colour)
    infoEmbed.add_field(name="Nazwa ogólna", value=member.name, inline = False)
    infoEmbed.add_field(name="Nazwa wyświetlana", value=member.display_name, inline = False)
    infoEmbed.add_field(name="Serwer", value=member.guild, inline = False)
    infoEmbed.set_thumbnail(url = member.avatar_url)
    infoEmbed.add_field(name="Hashtag", value=member.discriminator, inline = False)
    infoEmbed.add_field(name="Konto stworzone", value=member.created_at, inline = False)
    infoEmbed.add_field(name="Dołączył", value=member.joined_at, inline = False)
    infoEmbed.add_field(name="DC Premium", value=member.premium_since, inline = False)
    infoEmbed.add_field(name="Flags", value=member.public_flags, inline = False)
    infoEmbed.add_field(name="Relacja", value=member.relationship, inline = False)
    infoEmbed.add_field(name="System", value=member.system, inline = False)
    infoEmbed.add_field(name="Najwyższa rola", value=member.top_role, inline = False)
    infoEmbed.add_field(name="Status web", value=member.web_status, inline = False)
    infoEmbed.add_field(name="Status mobile", value=member.mobile_status, inline = False)
    infoEmbed.add_field(name="Status deskop", value=member.desktop_status, inline = False)

    infoEmbed.add_field(name="Aktywność", value=member.activity, inline = False)
    infoEmbed.set_footer(text="Wszystko pobrane całkiem 'legalnie', tak więc spoczi.")
    await ctx.send(embed=infoEmbed)
    
  else:
    await ctx.send("Brak uprawnień do tej komendy")
def setup(cmd):
    cmd.add_command(info)
