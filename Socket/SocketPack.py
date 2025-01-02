import struct 
 
class SocketPack:
    def __init__(self) -> None:
        self.m_packet = bytearray()
        pass

    def write_byte(self, value):
        self.m_packet.extend(struct.pack('<B', value))
        return
    
    def write_short(self, value):
        self.m_packet.extend(struct.pack('<H', value))
        return
    
    def write_int(self, value):
        self.m_packet.extend(struct.pack('<I', value))
        return
    
    def write_bytes(self, value:bytes):
        self.m_packet.extend(struct.pack(f"{len(value)}s", value))
        return
    
    def write_list(self, value:list):
        byte_data = b''

        i:int = 0
        for it in value:
             
            if it < -128:
                it = -128
            elif it > 127:
                it = 127 

            byte_data += struct.pack('b', it) 
            pass

        self.write_bytes(byte_data)
        return

    def to_bytearray(self) -> bytearray:
        return bytearray(self.m_packet)

    def print(self):
        print(list(self.m_packet))