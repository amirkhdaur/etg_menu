import websockets
import asyncio
import json
from etg import Menu


HOST = '26.72.213.193'
PORT = 9090

connected = set()

menu = Menu()


async def echo(websocket, path):
    async for message in websocket:
        try:
            json_string = json.loads(message)
            blanks = int(json_string.get('blanks'))
            heart = float(json_string.get('heart'))
            print(blanks, heart)
            menu.set_amount_blanks(blanks)
            menu.set_amount_health(heart)
        except (json.decoder.JSONDecodeError, ValueError):
            pass


start_server = websockets.serve(echo, HOST, PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
