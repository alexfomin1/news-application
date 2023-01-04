import asyncio
import sys
from loguru import logger


from redising import (
    validate_data_redis,
    exists_redis_key,
    redis_value_same,
    set_redis_value,
    get_all_redis,
)
from actions_db import (
    create_article,
    exists_source,
    get_latest_article_by_source,
    get_latest_article_url_by_source,
)
from messaging import send

"""
0. Validate data
1. Check if source in redis?
2.1. Source in redis
    3. Check if link is same?
        4.1. Link is same
            5. Exit
        4.2. Link is not same
            5. Change in redis
                6. Change in postgres
                    7. Post data
                        8. Exit
2.2. Source not in redis
    3. Check if source in postgres?
        4.1. Source in postgres
            5. Get the latest in db url
                6. Check if url is the latest?
                    7.1. Link is the latest
                        8. Set value in redis
                            9. Exit
                    7.2. Link is not the latest
                        8. Change in redis
                            9. Change in postgres
                                10. Post data
                                    11. Exit
        4.2. Source not in postgres
            5. Change in redis
                6. Change in postgres
                    7. Post data
                        8. Exit
"""

logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


async def check_art(source, link, title, summary):
    if not await validate_data_redis(source=source, link=link):  # 0
        return None
    if await exists_redis_key(source) == 1:  # 1
        # source in redis
        if await redis_value_same(key=source, value=link):  # 3
            logger.info("Value is same in redis")
            # 4 article is same in redis
            pass  # 5 exit
        else:
            # 4.2 article is not same in redis
            logger.info(f"New link: {link}")
            # new value
            await set_redis_value(key=source, value=link)  # 5 change in redis
            logger.info("value set in redis")
            await create_article(
                title=title, source=source, summary=summary, url=link
            )  # 6 create article in postgres
            logger.info("value added in postgres")
            await send(
                title=title, source=source, summary=summary, link=link
            )  # 7 posting data / sending in message broker
            logger.info("value sent in rabbitmq")
            # 8 exit

    else:
        # 2.2 source not in redis
        if await exists_source(source):  # 3
            # 4.1. exists in postgres
            value_in_db = await get_latest_article_url_by_source(source=source)  # 5
            if value_in_db == link:  # 6
                # 7.1 link is actual
                await set_redis_value(key=source, value=link)  # 8
                logger.info("new value in redis set, no source")
                await get_all_redis()
                # 9 exit
            else:
                # 7.2 link is not actual
                logger.info(f"New link: {link}")
                # new value
                await set_redis_value(key=source, value=link)  # 8 change in redis
                logger.info("new value in redis set")
                await create_article(
                    title=title, source=source, summary=summary, url=link
                )  # 9 create article in postgres
                logger.info("new article in postgres created")
                await send(
                    title=title, source=source, summary=summary, link=link
                )  # 10 posting data / sending in message broker
                logger.info("value sent in rabbitmq")
                # 11 exit
        else:
            # 4.2. not exists
            logger.info(f"New link: {link}")
            # new value
            await set_redis_value(key=source, value=link)  # 5 change in redis
            logger.info("new value in redis set")
            await create_article(
                title=title, source=source, summary=summary, url=link
            )  # 6 create article in postgres
            logger.info("new value in postgres set")
            await send(
                title=title, source=source, summary=summary, link=link
            )  # 7 posting data / sending in message broker
            logger.info("new value in rabbitmq sent")
            # 8 exit
