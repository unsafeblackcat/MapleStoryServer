import os    
from Socket.SocketBase import SocketBase

class SocketLogin(SocketBase): 
    def __init__(self, ip:str, port:int, time_out:int = 30):
        super().__init__(ip, port, time_out)
        pass
 
    # 返回值: 1, 如果需要给客户端返回数据包
    # 返回值: 0, 不需要给客户端返回数据包
    async def socket_connect(self, addr:tuple, output_data: bytearray = None) -> int:
        return 0

    # 返回值: 1, 如果需要给客户端返回数据包
    # 返回值: 0, 不需要给客户端返回数据包
    async def socket_callback(self, addr:tuple, input_data:bytes = None, output_data: bytearray = None) -> int:
        return
    