from Socket import SocketMessage


class PacketHandler:
    def __init__(self):
        pass
 
    async def handle_packet(self, message:SocketMessage):
        pass

    async def validate_state(self) -> bool:
        return True
