HOST = '127.0.0.1'
PORT = 35491

def sendMessage(sender, socketFrom, host_port, message):
    print(f'[{sender}] sent {message}....')
    socketFrom.sendto(bytes((message), encoding='utf8'), (host_port[0], host_port[1]))

def printResponse(sender, data):
    if(data):
        print(f'[{sender}] received {data.decode("utf-8")}\n')

async def getResponse(socket, timeout=5.0):
    socket.settimeout(timeout)
    data, addr = socket.recvfrom(1024)
    return data, addr

