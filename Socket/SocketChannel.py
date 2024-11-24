import os    
from Socket.SocketBase import *

class SocketChannel(SocketBase): 
    def __init__(self, ip:str, port:int):
        super().__init__(ip, port)
        pass

    async def _socket_callback(self, reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
        pass

    
    