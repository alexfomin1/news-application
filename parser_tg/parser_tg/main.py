import asyncio
import sys
from time import time

from loguru import logger
from telethon import TelegramClient

from config import *
from models import validate_article

logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


async def main():
    start = time()
    client = TelegramClient("parsing", api_id, api_hash)
    await client.start()
    message = await client.get_messages("bazabazon", limit=1)
    print(message[0].message)
    # print(messages[0].id, messages[0].message)
    await client.disconnect()
    end = time()
    logger.info(f"Время выполнения: {end - start}")


if __name__ == "__main__":
    asyncio.run(main())
