from .. import bot 
from telethon import events
import random 
import time


@bot.on(events.NewMessage(incoming=True, pattern="/game"))
async def game(event):
  await event.reply('Dice Game\n\nGame info:\nTwo dices 🎲 were rolled randomly. You have to choose your favourite number or we can say a random number in a range of 1-6. If the number matches with any of the output of dice then congratulations you won.\n\nChoose your favourite number by typing\nFav.num = "your number"\n\nFor example:\nFav.num = 5')


@bot.on(events.NewMessage(incoming=True, pattern="Fav.num = ?(.*)"))
async def game(event):
  num = str(event.text[10:])
  #await event.reply(num)
  #await event.reply(num)
  
  if num == "1" or num == "2" or num == "3" or num == "4" or num == "5" or num == "6":
  
    abc = await event.reply("I got your favourite number")
    time.sleep(2)
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    xy = str(dice1)
    yz = str(dice2)
    di1 = "First dice : " + str(dice1)
    di2 = "Second dice : " + str(dice2)
    di = di1 + "\n" + di2 
    
    await abc.edit("Rolling dices...")
    time.sleep(2)
    await abc.edit(di)
    time.sleep(2)
    
    if num == xy or num == yz:
      await abc.edit("Congratulations 🎉. You won")
    else:
      await abc.edit("You lose. Better luck next time")
    
    
  else:
   await event.reply("Number out of range or it is not a number type a valid number in a range of 1-6. Only a single number after Fav.num = ")
