

"""

import aiohttp
import asyncio
import time


async def fetch(client):
    print(f"打印 ClientSession 对象 >>>>> {client}")
    async with client.get('http://httpbin.org/get') as resp:
        assert resp.status == 200
        return await resp.text()


async def main():
    async with aiohttp.ClientSession() as client:
        html = await fetch(client)
        # print(html)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start_time = time.time()
    tasks = [loop.create_task(main()) for task in range(30)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(f"版爬虫花费时间为：{time.time() - start_time}")
"""
