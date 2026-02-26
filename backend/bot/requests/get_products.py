import aiohttp

async def get_products():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            'http://127.0.0.1:8000/api/products/'
        ) as response:
            return await response.json()