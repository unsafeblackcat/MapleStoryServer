import os    
import asyncio
from Socket.SocketBase import SocketBase
from Socket.SocketPack import SocketPack
from Socket.SocketMessage import SocketMessage
from PublicFun import generateSend
from PublicFun import generateReceive
from PublicFun import MAPLESTORY_SERVER_VERSION 

class SocketLogin(SocketBase): 
    def __init__(
            self
            , ip:str
            , port:int
            , time_out:int = 30): 
        super().__init__(ip, port, time_out)
        pass
 
    async def socket_connect(
            self
            , message:SocketMessage) -> int:
        '''
            当客户端建立连接请求时会进入此回调

            addr: 客户端连接IP和端口 

            返回值: int类型
                0: 继续监听客户端过来的数据包
                1: 拒绝客户端建立连接, 将主动断开客户端接入的TCP请求
        '''
         
        ivsend = generateSend()
        ivrecv = generateReceive()

        inpack = SocketPack()
        inpack.write_short(0xE)
        inpack.write_short(MAPLESTORY_SERVER_VERSION)
        inpack.write_short(1)
        inpack.write_byte(49)
        inpack.write_bytes(ivrecv)
        inpack.write_bytes(ivsend)
        inpack.write_byte(8) 
        await message.write_pack(inpack)  
        return 0

    async def socket_loop(
            self
            , message:SocketMessage) -> int:
        '''
            socket消息循环, 当函数返回时表明可以关闭socket  
        '''

        try: 
            while True:
                head = await message.read_int()
                
                pass
             
        except asyncio.CancelledError:
            print(f"Connection with {self.m_ip} was cancelled.")
        except ConnectionResetError as e:
            print(f"Connection with {self.m_ip} was cancelled. {e}")
        finally:
            pass
        
        return
    