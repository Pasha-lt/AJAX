import asyncio
import json

#Verification data
REQ_1 = {
    "request_id": "01",
    "data": "Hub&&name&&qwe&&id&&123&&%%Device&&name&&wqe&&id&&234&&"
}


class Client:
    def __init__(self, loop, host, port):
        self.loop = loop
        self.host = host
        self.port = port

    async def tcp_echo_client(self, REQ):
        """
        The client sends a request and waits for a response from the server.
        :param REQ - request.
        """
        reader, writer = await asyncio.open_connection(self.host, self.port, loop=self.loop)
        print(f'Send REQ: {REQ}\n')

        # Converts REQ into encoded JSON order, after that sends to the server.
        writer.write(json.dumps(REQ).encode())
        response = await reader.read(100)

        # Decoding response.
        convert_response = response.decode()
        print(convert_response, "Close client socket\n")
        writer.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = Client(loop, 'localhost', 8001)
    try:
        asyncio.ensure_future(client.tcp_echo_client(REQ_1))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
        print('\n', 'You closed applications using the keyboard')

