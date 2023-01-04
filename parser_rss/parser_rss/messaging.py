import asyncio
from aio_pika import Message, connect
from loguru import logger
import sys
import json
from config import rabbitmq_url

logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


async def send(title, summary, source, link):
    data = {"title": title, "summary": summary, "source": source, "link": link}
    connection = await connect(rabbitmq_url)

    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("hello")
        await channel.default_exchange.publish(
            Message(json.dumps(data).encode()),
            routing_key=queue.name,
        )

        # logger.info(f"Message {data} sent!")
