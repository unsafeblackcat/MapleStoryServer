from Socket.PacketHandler import PacketHandler
from Socket.SocketMessage import SocketMessage

'''
    登录后pin(安全码)验证逻辑
    不过北斗客户端好像没有pin的按钮和处理.
'''
class AfterLoginHandler(PacketHandler):
    def __init__(self):
        super().__init__()
        return
    
    async def handle_packet(
            self
            , message:SocketMessage):
        '''

        '''
        c2 = await message.read_bytes()
        c3 = 5

        if await message.is_eof() == False:
            pass
        else: 
            c3 = message.read_bytes()
            pass
        
        if c2 == 1 and c3 == 1:
            pass
        elif c2 == 1 and c3 == 0:
            pass
        elif c2 == 2 and c3 == 0:
            pass
        elif c2 == 0 and c3 == 5:
            pass
        else:
            pass

        return
    
    async def validate_state(self):
        return super().validate_state()