import asyncio

import aiohttp


async def logs(cont, name):
    conn = aiohttp.UnixConnector(path="/var/run/docker.sock")
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(f"http://localhost/containers/{cont}/logs?follow=1&stdout=true") as resp:
            print(resp.status)
            async for line in resp.content:
                print(name, line)


asyncio.run(logs("63b2cb50de91", "bo_energo"))
