from loguru import logger
from pydantic import ValidationError

import aioredis
import sys
import asyncio

from models import Article_redis
from config import redis_url
from actions_db import get_latest_article_by_source, create_article


logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


async def validate_data_redis(source, link):
    try:
        Article_redis(source=source, link=link)
    except ValidationError:
        logger.error("Data for redis is INVALID!")
        return False
    return True


async def exists_redis_key(key):
    redis = await aioredis.from_url(redis_url, decode_responses=True)
    existance = await redis.exists(key)
    await redis.close()
    return existance


async def get_redis_value(key):
    redis = await aioredis.from_url(redis_url, decode_responses=True)
    try:
        value = await redis.get(key)
        await redis.close()
    except Exception:
        await redis.close()
        logger.error("Timeout redis while GETTING value")
        return None
    return value


async def set_redis_value(key, value):
    redis = await aioredis.from_url(redis_url, decode_responses=True)
    await redis.set(key, value)
    await redis.close()


async def redis_value_same(key, value):
    if await get_redis_value(key) == value:
        return True
    return False


async def analyze_redis(source, link):
    if await validate_data_redis(source=source, link=link):
        if await exists_redis_key(source) == 1:
            # logger.info("KEY already in redis")
            # same value or not
            if await redis_value_same(key=source, value=link):
                # logger.info(f"Link already in redis: {link}")
                pass
            else:
                logger.info(f"New link: {link}")
                # new value
                await set_redis_value(key=source, value=link)
        else:

            logger.info(f"New link: {link}")
            # new key
            await set_redis_value(key=source, value=link)


async def get_all_redis():
    redis = await aioredis.from_url(redis_url, decode_responses=True)
    l = await redis.keys()
    for i in l:
        print(i, await redis.get(i))
    await redis.close()
