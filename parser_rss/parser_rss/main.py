import asyncio
from loguru import logger
import sys

from links import list_of_links
from parser import parser
import full_check


logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


async def main():
    while True:
        tasks = []
        for link in list_of_links:
            tasks.append(parser(link))
        for task in asyncio.as_completed(tasks):
            result = await task
            if result:
                await full_check.check_art(
                    source=result["source"],
                    link=result["link"],
                    title=result["title"],
                    summary=result["summary"],
                )

        print("=====================================")
        await asyncio.sleep(15)


if __name__ == "__main__":
    asyncio.run(main())
