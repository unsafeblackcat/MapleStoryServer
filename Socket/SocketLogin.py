import os    
import asyncio
import ctypes
import array
from Socket.SocketBase import SocketBase
from Socket.SocketPack import SocketPack
from Socket.SocketMessage import SocketMessage
from Socket.PacketHandler import PacketHandler
from Socket.MapleAESOFB import MapleAESOFB
from Socket.server.PackProcess import PackProcess
from Socket.opcodes.LoginOpcode import EnumLoginOpCode
from Socket.server.handlers.login.AcceptToSHandler import AcceptToSHandler

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
        self.m_process_handle:PackProcess = PackProcess()
        self.m_process_handle.register_handle(EnumLoginOpCode.ACCEPT_TOS, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.AFTER_LOGIN, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.SERVERLIST_REREQUEST, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.CHARLIST_REQUEST, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.CHAR_SELECT, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.LOGIN_PASSWORD, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.RELOG, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.SERVERLIST_REQUEST, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.SERVERSTATUS_REQUEST, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.CHECK_CHAR_NAME, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.CREATE_CHAR, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.DELETE_CHAR, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.VIEW_ALL_CHAR, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.PICK_ALL_CHAR, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.REGISTER_PIN, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.GUEST_LOGIN, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.REGISTER_PIC, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.CHAR_SELECT_WITH_PIC, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.SET_GENDER, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.VIEW_ALL_WITH_PIC, AcceptToSHandler())
        self.m_process_handle.register_handle(EnumLoginOpCode.VIEW_ALL_PIC_REGISTER, AcceptToSHandler())

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
 
        header = await message.read_int()
 
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

        if EnumLoginOpCode.__contains__(array_packet[0]):
            handle:PacketHandler = self.m_process_handle.get(array_packet[0])
            if handle.validate_state():
                handle.handle_packet(message)
                pass # if handle.validate_state():
            pass # if EnumLoginOpCode.__contains__(array_packet[0]):




        header = await message.read_int()
 
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

        if EnumLoginOpCode.__contains__(array_packet[0]):
            handle:PacketHandler = await self.m_process_handle.get(array_packet[0])
            if await handle.validate_state():
                await handle.handle_packet(message)
                pass # if handle.validate_state():
            pass # if EnumLoginOpCode.__contains__(array_packet[0]):
        return