from Socket.PacketHandler import PacketHandler

'''
    新建账户首次登陆, 协议按钮选择回调
'''
class AcceptToSHandler(PacketHandler):
    def __init__(self):
        super().__init__()
        return
    
    async def handle_packet(self, message):
        '''
            首次登陆的账户, 协议按钮处理
            当用户选中[取消]: 客户端会直接退出游戏, 服务端也需要吧客户端内容给清理掉. 
            当用户选中[确认]: 
                判断当前账户是否登录成功
                    当前账户登录成功, 成功返回数据包. 
                    当前登录登录失败, 失败返回数据包.  
                    不管是登录成功还是失败, 服务端不会强制断开TCP连接. 
        '''
        return 
    
    async def validate_state(self):
        return super().validate_state()