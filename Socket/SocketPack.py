import struct

class SocketPack:
    def __init__(self) -> None:
        self.m_packet = bytearray()
        pass

    def write_byte(self, value):
        self.m_packet.extend(struct.pack('>B', value))
        return
    
    def write_short(self, value):
        self.m_packet.extend(struct.pack('>H', value))
        return
    
    def write_int(self, value):
        self.m_packet.extend(struct.pack('>I', value))
        return
    
    def write_bytes(self, value):
        self.m_packet.extend(struct.pack(f"{len(value)}s", value))
        return
    
    def print(self):
        print(list(self.m_packet))