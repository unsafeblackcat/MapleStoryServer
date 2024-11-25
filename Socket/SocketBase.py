import asyncio

class SocketBase():  
    def __init__(self, ip:str, port:int, time_out:int = 30):
        self.m_ip = ip
        self.m_port = port
        self.m_server = None
        self.m_time_out = time_out
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
        addr:tuple = writer.get_extra_info('peername') 
        sock = writer.get_extra_info("socket")

          
        try:
            output_data = bytearray()
            await self.socket_connect(addr, output_data)
            await self._write(self, addr, output_data)
            output_data.clear()
 
            while True:
                # 从客户端读取数据
                input_data = await self._read(self, reader)

                if writer.is_closing():
                    break
  
                output_data = bytearray()
                await self.socket_callback(addr, input_data, output_data)
                await self._write(self, addr, output_data)
                output_data.clear()
                pass
  
        except asyncio.CancelledError:
            print(f"Connection with {addr} was cancelled.")
        finally:
            writer.close()
            await writer.wait_closed()

    async def _read(self, addr:tuple, reader:asyncio.StreamReader) -> bytes:
        
        try:
            input_data:bytes = await asyncio.wait_for(reader.read(), timeout=self.m_time_out)
        except asyncio.TimeoutError:
            print(f"Connection from {addr} timed out.") 
            return None 
 
        await self._decode(input_data)
        return input_data, 0
    
    async def _write(self, addr:tuple, writer:asyncio.StreamWriter, output_data:bytearray = None):
        
        if output_data == None:
            return
        
        if len(output_data) == 0:
            return

        await self._encode(output_data)
        writer.write(output_data)
        await writer.drain()  # 确保数据已发送
        return
    
    async def _decode(self, input_data:bytes):
        return
    
    async def _encode(self, output_data:bytearray):
        return

    async def socket_connect(self, addr:tuple, output_data:bytearray = None) -> int:
        return 0

    async def socket_callback(self, addr:tuple, input_data:bytes = None, output_data:bytearray = None) -> int:
        return