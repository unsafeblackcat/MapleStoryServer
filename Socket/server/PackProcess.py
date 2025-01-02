from Socket.PacketHandler import PacketHandler
from Socket.opcodes.LoginOpcode import EnumLoginOpCode

class PackProcess():
    def __init__(self):
        self.m_handle = dict()
        pass

    def register_handle(self, id:int, handle:PacketHandler):
        self.m_handle[id] = handle
        return
    
    async def get(self, id:int) -> PacketHandler: 
        return self.m_handle.get(id)