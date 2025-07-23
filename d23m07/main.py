import asyncio
import aiohttp

async def fetch_data(session, url):
    async with session.get(url) as responce:
        data = await responce.text()
        print(data)
        return data

async def main():
    urls = [
        'https://httpbin.org/delay/1',
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/3',
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for i, result in enumerate(results):
            print(f"Данные из {urls[i]}: {len(result)} символов")

asyncio.run(main())