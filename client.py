#client.py
import helpers
import socket
import asyncio

HOST = '127.0.0.1'
PORT = 35491
sender = "CLIENT"

async def runClient():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    messagesSent = 0
    pongCount = 0
    while True:
        if(messagesSent < 10):
            messagesSent += 1
            helpers.sendMessage(sender, client, (HOST, PORT), "ping")
            try: 
                response = await helpers.getResponse(client, 0.8)
                helpers.printResponse(sender, response[0])
                pongCount += 1
            except Exception as e:
                print(f'[{sender}] {e}')
        else:
            break
    client.close()
    return pongCount

async def main():    
    pongCount = 0
    totalCount = 0
    usrInput = 'y'
    while(usrInput[0] == 'y'):
        try:
            pongCount += await runClient()
            totalCount += 10
        except Exception as e:
            print(e)
        finally: 
            print(f'pongs/total: {pongCount}/{totalCount}')
            usrInput = input("Continue?(y/n): ")

asyncio.run(main())