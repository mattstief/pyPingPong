#client.py
import helpers #helpers.py
import socket
import asyncio

sender = "CLIENT"

async def runClient():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    messagesSent, pongCount = 0, 0
    while True:
        if(messagesSent < 10):
            messagesSent += 1
            helpers.sendMessage(sender, client, (helpers.HOST, helpers.PORT), "ping")
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
    pongCount, totalCount, usrInput = 0, 0, 'y'
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
