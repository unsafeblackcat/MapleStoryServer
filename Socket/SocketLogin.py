import os    
import asyncio
import ctypes
from Socket.SocketBase import SocketBase
from Socket.SocketPack import SocketPack
from Socket.SocketMessage import SocketMessage
from Socket.MapleAESOFB import MapleAESOFB
from PublicFun import generateSend
from PublicFun import generateReceive
from PublicFun import MAPLESTORY_SERVER_VERSION 

class SocketLogin(SocketBase): 
    def __init__(
            self
            , ip:str
            , port:int
            , time_out:int = 30): 
        super().__init__(ip, port, time_out)

        self.m_iv_send = list()
        self.m_iv_recv = list()
        self.m_encode:MapleAESOFB
        self.m_decode:MapleAESOFB

        pass
 
    async def socket_connect(
            self
            , message:SocketMessage) -> int: 
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.socket_connect_ex)
           
        inpack = SocketPack()
        inpack.write_short(0xE)
        inpack.write_short(MAPLESTORY_SERVER_VERSION)
        inpack.write_short(1)
        inpack.write_byte(49)
        inpack.write_bytes(self.m_iv_recv)
        inpack.write_bytes(self.m_iv_send)
        inpack.write_byte(8)  
        await message.write_pack(inpack)
 
        return 0

    async def socket_loop(
            self
            , message:SocketMessage) -> int:
       
        header = await message.read_int()
 
        loop = asyncio.get_running_loop()
        bret:bool = await loop.run_in_executor(None, self.m_decode.is_valid_header, header)

        if  bret == False:
            print(f"login: {self.m_ip} is_valid_header false")
            pass

        packet_length:int = await loop.run_in_executor(None, self.decode_packet_length, header)
        
        packet = await message.read_pack(packet_length)
        list_packet = list(packet)

        return
    
    def socket_connect_ex(self):
        self.m_iv_send = generateSend()
        self.m_iv_recv = generateReceive()

        self.m_encode = MapleAESOFB(self.m_iv_send, ctypes.c_short(0xFFFF - MAPLESTORY_SERVER_VERSION).value)
        self.m_decode = MapleAESOFB(self.m_iv_recv, MAPLESTORY_SERVER_VERSION)
        return