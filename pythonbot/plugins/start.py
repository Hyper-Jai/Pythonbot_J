from .. import bot,openai_key
from telethon import events
import asyncio
import openai
import time 

openai.my_api_key=openai_key

@bot.on(events.NewMessage(incoming=True,pattern="/start"))
async def start(event):
  a = int(time.strftime('%H'))
  if a > 6 and a < 12:
    await event.reply("Good morning\nThis is Engamerpybot by Jai Saini ")
  elif a > 12 and a < 16:
    await event.reply("Good afternoon\nThis is Engamerpybot by Jai Saini")
  elif a > 16 and a < 20:
    await event.reply("Good evening\nThis is Engamerpybot by Jai Saini")
  else:
    await event.reply("Good night\nThis is Engamerpybot by Jai Saini")
  #client.send_message('username',"Hello this is Engamerpybot by Jai Saini")
  
@bot.on(events.NewMessage(incoming=True,pattern="Hello"))
async def start(event):
  await event.reply("Hii I am engamerbot.\nHow can I help you...")
  
@bot.on(events.NewMessage(incoming=True,pattern="/eval"))
async def start(event):
  await event.reply("Hello this is eval command")


@bot.on(events.NewMessage(incoming=True,pattern="edit"))
async def start(event):
  a=await event.reply("Get command")
  await asyncio.sleep(3)
  await a.edit("This is edited message")
  
"""@bot.on(events.NewMessage(incoming=True,pattern="(?i)/ask"))
async def chatgpt(event):
  if event.sender_id == int(5782481501):
    await event.reply("Yes you are my owner")
  else:
    await event.reply("You are a user")"""


"""@bot.on(events.NewMessage(incoming=True,pattern="(?i)/ask"))
async def chatgpt(event):
  await event.reply(f"{event}")"""

@bot.on(events.NewMessage(incoming=True,pattern="/help"))
async def help(event):
  await event.reply("""yta 'link of the video' : for downloading song from the youtube\n\nytv 'link of the video' : for downloading video from the youtube\n\n/tr hi/en(in which language you want to translate) 'sentence'\n
   /tr hi how are you""")