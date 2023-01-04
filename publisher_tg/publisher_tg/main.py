import asyncio
from aio_pika import connect, Message
from aio_pika.abc import AbstractIncomingMessage
import json
from config import rabbitmq_url
from formatting import format
import publishing
from loguru import logger
import sys

logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


async def on_message(message: AbstractIncomingMessage) -> None:
    logger.info("Message received")
    result = message.body.decode()
    result = json.loads(result)

    message_formatted = await format(
        source=result["source"],
        title=result["title"],
        summary=result["summary"],
        link=result["link"],
    )
    await publishing.send(message_formatted)
    logger.info("Message published")


async def receive():
    connection = await connect(rabbitmq_url)
    async with connection:
        # Creating a channel
        channel = await connection.channel()

        # Declaring queue
        queue = await channel.declare_queue("hello")

        # Start listening the queue with name 'hello'
        await queue.consume(on_message, no_ack=True)

        await asyncio.Future()


# async def send():
#    # Perform connection
#    connection = await connect(rabbitmq_url)
#
#    async with connection:
#        # Creating a channel
#        channel = await connection.channel()
#
#        # Declaring queue
#        queue = await channel.declare_queue("hello")
#
#        message = {
#            "title": "no way one two three",
#            "summary": "привет пока",
#            "link": "google.com",
#            "source": "rbc",
#        }
#        # Sending the message
#        await channel.default_exchange.publish(
#            Message(json.dumps(message).encode()),
#            routing_key=queue.name,
#        )


if __name__ == "__main__":
    asyncio.run(receive())
