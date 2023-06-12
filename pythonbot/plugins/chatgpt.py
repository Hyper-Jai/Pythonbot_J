import openai
import asyncio
from telethon.tl.custom import Button
from telethon import events
from .. import bot
from .. import openai_key
import telethon

openai.api_key = openai_key
model_engine = "gpt-3.5-turbo"

k_board = [[Button.inline("stop and reset", b"stopgpt")]]

@bot.on(events.NewMessage(incoming=True,pattern="(?i)/ask"))
async def chatgpt(event):
  gpt_msg = "Hello! I am pythonbot and I will answer your question!"
  sender_id = event.sender_id
  try:
    await bot.send_message(sender_id, gpt_msg)
    async with bot.conversation(await event.get_chat(), exclusive = True, timeout = 600) as conv:
      history = []
      
      
      while True:
        gpt_msg = "Send your message"
        u_input = await send_receive(gpt_msg, conv, k_board)
        if u_input is None:
          gpt_msg = "Conversation reset.Type /ask to start a new conversation"
          await bot.send_message(sender_id, gpt_msg)
          break 
        else:
          gpt_msg = "I got your message wait for response"
          ab = await bot.send_message(sender_id, gpt_msg)
          history.append({"role":"user", "content":u_input})
          c_comp = openai.ChatCompletion.create(
            model = model_engine,
            messages = history,
            max_tokens = 100,
            n = 1,
            temperature = 0.1
            )
          response = c_comp.choices[0].message.content
          history.append({"role":"assistant","content":response})
          await ab.delete()
          await bot.send_message(sender_id, response, parse_mode = "Markdown")
          if isinstance(result, events.CallbackQuery.event):
            return None 
          else:
            return result.message.strip()
            
  except asyncio.TimeoutError:
    await bot.send_message(sender_id, "conversion ended due to no response")
    return
  except telethon.errors.AlreadyInConversationError:
    pass
  except Exception as e:
    print(e)
    await bot.send_message(sender_id, "Conversation ended. Something went wrong")
    return

async def send_receive(gpt_msg, conv, keyboard):
  msg = await conv.send_message(gpt_msg, buttons = keyboard)
  done, _ = await asyncio.wait({conv.wait_event(events.CallbackQuery()), conv.get_response()},return_when = asyncio.FIRST_COMPLETED)
  result = done.pop().result()
  await message.delete()
 