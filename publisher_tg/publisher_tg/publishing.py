import asyncio
import sys

from loguru import logger
from telethon import TelegramClient

from config import api_hash, api_id, bot_token, chat_id

logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


async def send(message):
    client = TelegramClient("publishing", api_id, api_hash)
    await client.start(bot_token=bot_token)
    await client.send_message(entity=chat_id,
                              message=message,
                              link_preview=False)
    await client.disconnect()
