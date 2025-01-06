
from datetime import datetime

from Socket.PacketHandler import PacketHandler
from Socket.SocketBase import SocketBase


class Pone(PacketHandler):
    def __init__(self, sb:SocketBase):
        super().__init__()
        self.m_sb = sb
        return
    
    async def handle_packet(self, message):
        super().handle_packet(message)
        self.m_sb.m_last_pong = int(datetime.now().timestamp() * 1000) 
        return 
    
    async def validate_state(self):
        return super().validate_state()