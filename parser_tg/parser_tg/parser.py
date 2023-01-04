import feedparser
import asyncio
import aiohttp
from loguru import logger
import sys

from headers import get_headers


logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


async def parser(source):
    timeout = aiohttp.ClientTimeout(total=4)
    try:
        async with aiohttp.ClientSession(
            timeout=timeout,
            headers=await get_headers(),
            connector=aiohttp.TCPConnector(verify_ssl=False),
        ) as session:
            try:
                async with session.get(source["url"]) as response:
                    feed = feedparser.parse(await response.text())
                    # return feed['entries'][0]
                    try:
                        return {
                            "source": source["name"],
                            "title": feed["entries"][0]["title"],
                            "link": feed["entries"][0]["link"],
                            "summary": feed["entries"][0]["summary"],
                        }

                    except Exception:
                        return None
            except Exception:
                return None
    except TimeoutError:
        logger.error(f"{TimeoutError} while parsing {source['name']}")
