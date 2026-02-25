import aiohttp

async def create_order(user_id: int):
    data = {
        'user': user_id,
        'status': 'new'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            'http://127.0.0.1:8000/api/orders/',
            json= data
        ) as response:
            return await response.json()