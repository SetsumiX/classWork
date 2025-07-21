import aiohttp, asyncio
#
# async def fetch_user_data(user_id:int):
#     url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             if response.status == 200:
#                 data = await response.json()
#                 print(f"Пользователь {user_id}: {data['name']}")
#             else:
#                 print(f"Ошибка запроса пользователя: {user_id}")
#
# async def main():
#     tasks = []
#     for user_id in range(1, 11):
#         task = asyncio.create_task(fetch_user_data(user_id))
#         tasks.append(task)
#
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())

print("one")
async def fetch_data(url):
    print(f"Скачивание url...")
    await asyncio.sleep(2)
    print(f"Получаем документацию из {url}")

print("two")
async def main():
    task1 = asyncio.create_task(fetch_data("https://jopa.org/data1"))
    task2 = asyncio.create_task(fetch_data("https://jopa.org/data1"))
    await task1
    await task2
print("three")
asyncio.run(main())
print("four")