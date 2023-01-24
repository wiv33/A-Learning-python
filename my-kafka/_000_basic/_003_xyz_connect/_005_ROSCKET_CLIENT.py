import asyncio
import logging

from rsocket.helpers import single_transport_provider
from rsocket.payload import Payload
from rsocket.rsocket_client import RSocketClient
from rsocket.rx_support.rx_rsocket import RxRSocket
from rsocket.transports.tcp import TransportTCP


async def main():
    connection = await asyncio.open_connection('localhost', 7000)

    async with RSocketClient(single_transport_provider(TransportTCP(*connection))) as client:
        rx_client = RxRSocket(client)
        payload = Payload(b'Hello World')

        result = await rx_client.request_response(payload)

        logging.info(result.data)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
