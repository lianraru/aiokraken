import asyncio
from aiokraken import RestClient

async def get_assets():
    """ get kraken time"""
    rest_kraken = RestClient()

    response = await rest_kraken.time()
    print(f'response is {response}')

    await rest_kraken.close()

asyncio.get_event_loop().run_until_complete(get_assets())
