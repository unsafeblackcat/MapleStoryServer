import ctypes
from Crypto.Cipher import AES



class MapleAESOFB:
    def __init__(self, iv:list, maple_version:int):
        self.m_iv = iv   
        self.m_maple_version \
            = ctypes.c_short(((maple_version >> 8) & 0xFF) | ((maple_version << 8) & 0xFF00)).value
        
        key = [0x13, 0x00, 0x00, 0x00
            , 0x08, 0x00, 0x00, 0x00
            , 0x06, 0x00, 0x00, 0x00
            , ctypes.c_byte(0xB4), 0x00, 0x00, 0x00
            , 0x1B, 0x00, 0x00, 0x00
            , 0x0F, 0x00, 0x00, 0x00
            , 0x33, 0x00, 0x00, 0x00
            , 0x52, 0x00, 0x00, 0x00]

        c_array = ctypes.c_byte * len(key)  # 创建一个 C 类型的数组
        c_array_data = c_array(*key)
        self.m_cipher = AES.new(c_array_data, AES.MODE_ECB)
        pass

    def is_valid_header(self, header:int) -> bool: 
        
        packet_header_buf = list() 
        packet_header_buf.append(ctypes.c_byte(((header >> 24) & 0xFF)).value)
        packet_header_buf.append(ctypes.c_byte(((header >> 16) & 0xFF)).value)
        # 41, 2
        return self.check_packet(packet_header_buf)
    
    def check_packet(self, packet:list) -> bool:
        v1 = ctypes.c_byte(packet[0]).value
        v2 = ctypes.c_byte(self.m_iv[2]).value

        v3 = ctypes.c_byte((v1 ^ v2) & 0xFF).value
        v4 = ctypes.c_byte((self.m_maple_version >> 8) & 0xFF).value

        b1 = (v3 == v4)
 
        v1 = ctypes.c_byte(packet[1]).value
        v2 = ctypes.c_byte(self.m_iv[3]).value
        v3 = ctypes.c_byte(v1 ^ v2).value
        v4 = ctypes.c_byte(v3 & 0xFF)

        v3 = ctypes.c_byte((v1 ^ v2) & 0xFF).value
        v4 = ctypes.c_byte(self.m_maple_version & 0xFF).value
        b2 = (v3 == v4)

        return (b1) and (b2)