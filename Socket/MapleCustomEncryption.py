import array
import ctypes

class MapleCustomEncryption:
    def decryptData(data:array) -> array:
        
        index:int = 1
        while (index <= 6):
            
            remember:int = 0
            data_length:int = ctypes.c_byte(len(data) & 0xFF).value
            next_remember:int = 0

            if (index % 2) == 0:
                
                i:int = 0
                while (i < len(data)):

                    cur = data[i]
                    cur = cur - 0x48
                    cur = ctypes.c_byte((~cur) & 0xFF).value
                    cur = MapleCustomEncryption.roll_left(cur, data_length & 0xFF)
                    next_remember = cur
                    cur = cur ^ remember
                    remember = next_remember
                    cur = cur - data_length
                    cur = MapleCustomEncryption.roll_right(cur, 3)
                    data[i] = cur
                    data_length = data_length - 1

                    i = i + 1
                    pass # while (i < len(data)):

                pass # if (index % 2) == 0:
            else:

                i:int = len(data) - 1
                while (i >= 0):

                    cur:int = data[i]
                    # 119
                    cur = MapleCustomEncryption.roll_left(cur, 3)
                    # -69
                    cur = cur ^ 0x13
                    # -88
                    next_remember = cur
                    # -88
                    cur = cur ^ remember
                    remember = next_remember

                    cur = cur - data_length

                    # -90
                    cur = MapleCustomEncryption.roll_right(cur, 4)
                    # 106

                    data[i] = cur
                    data_length = data_length - 1 

                    i = i - 1
                    pass # while (i >= 0):

                pass # else

            index = index + 1
            pass # while (index <= 6)

        return data
    
    def roll_left(i:int, count:int) -> int:
        tmp = i & 0xFF
        tmp = tmp << (count % 8)
        return ctypes.c_byte((tmp % 0xFF) | (tmp >> 8)).value
    
    def roll_right(i:int, count:int) -> int:
        tmp = i & 0xFF
        tmp = tmp << 8
        tmp =  tmp >> (count % 8)

        tmp2 = tmp
        tmp = tmp & 0xFF
        tmp2 = ctypes.c_uint(tmp2).value >> 8

        return ctypes.c_byte(tmp | tmp2).value