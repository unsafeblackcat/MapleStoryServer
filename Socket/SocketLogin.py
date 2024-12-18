import asyncio 
import array
from Socket.SocketBase import SocketBase
from Socket.SocketPack import SocketPack
from Socket.SocketMessage import SocketMessage
from Socket.PacketHandler import PacketHandler 
from Socket.server.PackProcess import PackProcess
from Socket.opcodes.LoginOpcode import EnumLoginOpCode
from Socket.server.handlers.login.AcceptToSHandler import AcceptToSHandler
from PublicFun import MAPLESTORY_SERVER_VERSION 
 
 
class SocketLogin(SocketBase): 
    def __init__(
            self
            , ip:str
            , port:int
            , time_out:int = 30): 
        super().__init__(ip, port, time_out)
 
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
       
        inpack = SocketPack()
        inpack.write_short(0xE)
        inpack.write_short(MAPLESTORY_SERVER_VERSION)
        inpack.write_short(1)
        inpack.write_byte(49)
        inpack.write_bytes(message.m_iv_recv)
        inpack.write_bytes(message.m_iv_send)
        inpack.write_byte(8)  
        await message.write_pack(inpack, False)
        return 0
      
    async def opcode_process(
            self
            , opcode_buffer:array
            , message:SocketMessage) -> int:
      
        if EnumLoginOpCode.__contains__(opcode_buffer[0]):
            handle:PacketHandler = self.m_process_handle.get(opcode_buffer[0])
            if handle.validate_state():
                handle.handle_packet(message)
                pass # if handle.validate_state():
            pass # if EnumLoginOpCode.__contains__(array_packet[0]):

        pass
        return