import aiohttp
import asyncio
import tracemalloc
import requests
tracemalloc.start()
token = "your token here"
async def mass_leave():
    headers = {'Authorization': token}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://discordapp.com/api/v6/users/@me/guilds', headers=headers) as resp:
            guilds = await resp.json()
            for guild in guilds:
                try:
                    # cuz maybe aiohttp is broken we try requests
                    await session.delete(f'https://discordapp.com/api/v6/users/@me/guilds/{guild["id"]}', headers=headers)
                    print(f'Left {guild["name"]}')
                    await session.delete(f'https://discordapp.com/api/v6/users/@me/guilds/{guild["id"]}', headers=headers)
                    requests.delete(f'https://discordapp.com/api/v6/users/@me/guilds/{guild["id"]}', headers=headers)
                except:
                    print(f'Failed to leave {guild["name"]}')
loop = asyncio.get_event_loop()
loop.run_until_complete(mass_leave())
