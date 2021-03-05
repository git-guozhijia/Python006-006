import aiohttp
import asyncio

url = "http://httpbin.org/get"


async def fetch(client, url):
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.text()


async def main():
    async with aiohttp.ClientSession() as client:
        html = await fetch(client, url)
        print(html)


loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)
loop.run_until_complete(asyncio.sleep(0))
loop.close()
