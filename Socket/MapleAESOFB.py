import array
import ctypes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class MapleAESOFB:
    def __init__(self, iv:list, maple_version:int):
        self.m_iv:list = iv   
        self.m_maple_version \
            = ctypes.c_short(((maple_version >> 8) & 0xFF) | ((maple_version << 8) & 0xFF00)).value
        
        self.key = [0x13, 0x00, 0x00, 0x00
            , 0x08, 0x00, 0x00, 0x00
            , 0x06, 0x00, 0x00, 0x00
            , ctypes.c_byte(0xB4).value, 0x00, 0x00, 0x00
            , 0x1B, 0x00, 0x00, 0x00
            , 0x0F, 0x00, 0x00, 0x00
            , 0x33, 0x00, 0x00, 0x00
            , 0x52, 0x00, 0x00, 0x00]

        c_array = ctypes.c_byte * len(self.key)  # 创建一个 C 类型的数组
        c_array_data = c_array(*self.key)
        self.m_cipher = AES.new(c_array_data, AES.MODE_ECB)

        self.funny_bytes:array = array.array(
            'b'
            , [ctypes.c_byte(0xEC).value, ctypes.c_byte(0x3F).value, ctypes.c_byte(0x77).value, ctypes.c_byte(0xA4).value, ctypes.c_byte(0x45).value, ctypes.c_byte(0xD0).value, ctypes.c_byte(0x71).value, ctypes.c_byte(0xBF).value,
ctypes.c_byte(0xB7).value, ctypes.c_byte(0x98).value, ctypes.c_byte(0x20).value, ctypes.c_byte(0xFC).value, ctypes.c_byte(0x4B).value, ctypes.c_byte(0xE9).value, ctypes.c_byte(0xB3).value, ctypes.c_byte(0xE1).value,
ctypes.c_byte(0x5C).value, ctypes.c_byte(0x22).value, ctypes.c_byte(0xF7).value, ctypes.c_byte(0x0C).value, ctypes.c_byte(0x44).value, ctypes.c_byte(0x1B).value, ctypes.c_byte(0x81).value, ctypes.c_byte(0xBD).value,
ctypes.c_byte(0x63).value, ctypes.c_byte(0x8D).value, ctypes.c_byte(0xD4).value, ctypes.c_byte(0xC3).value, ctypes.c_byte(0xF2).value, ctypes.c_byte(0x10).value, ctypes.c_byte(0x19).value, ctypes.c_byte(0xE0).value,
ctypes.c_byte(0xFB).value, ctypes.c_byte(0xA1).value, ctypes.c_byte(0x6E).value, ctypes.c_byte(0x66).value, ctypes.c_byte(0xEA).value, ctypes.c_byte(0xAE).value, ctypes.c_byte(0xD6).value, ctypes.c_byte(0xCE).value,
ctypes.c_byte(0x06).value, ctypes.c_byte(0x18).value, ctypes.c_byte(0x4E).value, ctypes.c_byte(0xEB).value, ctypes.c_byte(0x78).value, ctypes.c_byte(0x95).value, ctypes.c_byte(0xDB).value, ctypes.c_byte(0xBA).value,
ctypes.c_byte(0xB6).value, ctypes.c_byte(0x42).value, ctypes.c_byte(0x7A).value, ctypes.c_byte(0x2A).value, ctypes.c_byte(0x83).value, ctypes.c_byte(0x0B).value, ctypes.c_byte(0x54).value, ctypes.c_byte(0x67).value,
ctypes.c_byte(0x6D).value, ctypes.c_byte(0xE8).value, ctypes.c_byte(0x65).value, ctypes.c_byte(0xE7).value, ctypes.c_byte(0x2F).value, ctypes.c_byte(0x07).value, ctypes.c_byte(0xF3).value, ctypes.c_byte(0xAA).value,
ctypes.c_byte(0x27).value, ctypes.c_byte(0x7B).value, ctypes.c_byte(0x85).value, ctypes.c_byte(0xB0).value, ctypes.c_byte(0x26).value, ctypes.c_byte(0xFD).value, ctypes.c_byte(0x8B).value, ctypes.c_byte(0xA9).value,
ctypes.c_byte(0xFA).value, ctypes.c_byte(0xBE).value, ctypes.c_byte(0xA8).value, ctypes.c_byte(0xD7).value, ctypes.c_byte(0xCB).value, ctypes.c_byte(0xCC).value, ctypes.c_byte(0x92).value, ctypes.c_byte(0xDA).value,
ctypes.c_byte(0xF9).value, ctypes.c_byte(0x93).value, ctypes.c_byte(0x60).value, ctypes.c_byte(0x2D).value, ctypes.c_byte(0xDD).value, ctypes.c_byte(0xD2).value, ctypes.c_byte(0xA2).value, ctypes.c_byte(0x9B).value,
ctypes.c_byte(0x39).value, ctypes.c_byte(0x5F).value, ctypes.c_byte(0x82).value, ctypes.c_byte(0x21).value, ctypes.c_byte(0x4C).value, ctypes.c_byte(0x69).value, ctypes.c_byte(0xF8).value, ctypes.c_byte(0x31).value,
ctypes.c_byte(0x87).value, ctypes.c_byte(0xEE).value, ctypes.c_byte(0x8E).value, ctypes.c_byte(0xAD).value, ctypes.c_byte(0x8C).value, ctypes.c_byte(0x6A).value, ctypes.c_byte(0xBC).value, ctypes.c_byte(0xB5).value,
ctypes.c_byte(0x6B).value, ctypes.c_byte(0x59).value, ctypes.c_byte(0x13).value, ctypes.c_byte(0xF1).value, ctypes.c_byte(0x04).value, ctypes.c_byte(0x00).value, ctypes.c_byte(0xF6).value, ctypes.c_byte(0x5A).value,
ctypes.c_byte(0x35).value, ctypes.c_byte(0x79).value, ctypes.c_byte(0x48).value, ctypes.c_byte(0x8F).value, ctypes.c_byte(0x15).value, ctypes.c_byte(0xCD).value, ctypes.c_byte(0x97).value, ctypes.c_byte(0x57).value,
ctypes.c_byte(0x12).value, ctypes.c_byte(0x3E).value, ctypes.c_byte(0x37).value, ctypes.c_byte(0xFF).value, ctypes.c_byte(0x9D).value, ctypes.c_byte(0x4F).value, ctypes.c_byte(0x51).value, ctypes.c_byte(0xF5).value,
ctypes.c_byte(0xA3).value, ctypes.c_byte(0x70).value, ctypes.c_byte(0xBB).value, ctypes.c_byte(0x14).value, ctypes.c_byte(0x75).value, ctypes.c_byte(0xC2).value, ctypes.c_byte(0xB8).value, ctypes.c_byte(0x72).value,
ctypes.c_byte(0xC0).value, ctypes.c_byte(0xED).value, ctypes.c_byte(0x7D).value, ctypes.c_byte(0x68).value, ctypes.c_byte(0xC9).value, ctypes.c_byte(0x2E).value, ctypes.c_byte(0x0D).value, ctypes.c_byte(0x62).value,
ctypes.c_byte(0x46).value, ctypes.c_byte(0x17).value, ctypes.c_byte(0x11).value, ctypes.c_byte(0x4D).value, ctypes.c_byte(0x6C).value, ctypes.c_byte(0xC4).value, ctypes.c_byte(0x7E).value, ctypes.c_byte(0x53).value,
ctypes.c_byte(0xC1).value, ctypes.c_byte(0x25).value, ctypes.c_byte(0xC7).value, ctypes.c_byte(0x9A).value, ctypes.c_byte(0x1C).value, ctypes.c_byte(0x88).value, ctypes.c_byte(0x58).value, ctypes.c_byte(0x2C).value,
ctypes.c_byte(0x89).value, ctypes.c_byte(0xDC).value, ctypes.c_byte(0x02).value, ctypes.c_byte(0x64).value, ctypes.c_byte(0x40).value, ctypes.c_byte(0x01).value, ctypes.c_byte(0x5D).value, ctypes.c_byte(0x38).value,
ctypes.c_byte(0xA5).value, ctypes.c_byte(0xE2).value, ctypes.c_byte(0xAF).value, ctypes.c_byte(0x55).value, ctypes.c_byte(0xD5).value, ctypes.c_byte(0xEF).value, ctypes.c_byte(0x1A).value, ctypes.c_byte(0x7C).value,
ctypes.c_byte(0xA7).value, ctypes.c_byte(0x5B).value, ctypes.c_byte(0xA6).value, ctypes.c_byte(0x6F).value, ctypes.c_byte(0x86).value, ctypes.c_byte(0x9F).value, ctypes.c_byte(0x73).value, ctypes.c_byte(0xE6).value,
ctypes.c_byte(0x0A).value, ctypes.c_byte(0xDE).value, ctypes.c_byte(0x2B).value, ctypes.c_byte(0x99).value, ctypes.c_byte(0x4A).value, ctypes.c_byte(0x47).value, ctypes.c_byte(0x9C).value, ctypes.c_byte(0xDF).value,
ctypes.c_byte(0x09).value, ctypes.c_byte(0x76).value, ctypes.c_byte(0x9E).value, ctypes.c_byte(0x30).value, ctypes.c_byte(0x0E).value, ctypes.c_byte(0xE4).value, ctypes.c_byte(0xB2).value, ctypes.c_byte(0x94).value,
ctypes.c_byte(0xA0).value, ctypes.c_byte(0x3B).value, ctypes.c_byte(0x34).value, ctypes.c_byte(0x1D).value, ctypes.c_byte(0x28).value, ctypes.c_byte(0x0F).value, ctypes.c_byte(0x36).value, ctypes.c_byte(0xE3).value,
ctypes.c_byte(0x23).value, ctypes.c_byte(0xB4).value, ctypes.c_byte(0x03).value, ctypes.c_byte(0xD8).value, ctypes.c_byte(0x90).value, ctypes.c_byte(0xC8).value, ctypes.c_byte(0x3C).value, ctypes.c_byte(0xFE).value,
ctypes.c_byte(0x5E).value, ctypes.c_byte(0x32).value, ctypes.c_byte(0x24).value, ctypes.c_byte(0x50).value, ctypes.c_byte(0x1F).value, ctypes.c_byte(0x3A).value, ctypes.c_byte(0x43).value, ctypes.c_byte(0x8A).value,
ctypes.c_byte(0x96).value, ctypes.c_byte(0x41).value, ctypes.c_byte(0x74).value, ctypes.c_byte(0xAC).value, ctypes.c_byte(0x52).value, ctypes.c_byte(0x33).value, ctypes.c_byte(0xF0).value, ctypes.c_byte(0xD9).value,
ctypes.c_byte(0x29).value, ctypes.c_byte(0x80).value, ctypes.c_byte(0xB1).value, ctypes.c_byte(0x16).value, ctypes.c_byte(0xD3).value, ctypes.c_byte(0xAB).value, ctypes.c_byte(0x91).value, ctypes.c_byte(0xB9).value,
ctypes.c_byte(0x84).value, ctypes.c_byte(0x7F).value, ctypes.c_byte(0x61).value, ctypes.c_byte(0x1E).value, ctypes.c_byte(0xCF).value, ctypes.c_byte(0xC5).value, ctypes.c_byte(0xD1).value, ctypes.c_byte(0x56).value,
ctypes.c_byte(0x3D).value, ctypes.c_byte(0xCA).value, ctypes.c_byte(0xF4).value, ctypes.c_byte(0x05).value, ctypes.c_byte(0xC6).value, ctypes.c_byte(0xE5).value, ctypes.c_byte(0x08).value, ctypes.c_byte(0x49).value])
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
    
    def crypt(self, packer:array):
        remaining:int = len(packer)
        llength:int = 0x5B0
        start:int = 0

        while (remaining > 0):
            myIv:array = self.multiplyBytes(self.m_iv, 4, 4) 

            if remaining < llength:
                llength = remaining

            x:int = start
            while (x < (start + llength)):
                if ((x - start) % len(self.m_iv)) == 0:
                    padded_data = pad(bytes(myIv), AES.block_size)
                    ciphertext:bytes = self.m_cipher.encrypt(padded_data)

                    index:int = 0
                    cipher_count:int = len(ciphertext)
                    iv_len:int = len(myIv)
                    while (index < cipher_count):
                        val = ctypes.c_byte(ciphertext[index]).value 
                        if index < iv_len:
                            myIv[index] = val
                        else:
                            myIv.append(val)

                        index = index + 1 
                        pass # while (index < cipher_count):
                    pass # if ((x - start) % len(self.m_iv)) == 0:

                packer[x] = packer[x] ^ myIv[(x - start) % len(myIv)]

                x = x + 1
                pass # while (x < (start + llength)):

            start = start + llength
            remaining = remaining - llength
            llength = 0x5B4
                
            pass # while (remaining > 0):
         
        self.updateIv()
        return
    
    def multiplyBytes(self, iv:list, count:int, mul:int) -> array:
        size:int = count * mul
        ret:array = array.array('b')
 
        x:int = 0
        while (x < size):
            ret.append(iv[x % count])
            x = x + 1
            pass

        return ret
    
    def updateIv(self) -> None: 
        self.m_iv = self.get_new_iv(self.m_iv)
        return
    
    def get_new_iv(self, old_iv:list) -> list:
        tmp_iv:list = [ctypes.c_byte(0xf2).value, 0x53, ctypes.c_byte(0x50).value,  ctypes.c_byte(0xc6).value]
        
        index:int = 0
        while (index < 4): 
            self.funnyShit(old_iv[index], tmp_iv)
            index = index + 1
            pass
        
        return tmp_iv
    
    def funnyShit(self, in_byte:int, in_list:list) -> list:
        elina:int = ctypes.c_byte(in_list[1]).value
        anna:int = in_byte
        moritz = self.funny_bytes[elina & 0xFF]
        moritz = moritz - in_byte
        in_list[0] = in_list[0] + moritz 
        moritz = in_list[2]
        moritz = moritz ^ self.funny_bytes[anna & 0xFF]
        elina = elina - moritz & 0xFF
        in_list[1] = ctypes.c_byte(elina).value
        elina = in_list[3]
        moritz = ctypes.c_byte(elina).value
        elina = ctypes.c_byte(elina - in_list[0] & 0xFF).value
        moritz = self.funny_bytes[moritz & 0xFF]
        moritz = moritz + in_byte
        moritz = moritz ^ in_list[2]
        in_list[2] = moritz
        elina = ctypes.c_byte(elina + self.funny_bytes[anna & 0xFF] & 0xFF).value
        in_list[3] = elina

        merry:int = in_list[0] & 0xFF
        merry = merry | ((in_list[1] << 8) & 0xFF00)
        merry = merry | ((in_list[2] << 16) & 0xFF0000)
        merry = merry | ((in_list[3] << 24) & 0xFF000000)

        ret_value:int = merry
        ret_value = ret_value >> 0x1D

        merry = merry << 3
        ret_value = ret_value | merry

        in_list[0] = ctypes.c_byte(ret_value & 0xFF).value
        in_list[1] = ctypes.c_byte((ret_value >> 8) & 0xFF).value 
        in_list[2] = ctypes.c_byte((ret_value >> 16) & 0xFF).value 
        in_list[3] = ctypes.c_byte((ret_value >> 24) & 0xFF).value
        return in_list