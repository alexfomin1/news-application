import asyncio


async def format(source, title, summary, link):
    if summary:
        message = f"""
**{title}**
        
{summary}
        
[{source}]({link})
        """
    else:
        message = f"""
**{title}**

[{source}]({link})
        """
    return message
