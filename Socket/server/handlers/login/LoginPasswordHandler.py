from Socket.PacketHandler import PacketHandler
from Socket.SocketMessage import SocketMessage
from Socket.server.PacketCreator import PacketCreator

'''
    用户登录协议处理. 
'''
class LoginPasswordHandler(PacketHandler):
    def __init__(self):
        super().__init__()
        return
    
    async def handle_packet(
            self
            , message:SocketMessage):
        '''
            处理登录回调.
        '''
        if message.m_address[0] == None:
            message.write_pack(PacketCreator.get_login_failed(14))
            return
        
        login:str = message.read_string()
        pwd:str = message.read_string()

        message.skip(6)

        hwidNibbles = message.read_pack(4)


        return
    
    async def validate_state(self):
        return super().validate_state()