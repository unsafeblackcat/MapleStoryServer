from Socket.PacketHandler import PacketHandler

class Pone(PacketHandler):
    def __init__(self):
        super().__init__()
        return
    
    async def handle_packet(self, message):
        return super().handle_packet(message)
    
    async def validate_state(self):
        return super().validate_state()