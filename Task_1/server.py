import asyncio
import random
import json


class Server:
    async def handle_echo(self, reader, writer):
        """
        The server expects any incoming packet and turns it into the expected representation.
        Then randomly waits for 1 to 5 seconds.
        :param reader - object of class StreamReader
        :param writer - object of class StreamReader
        """
        REQ = await reader.read(100)
        RESP = self.translate_request(REQ)
        # Returns request_id in REQ
        request_id = json.loads(REQ.decode())["request_id"]

        addr = writer.get_extra_info('peername')
        print(f"Received REQ with request_id = {request_id} from {addr}")

        timeout = random.randint(1, 5)
        print(f"Random timeout is {timeout} seconds\n")
        await asyncio.sleep(timeout)

        print(f"Send: {RESP}")
        writer.write(RESP)
        await writer.drain()

        print("Close the client socket\n")
        writer.close()

    @staticmethod
    def translate_request(REQ):
        """
        Translates request REQ to RESP representation.
        :param MREQ - request (bytes)
        :return RESP - response (bytes)
        """
        request_dict = json.loads(REQ.decode())
        request_id = request_dict["request_id"]
        request_data = request_dict["data"]
        request_entities = [rd for rd in request_data.split("%%") if rd]
        response_data = {}
        for request_entity in request_entities:
            request_parameters = request_entity.split('&&')
            response_data[request_parameters[0]] = {
                request_parameters[i]: request_parameters[i + 1]
                for i in range(1, len(request_parameters) - 1, 2)
                if request_parameters[i + 1]
            }
        RESP = {
            "request_id": request_id,
            "data": response_data
        }
        return json.dumps(RESP).encode()


if __name__ == '__main__':
    server = Server()
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(server.handle_echo, 'localhost', 8001, loop=loop)
    server_ = loop.run_until_complete(coro)
    print(f"Deploy on {server_.sockets[0].getsockname()}\n")
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server_.close()
        loop.run_until_complete(server_.wait_closed())
        loop.close()
        print('\n', 'You closed applications using the keyboard')
