import ctypes


class MapleAESOFB:
    def __init__(self, iv:list, maple_version:int):
        self.m_iv = iv   
        v1 = ctypes.c_short(((maple_version >> 8) & 0xFF) | ((maple_version << 8) & 0xFF00))
        self.m_maple_version = v1.value
        pass