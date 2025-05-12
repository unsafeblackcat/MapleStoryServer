from enum import Enum 
from Config.MapleStoryConfig import *
from PublicFun import *


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
        self.m_file_name = wzfe.name + ".wz"
        
    def get_file_path(self) -> str:
        ret:str = "" 
        wzpath:str = os.getcwd() + "/Resources/wz/" + self.m_file_name
        langpath = os.getcwd() + "/Resources/wz-" + get_language() + self.m_file_name + "/"

        if is_file_exist(langpath):
            ret = langpath
        else: 
            ret = wzpath
        return ret


