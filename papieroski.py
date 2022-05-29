import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
async def papieroski(ctx, cena: float, paczki: int, miesiac:int):
  embed = discord.Embed(title = "Kalkulator papierosków", colour = 0x9d0208)
  embed.add_field(name="Cena za paczkę", value = f"{cena}zł", inline = False)
  embed.add_field(name="Ilość paczek", value = f"{paczki} szt." , inline = False)
  embed.add_field(name = "Ilość miesięcy", value = f"{miesiac}", inline = False)
  miesiac = cena * paczki
  embed.add_field(name="Suma na miesiąc" , value = f"{miesiac}zł")
  half_year = miesiac * 6
  embed.add_field(name="Suma na pół roku", value = f"{half_year}zł")
  whole_year = miesiac * 12
  embed.add_field(name="Suma roczna", value=f"{whole_year}zł")
  embed.set_footer(text="Nie zapomnij wesprzeć działania bota! Liczy się każda złotówka ")
  await ctx.send(embed=embed)

@papieroski.error
async def papieroski_error(ctx):
  await ctx.send("wystąpił błąd, sprawdź czy wszystko jest poprawnie wpisane.")

def setup(cmd):
  cmd.add_command(papieroski)
  
