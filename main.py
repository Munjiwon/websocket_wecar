import asyncio
import websockets

import os
import subprocess
import threading
from time import sleep

async def echo(websocket, path):
    print("start websocket")
    async for message in websocket:

        print(message)
        sleep(3)
        await websocket.send("print")

#ipconfig 주소
start_server = websockets.serve(echo, "203.250.35.33", 5000)

if "__main__" == __name__:

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

    # asyncio.run(main())