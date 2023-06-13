from telethon import TelegramClient
import logging 
import time

openai_key = "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"
api_id = "26826728"
api_hash = "35ca28ae08aa543bfcaba98649a7a580"
bot_token = "6034653584:AAGof6UAXEtMCofOzGK_yRl5ygcwOWHzZx8"
bot = TelegramClient("pythonbot", api_id, api_hash).start(bot_token=bot_token)
