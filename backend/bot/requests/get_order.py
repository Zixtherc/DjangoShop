import aiohttp

async def get_orders(user_id: int):
    params = {
        'user': user_id
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(
            'http://127.0.0.1:8000/api/orders/',
            params=params
        ) as response:
            return await response.json()