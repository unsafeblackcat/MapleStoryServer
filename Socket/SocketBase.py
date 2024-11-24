import asyncio

class SocketBase():  
    def __init__(self, ip:str, port:int):
        self.m_ip = ip
        self.m_port = port
        self.m_server = None
        pass 
           
    async def run(self) -> int:
        iret:int = 1

        try:
            self.m_server = await asyncio.start_server(
                self._socket_callback
                , self.m_ip
                , self.m_port)
            iret = 0
        except Exception as e:
            print(f"Failed to start server: {e}")  
            pass
        
        return iret
         

    async def _socket_callback(self, reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
        pass