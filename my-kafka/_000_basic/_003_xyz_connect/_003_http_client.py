import time

import rsocket
import asyncio
import aiohttp

import aiohttp
import asyncio
import json

_id = "ss01"
url = f"http://localhost:8080/v1/power-ball-choice/conn-id/{_id}/test"


async def fetch(client):
    async with client.get(url) as resp:
        print(resp)
        assert resp.status == 200

        result = await resp.text()
        print(result)
        result_json = json.loads(result)
        return result_json



async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as client:
        prev_algo = {}
        result = await fetch(client)
        if prev_algo and result['algorithm'] == prev_algo['algorithm']:
            prev_algo = result

        print(prev_algo)
        print(result)


loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(main(loop))
    loop.run_forever()
finally:
    loop.close()
