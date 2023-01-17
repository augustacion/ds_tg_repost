from datetime import datetime
import os

from dotenv import load_dotenv
from telethon import TelegramClient, sync
import asyncio
import discord
from discord.ext import commands

load_dotenv()
TIMEOUT = 20
MSG_BATCH = 10

# ================================================
# init Discord client
channels_to_read = set(os.environ.get('DISCORD_CHANNELS').split('@'))
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# ================================================
# init Telegram client
channels_to_fwd = set(os.environ.get('TELEGRAM_CHANNELS').split('@'))
api_id = os.environ.get('TELEGRAM_API_ID', '')
api_hash = os.environ.get('TELEGRAM_API_HASH', '')

client = TelegramClient('session_name', api_id, api_hash)

# ================================================


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} [ {bot.user.id} ]')
    await client.start()
    print("Started at ", datetime.now().strftime('%D %H-%M-%S'))


@bot.event
async def on_message(message):
    if message.channel.name in channels_to_read:
        for channel in channels_to_fwd:
            print(f"Sent to {channel}: {message.jump_url}")
            await client.send_message(channel, f"{message.content}\n{message.jump_url}")


bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
