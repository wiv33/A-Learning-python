import asyncio

import requests
from requests import request

_id = "sun18"
try:

    reader = requests.get(
        f"http://powerball.public.psawesome.xyz/v1/power-ball-choice/conn-id/{_id}/stream")
    print(reader)
    data = reader.content
    print(data)
except Exception as e:
    print("exit exception")
    print(e)
finally:
    requests.delete(f"http://powerball.public.psawesome.xyz/v1/power-ball-choice/conn-id/{_id}")
    print("finally call delete request")

requests.delete(f"http://powerball.public.psawesome.xyz/v1/power-ball-choice/conn-id/{_id}")
