import asyncio
from Socket.SocketPack import SocketPack

class SocketMessage():
    def __init__(self
            , address:tuple
            , reader:asyncio.StreamReader
            , writer:asyncio.StreamWriter
            , time_out:int = 30) -> None:
        self.m_address = address
        self.m_reader = reader
        self.m_writer = writer
        self.m_time_out = time_out
        pass
  
    async def read_pack(self
                        , read_len:int) -> bytes:
        '''
            接受来自socket的数据包

            read_len: 读取socket包长度
        '''
        try:
            input_data:bytes = await asyncio.wait_for(self.m_reader.read(read_len), timeout=self.m_time_out)
        except asyncio.TimeoutError:
            raise asyncio.TimeoutError(e)
        except ConnectionResetError as e: 
            raise ConnectionResetError(e)
        except asyncio.CancelledError as e:
            raise asyncio.CancelledError(e)
        except Exception as e:
            print(f"Error with client {e}")
            return None 
  
        return input_data
    
    async def read_int(self) -> int:
        value =  await self.read_pack(4)
        return int.from_bytes(value, byteorder='big')
    
    async def write_pack(self
                         , output_data:SocketPack = None):
        '''
            向socket发送数据包
        '''

        if output_data == None:
            return
        
        if len(output_data.m_packet) == 0:
            return
        
        self.m_writer.write(output_data.to_bytearray())
        await self.m_writer.drain()  # 确保数据已发送