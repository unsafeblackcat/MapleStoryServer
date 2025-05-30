import asyncio
import ctypes
import array

from Socket.SocketPack import SocketPack
from Socket.MapleAESOFB import MapleAESOFB 
from Socket.MapleCustomEncryption import *

from PublicFun import generateSend
from PublicFun import generateReceive 
from PublicFun import MAPLESTORY_SERVER_VERSION 
 


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
 
        self.m_iv_send = list()
        self.m_iv_recv = list()
        self.m_sender:MapleAESOFB
        self.m_receive:MapleAESOFB

        self.m_iv_send = generateSend()
        self.m_iv_recv = generateReceive()

        self.m_sender = MapleAESOFB(
            self.m_iv_send
            , ctypes.c_short(0xFFFF - MAPLESTORY_SERVER_VERSION).value)
        self.m_receive = MapleAESOFB(
            self.m_iv_recv
            , MAPLESTORY_SERVER_VERSION)
        pass

    async def is_eof(self) -> bool:
        return await self.m_reader.at_eof()
  
    async def read_pack(self
                        , read_len:int) -> bytes:
        '''
            接受来自socket的数据包

            read_len: 读取socket包长度
        '''
        try:
            recv_data:bytes = await asyncio.wait_for(self.m_reader.read(read_len), timeout=self.m_time_out)
            if len(recv_data) == 0:
                raise asyncio.InvalidStateError("读取数据None, Socket异常客户端可能断开....")
        except asyncio.TimeoutError as e:
            raise asyncio.TimeoutError(e)
        except ConnectionResetError as e: 
            raise ConnectionResetError(e)
        except asyncio.CancelledError as e:
            raise asyncio.CancelledError(e)
  
        return recv_data
    
    async def skip(self, number:int):
        await self.read_bytes(number)
        return
    
    async def read_bytes(self) -> int:
        recv_data:bytes = await self.read_pack(1)
        ret:int = int.from_bytes(recv_data, byteorder='big')
        return ret
     
    async def read_short(self) -> int: 
        return self.read_pack(2)
    
    async def read_string(self) -> str: 
        str_len:int = self.read_short() 
        str = self.read_bytes(str_len) 
        return str
    
    async def read_header(self) -> array:
        recv_data:bytes = await self.read_pack(4)
        header:int = int.from_bytes(recv_data, byteorder='big')
 
        loop = asyncio.get_running_loop()

        bret:bool = await loop.run_in_executor(
            None
            , self.m_receive.is_valid_header
            , header) 
        if  bret == False:
            print(f"login: {self.m_ip} is_valid_header false")
            pass

        packet_length:int = await self.decode_packet_length(header)
        
        packet = await self.read_pack(packet_length)
        array_packet:array = array.array('b', packet)
  
        await loop.run_in_executor(
            None
            , self.m_receive.crypt
            , array_packet) 
         
        array_packet = await loop.run_in_executor(
            None
            , MapleCustomEncryption.decryptData
            , array_packet)   
 
        return array_packet
    
    async def write_pack(self
                         , socket_pack:SocketPack = None
                         , encode:bool = True):
        '''
            向socket发送数据包
        '''

        if socket_pack == None:
            return
        
        if len(socket_pack.m_packet) == 0:
            return
        
        send_array = bytearray()
        if encode:
            send_array = await self.encode(socket_pack)
            pass
        else:
            send_array = socket_pack.to_bytearray()
        
        self.m_writer.write(send_array)
        await self.m_writer.drain()  # 确保数据已发送

     
    async def decode_packet_length(self, header:int) -> int:
        length:int = (ctypes.c_uint32(header).value >> 16) ^ (header & 0xFFFF)
        length = (ctypes.c_uint32(length << 8).value & 0xFF00) | (ctypes.c_uint32(length >> 8).value & 0xFF)
        return length 
    
    async def encode(self, socket_pack:SocketPack) -> bytearray:
        
        loop = asyncio.get_running_loop()

        encode_pack:SocketPack = SocketPack()

        packet_head:array = await loop.run_in_executor(
            None
            , self.m_sender.getPacketHeader
            , len(socket_pack.to_bytearray())) 
         
        encode_pack.write_bytes(array.array.tobytes(packet_head))
  
        list_packet = await loop.run_in_executor(
            None
            , MapleCustomEncryption.encryptData
            , socket_pack.to_bytearray())    
        
        self.m_sender.crypt(list_packet)  

        encode_pack.write_list(list_packet)

        return encode_pack.to_bytearray()