from Socket.PacketHandler import PacketHandler
from Socket.SocketMessage import SocketMessage

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
            message.write_pack()
            return
        

        return
    
    async def validate_state(self):
        return super().validate_state()