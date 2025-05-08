from Socket.SocketPack import SocketPack
from Socket.server.opcodes.ServerSendOpcode import ServerSendOpcode


class PacketCreator():
    
    def get_login_failed(number:int) -> SocketPack:
        inpack = SocketPack()
        inpack.write_short(ServerSendOpcode.LOGIN_STATUS.value)
        inpack.write_byte(number)
        inpack.write_byte(0)
        inpack.write_byte(0) 
        return inpack
    
    pass