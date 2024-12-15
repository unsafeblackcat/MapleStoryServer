import os    
import asyncio
import ctypes
import array
from Socket.SocketBase import SocketBase
from Socket.SocketPack import SocketPack
from Socket.SocketMessage import SocketMessage
from Socket.MapleAESOFB import MapleAESOFB
from PublicFun import generateSend
from PublicFun import generateReceive
from PublicFun import MAPLESTORY_SERVER_VERSION 
from Socket.MapleCustomEncryption import *

class SocketLogin(SocketBase): 
    def __init__(
            self
            , ip:str
            , port:int
            , time_out:int = 30): 
        super().__init__(ip, port, time_out)

        self.m_iv_send = list()
        self.m_iv_recv = list()
        self.m_sender:MapleAESOFB
        self.m_receive:MapleAESOFB

        pass
 
    async def socket_connect(
            self
            , message:SocketMessage) -> int: 
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(
            None
            , self._socket_connect_init)
           
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
    
    def _socket_connect_init(self):
        self.m_iv_send = generateSend()
        self.m_iv_recv = generateReceive()

        self.m_sender = MapleAESOFB(
            self.m_iv_send
            , ctypes.c_short(0xFFFF - MAPLESTORY_SERVER_VERSION).value)
        self.m_receive = MapleAESOFB(
            self.m_iv_recv
            , MAPLESTORY_SERVER_VERSION)
        return

    async def socket_loop(
            self
            , message:SocketMessage) -> int:
       
        try:
            header = await message.read_int()
        except asyncio.TimeoutError: 
            pass

        loop = asyncio.get_running_loop()
        bret:bool = await loop.run_in_executor(
            None
            , self.m_receive.is_valid_header
            , header) 
        if  bret == False:
            print(f"login: {self.m_ip} is_valid_header false")
            pass

        packet_length:int = await loop.run_in_executor(
            None
            , self.decode_packet_length
            , header)
        
        packet = await message.read_pack(packet_length)
        array_packet:array = array.array('b', packet)
  
        await loop.run_in_executor(
            None
            , self.m_receive.crypt
            , array_packet) 
         
        array_packet = await loop.run_in_executor(
            None
            , MapleCustomEncryption.decryptData
            , array_packet)  
        i = 0

        return