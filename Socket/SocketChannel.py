import os    
from Socket.SocketBase import *

class SocketChannel(SocketBase): 
    def __init__(self, ip:str, port:int, time_out:int = 30):
        super().__init__(ip, port, time_out)
        pass

    async def _socket_callback(self, reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
        pass

    
    