import os    
from Socket.SocketBase import SocketBase
from Socket.SocketPack import SocketPack
from PublicFun import generateSend
from PublicFun import generateReceive
from PublicFun import MAPLESTORY_SERVER_VERSION 


class SocketLogin(SocketBase): 
    def __init__(self, ip:str, port:int, time_out:int = 30):
        super().__init__(ip, port, time_out)
        pass
 
    async def socket_connect(self, addr:tuple, output_data:bytearray) -> int:
        '''
            当客户端建立连接请求时会进入此回调

            addr: 客户端连接IP和端口
            output_data: 建立连接请求时如果需发送数据包给客户端从此处返回

            返回值: int类型
                0: 继续监听客户端过来的数据包
                1: 拒绝客户端建立连接, 将主动断开客户端接入的TCP请求
        '''
        
 
        ivsend = generateSend()
        ivrecv = generateReceive()

        inpack = SocketPack()
        inpack.write_byte(0xE)
        inpack.write_byte(MAPLESTORY_SERVER_VERSION)
        inpack.write_byte(1)
        inpack.write_byte(49)
        inpack.write_bytes(ivrecv)
        inpack.write_bytes(ivsend)
        inpack.write_byte(8)
   
        output_data.extend(bytearray(inpack.m_packet))

        return 0

    async def socket_callback(self, addr:tuple, input_data:bytes, output_data:bytearray) -> int:
        '''
            当收到客户端数据包时会进入此回调

            addr: 客户端连接IP和端口
            intpu_data: 客户端发送过来的数据包
            output_data: 建立连接请求时如果需发送数据包给客户端从此处返回

            返回值: int类型
                0: 继续监听客户端过来的数据包
                1: 拒绝客户端建继续连接, 将主动断开客户端接入的TCP请求
        '''
        return
    