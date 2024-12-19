import asyncio
import ctypes 
import array

from datetime import datetime
from Socket.SocketMessage import SocketMessage
from Socket.SocketPack import SocketPack

class SocketBase():  
    def __init__(
            self
            , ip:str
            , port:int
            , time_out:int = 30): 
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
         

    async def _socket_callback(
            self
            , reader:asyncio.StreamReader
            , writer:asyncio.StreamWriter):
        
        addr:tuple = writer.get_extra_info('peername')  
         
        message = SocketMessage(addr, reader, writer, self.m_time_out)

        try: 
            if await self.socket_connect(message):
                return
            
            currentime:int = 0
            is_time_out:bool = False
            
            while (True):
                try:
                    opcode_buffer:array = await message.read_header()
                    await self.opcode_process(opcode_buffer, message) 
                except asyncio.TimeoutError as e:
                    if is_time_out:
                        raise asyncio.TimeoutError(e)
                    else:
                        currentime = int(datetime.now().timestamp() * 1000) 
                        inpack = SocketPack() 
                        inpack.write_short(0x11)
                        await message.write_pack(inpack) 
                        is_time_out = True 
                        continue
                    pass # except asyncio.TimeoutError as e:
                pass # while (True):
               
        except asyncio.InvalidStateError as e:
            print(f"{addr}: {e}")
        except asyncio.TimeoutError as e:
            print(f"Connection with {addr} was cancelled.")
        except asyncio.CancelledError:
            print(f"Connection with {addr} was cancelled.")
        except ConnectionResetError as e:
            print(f"Connection with {addr} was cancelled. {e}")
        finally:
            writer.close()
            await writer.wait_closed()
            self.socket_close(addr)
  
    async def socket_connect(
            self
            , message:SocketMessage) -> int:
        '''
            当客户端建立连接请求时会进入此回调

            addr: 客户端连接IP和端口 

            返回值: int类型
                0: 继续监听客户端过来的数据包
                1: 拒绝客户端建立连接, 将主动断开客户端接入的TCP请求
        '''
        return 0

    async def opcode_process(
            self
            , opcode_buffer:array
            , message:SocketMessage) -> int:
        '''
            opcode消息过程
            opcode_buffer: socket接受解码后的数据  
            message: 和客户端通讯类
        '''
        return
    

    async def socket_close(self
            , address:tuple):
        '''
            socket 关闭后用于清理数据
        '''
        return 