import asyncio


async def create_link(chat_id, post_id):
    return f"https://t.me/{chat_id}/{post_id}"
