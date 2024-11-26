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

        print(f"Connection with {addr} was cancelled.")
          
        try:
            output_data = bytearray()
            iret = await self.socket_connect(addr, output_data)
            if iret:
                return

            await self._write(addr, writer, output_data)
            output_data.clear()
 
            while True:
                # 从客户端读取数据 
                input_data = await self._read(self, reader)
                if reader.at_eof():
                    print(f'{addr} close')
                    break

                print(input_data)
  
                output_data = bytearray()
                await self.socket_callback(addr, input_data, output_data)
                await self._write(addr, writer, output_data)
                output_data.clear()
                pass
  
        except asyncio.CancelledError:
            print(f"Connection with {addr} was cancelled.")
        except ConnectionResetError as e:
            print(f"Connection with {addr} was cancelled. {e}")
        finally:
            writer.close()
            await writer.wait_closed()

    async def _read(self, addr:tuple, reader:asyncio.StreamReader) -> int:
        
        try:
            input_data:bytes = await asyncio.wait_for(reader.read(1024), timeout=self.m_time_out)
        except asyncio.TimeoutError:
            print(f"Connection from {addr} timed out.") 
            return None 
        except ConnectionResetError as e: 
            raise ConnectionResetError(e)
        except asyncio.CancelledError as e:
            raise asyncio.CancelledError(e)
        except Exception as e:
            print(f"Error with client {addr}: {e}")
            return None 
 
        await self._decode(input_data)
        return input_data
    
    async def _write(self, addr:tuple, writer:asyncio.StreamWriter, output_data:bytearray = None):
        
        if output_data == None:
            return
        
        if len(output_data) == 0:
            return

        #await self._encode(output_data)
        writer.write(output_data)
        await writer.drain()  # 确保数据已发送
        return
    
    async def _decode(self, input_data:bytes):
        return
    
    async def _encode(self, output_data:bytearray):
        return

    async def socket_connect(self, addr:tuple, output_data:bytearray) -> int:
        '''
            当客户端建立连接请求时会进入此回调

            addr: 客户端连接IP和端口
            output_data: 建立连接请求时如果需发送数据包给客户端从此处返回

            返回值: int类型
                0: 继续监听客户端过来的数据包
                1: 拒绝客户端建立连接, 将主动断开客户端接入的TCP请求
        '''
        return 0

    async def socket_callback(self, addr:tuple, input_data:bytes, output_data:bytearray) -> int:
        '''
            当收到客户端数据包时会进入此回调

            addr: 客户端连接IP和端口
            intpu_data: 客户端发送过来的数据包
            output_data: 建立连接请求时如果需发送数据包给客户端从此处返回

            返回值: int类型
                0: 继续监听客户端过来的数据包
                1: 拒绝客户端建继续连接, 将主动断开客户端接入的TCP请求
        '''
        return