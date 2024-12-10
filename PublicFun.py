import random

MAPLESTORY_SERVER_VERSION = 83

def generateSend() -> bytes:
    ivSend = [82, 48, 120, 1] #(random.randint(0, 255) * 255) & 0xff
    return bytes(ivSend)

def generateReceive() -> bytes:
    ivRecv = [70, 114, 122, 2] #(random.randint(0, 255) * 255) & 0xff
    return bytes(ivRecv)
