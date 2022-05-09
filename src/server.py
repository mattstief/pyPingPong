#server
import helpers #helpers.py
import asyncio
import socket
import random

sender = "SERVER"

async def runServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((helpers.HOST, helpers.PORT))
    while(True):
        try:
            response = await helpers.getResponse(server, 5.0)
            helpers.printResponse(sender, response[0])
            randFloat = random.random()
            if(randFloat <= 0.7):
                helpers.sendMessage(sender, server, response[1], "pong")
        except Exception as e:
            print(f'[{sender}] {e}')


async def main():
    try:
        await runServer()
    except Exception as e:
        print(e)


asyncio.run(main())


