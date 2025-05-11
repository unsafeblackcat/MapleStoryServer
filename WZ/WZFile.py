from enum import Enum
from pathlib import Path

from Config.MapleStoryConfig import *


class WZFileEnum(Enum):
    QUEST = "Quest"
    ETC = "Etc"
    ITEM = "Item"
    CHARACTER = "Character"
    STRING = "String"
    LIST = "List"
    MOB = "Mob"
    MAP = "Map"
    NPC = "Npc"
    REACTOR = "Reactor"
    SKILL = "Skill"
    SOUND = "Sound"
    UI = "UI"

class WZFile:
    def __init__(self, wzfe:WZFileEnum):
        self.m_file_name = wzfe + ".wz"
        
    def get_file_path(self) -> str:
        ret:str = "" 
        wzpath:str = os.getcwd() + "/wz/" + self.m_file_name
        langpath = os.getcwd() + "/wz-" + get_language() + self.m_file_name + "/"

        if Path(langpath).is_file():
            ret = langpath
        else: 
            ret = wzpath
        return ret


