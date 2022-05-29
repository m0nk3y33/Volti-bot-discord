import discord
from discord import Embed
from discord.ext import commands
from webserver import keep_alive
import os
from datetime import datetime
import pytz
from discord_slash import SlashCommand, SlashContext

#import colorama

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command("help")
slash = SlashCommand(bot)

@slash.slash(name = "cos")
async def cos(ctx: SlashContext):
  embed = Embed(title="Cos Test")
  await ctx.send(embed = embed)


@bot.event
async def on_ready():
    print("I'm Ready to use")
    print(f"Prędkość łącza - {round(bot.latency * 1000)}ms")
    await bot.change_presence(activity=discord.Game(name="PEGASUS"))
    #guild = bot.get_guild(689426242868740113)
    #member = guild.get_member(int(408698577112662016))
    #role = guild.get_role(int(791284079789867008))
    #await member.remove_roles(role)


@bot.event
async def on_member_join(ctx):
  role = discord.utils.get(ctx.guild.roles, name = "Nowy")
  await ctx.add_roles(role)

@bot.command()
async def test(ctx):
    print("test")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("*Nie ma takiej komendy. Daj mi w spokoju pilnować balkonu*")
    await ctx.send(file=discord.File('img/error.png'))


#każda czynność usera jaką wykonuje jest kontrolowana poniżej
@bot.event
async def on_voice_state_update(member,after,before):
  if before.self_mute == True:

    now = datetime.now(pytz.timezone('Europe/Warsaw'))
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d | %B | %Y")
    print("[",current_date,",",current_time,"]",member.name,"Wyciszył się", " | ", member.id)

    user_data = {
      "Data": current_date,
      "Czas" : current_time,
      "Nazwa": member.name,
      "Czynnosc": 'Wyciszyl sie',
      "Id": member.id 
    }

    
    with open(r'log.txt', 'a') as file:
      file.write(str(user_data) + '\n\n')
    


  elif after.self_mute == True:

    now = datetime.now(pytz.timezone('Europe/Warsaw'))
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d | %B | %Y")
    print("[",current_date,",",current_time,"]",member.name,"Odciszył się", " | ", member.id)

    user_data = {
      "Data": current_date,
      "Czas" : current_time,
      "Nazwa": member.name,
      "Czynnosc": 'Odciszył się',
      "Id": member.id 
    }

    with open('log.txt', 'a') as file:
      file.write(str(user_data) + '\n\n')


  elif before.afk == True:
    now = datetime.now(pytz.timezone('Europe/Warsaw'))
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d | %B | %Y")
    print("[",current_date,",",current_time,"]",member.name,"Poszedł AFK", " | ", member.id)

    user_data = {
      "Data": current_date,
      "Czas" : current_time,
      "Nazwa": member.name,
      "Czynnosc": 'Poszedł AFK',
      "Id": member.id 
    }

    with open('log.txt', 'a') as file:
      file.write(str(user_data) + '\n\n')

  elif after.afk == True:
    now = datetime.now(pytz.timezone('Europe/Warsaw'))
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d | %B | %Y")
    print("[",current_date,",",current_time,"]",member.name,"Wrócił z AFK'a", " | ", member.id)

    user_data = {
      "Data": current_date,
      "Czas" : current_time,
      "Nazwa": member.name,
      "Czynnosc": 'Wrócił z AFKa',
      "Id": member.id 
    }

    with open('log.txt', 'a') as file:
      file.write(str(user_data) + '\n\n')


  elif before.self_stream == True:
    now = datetime.now(pytz.timezone('Europe/Warsaw'))
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d | %B | %Y")
    print("[",current_date,",",current_time,"]",member.name,"Rozpoczął streama", " | ", member.id)

    user_data = {
      "Data": current_date,
      "Czas" : current_time,
      "Nazwa": member.name,
      "Czynnosc": 'Rozpoczął streama',
      "Id": member.id 
    }

    with open('log.txt', 'a') as file:
      file.write(str(user_data) + '\n\n')



  elif after.self_stream == True:
    now = datetime.now(pytz.timezone('Europe/Warsaw'))
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d | %B | %Y")
    print("[",current_date,",",current_time,"]",member.name," Zakończył streama", " | ", member.id)


    user_data = {
      "Data": current_date,
      "Czas" : current_time,
      "Nazwa": member.name,
      "Czynnosc": 'Zakończył streama',
      "Id": member.id 
    }

    with open('log.txt', 'a') as file:
      file.write(str(user_data) + '\n\n')



  elif before.self_video == True:
    now = datetime.now(pytz.timezone('Europe/Warsaw'))
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d | %B | %Y")
    print("[",current_date,",",current_time,"]",member.name," Rozpoczął odtwarzanie video", " | ", member.id)

    user_data = {
      "Data": current_date,
      "Czas" : current_time,
      "Nazwa": member.name,
      "Czynnosc": 'Rozpoczął odtwarzanie video',
      "Id": member.id 
    }

    with open('log.txt', 'a') as file:
      file.write(str(user_data) + '\n\n')



  elif after.self_video == True:
    now = datetime.now(pytz.timezone('Europe/Warsaw'))
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d | %B | %Y")
    print("[",current_date,",",current_time,"]",member.name," Zakończył odtwarzanie video", " | ", member.id)

    user_data = {
      "Data": current_date,
      "Czas" : current_time,
      "Nazwa": member.name,
      "Czynnosc": 'Zakończył odtwarzanie video',
      "Id": member.id 
    }

    with open('log.txt', 'a') as file:
      file.write(str(user_data) + '\n\n')

   

  else:
    now = datetime.now(pytz.timezone('Europe/Warsaw'))
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d | %B | %Y")
    print("[",current_date,",",current_time,"]",member.name,"Z:", after.channel, "Do:", before.channel, " | ", member.id)

    user_data = {
      "Data": current_date,
      "Czas" : current_time,
      "Nazwa": member.name,
      "Czynnosc": 'Zmienił kanał',
      "Z": after.channel,
      "Do": before.channel,
      "Id": member.id 
    }

    with open('log.txt', 'a') as file:
      file.write(str(user_data) + '\n\n')

  
#każda wiadomość wysłana przez usera jest kontrolowana poniżej
@bot.event
async def on_message(message):

  now = datetime.now(pytz.timezone('Europe/Warsaw'))

  current_time = now.strftime("%H:%M:%S")
  current_date = now.strftime("%d | %B | %Y")
  print("[",current_date,",",current_time,"]", message.author, message.content)

  message_data = {
    "Data": current_date,
    "Czas": current_time,
    "User": message.author,
    "Treść": message.content
  }

  with open('message_log.txt','a') as file:
    file.write(str(message_data) + '\n\n')

  await bot.process_commands(message)





bot.load_extension("donate")
bot.load_extension("clear")
bot.load_extension("remind")
bot.load_extension("papieroski")
bot.load_extension("ascii")
bot.load_extension("move")
bot.load_extension("meme")
bot.load_extension("silent")
bot.load_extension("play")
bot.load_extension("info")


keep_alive()

token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)


  #if before.mute and after.mute:
    #logs_channel = bot.get_channel(689431083426906158)
    #print(member.name+" Joined")
  #else:
    #print('Cos')
       #print(before.self_mute, "changed their voice state into", after.self_mute)