import aiohttp, asyncio

async def fetch_user_data(user_id:int):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                print(f"Пользователь {user_id}: {data['name']}")
            else:
                print(f"Ошибка запроса пользователя: {user_id}")

async def main():
    tasks = []
    for user_id in range(1, 11):
        task = asyncio.create_task(fetch_user_data(user_id))
        tasks.append(task)

    await asyncio.gather(*tasks)

asyncio.run(main())