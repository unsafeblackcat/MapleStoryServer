import xml.etree.ElementTree as ET
from typing import Optional

from WZ.WZFile import * 
from PublicFun import *

class SkillElement (Enum):
    
    NEUTRAL = (0, False)
    PHYSICAL = (1, False)
    FIRE = (2, True)
    ICE = (3, True)
    LIGHTING = (4, False)
    POISON = (5, False)
    HOLY = (6, True)
    DARKNESS = (7, False)
 
    def __init__(self, value:int, special:bool):
        self.m_value = value
        self.m_special = special
        pass

    @classmethod
    def from_initial(cls, char: str) -> Optional['SkillElement']:
        char = char.upper()
        for member in cls:
            if member.name.startswith(char):
                return member
        return SkillElement.NEUTRAL
        


class Skill:
    def __init__(self, id:int):
        self.m_id:int = id
        self.m_job:int = id // 10000
        self.m_element:SkillElement = None
        self.m_action = False
        pass

class SkillFactory:
    def __init__(self):
        self.m_skills:dict[int, Skill] = {}
        pass

    def get_skill(self, id:int) -> Skill:
        return self.m_skills[id]
    
    def get_skill_name(self, id:int) -> str:
        return '' 
    
    def _load_all_skill(self):
        return
    
    def init(self):
        wz:WZFile = WZFile(WZFileEnum.SKILL)
        skill_wz:str = wz.get_file_path()

        files = enum_dir(skill_wz)
        for it in files: 
            tree = ET.parse(it)
            root = tree.getroot()
            for child in root:
                print(child.tag, child.attrib, child.text)
                if (child.tag == 'imgdir' and child.attrib.get('name') == 'skill'):
                    for skill_element in child:
                        skillid = int(skill_element.get('name'))  
                        skill:Skill = self._get_skill(skillid, skill_element)
                        
    
                    pass
                pass
            pass
        pass

        return
    
    def _get_skill(self, skillid:int, skill_element:ET.Element) -> Skill:
        skill_ret:Skill = Skill(skillid)

        is_buffer:bool = False
        skill_type:int = xml_get_element_to_int(skill_element, "skillType", -1)
        elem:str = xml_get_element_to_str(skill_element, "elemAttr", None)
        if elem != None:
            skill_ret.m_element.from_initial(elem[0])
            pass
        else:
            skill_ret.m_element = SkillElement.NEUTRAL
            pass

        if skill_type != -1:
            if skill_type == 2:
                is_buffer = True
            pass  
        else:
            action:bool = False
            if xml_is_element(skill_element, "action") == False:
                if xml_is_element(skill_element, "prepare/action"):
                    action = True
                    pass
                else: 
                    pass
                pass
            else:
                action = True
                pass

            pass # else
        
        return


g_SkillFactory:SkillFactory = None 

def get_skill_factory() -> SkillFactory:
    global g_SkillFactory
    if g_SkillFactory == None:
        g_SkillFactory = SkillFactory()
        pass
    return g_SkillFactory