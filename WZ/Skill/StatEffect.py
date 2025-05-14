import xml.etree.ElementTree as ET

from PublicFun import *
from WZ.Skill.Disease import *

class StatEffect:
    def __init__(self, element_item:ET.Element, id:int, is_skill:bool, over_time:bool):
        self.m_duration:int = xml_get_element_to_int(element_item, "time", -1)
        self.m_hp:int = xml_get_element_to_int(element_item, "hp", 0)
        self.m_hpR:int = xml_get_element_to_int(element_item, "hpR", 0) / 100.0
        self.m_mp:int = xml_get_element_to_int(element_item, "mp", 0)
        self.m_mpR:int = xml_get_element_to_int(element_item, "mpR", 0) / 100.0
        self.m_hpCon:int = xml_get_element_to_int(element_item, "hpCon", 0)
        self.m_mpCon:int = xml_get_element_to_int(element_item, "mpCon", 0)

        ipro:int = xml_get_element_to_int(element_item, "prop", 0)
        self.m_prop = ipro / 100.0

        self.m_cp = xml_get_element_to_int(element_item, "cp", 0)

        cure:list = list()
        if xml_get_element_to_int(element_item, "poison", 0) > 0:
            cure.append(Disease.POISON)
            pass

        if xml_get_element_to_int(element_item, "seal", 0) > 0:
            cure.append(Disease.SEAL)
            pass
        
        if xml_get_element_to_int(element_item, "darkness", 0) > 0:
            cure.append(Disease.DARKNESS)
            pass

        if xml_get_element_to_int(element_item, "weakness", 0) > 0:
            cure.append(Disease.WEAKEN)
            cure.append(Disease.SLOW)
            pass

        if xml_get_element_to_int(element_item, "curse", 0) > 0:
            cure.append(Disease.CURSE)
            pass

        self.m_cure_debuffer:list = cure
        self.m_nuff_skill:int = xml_get_element_to_int(element_item, "nuffSkill", 0)
        self.m_mob_count:int = xml_get_element_to_int(element_item, "mobCount", 0)
        self.m_cool_time:int = xml_get_element_to_int(element_item, "cooltime", 0)
        self.m_morph:int = xml_get_element_to_int(element_item, "morph", 0)
        self.m_ghost:int = xml_get_element_to_int(element_item, "ghost", 0)
        self.m_inc_fatigue:int = xml_get_element_to_int(element_item, "incFatigue", 0)
        self.m_repeat_effect:int = xml_get_element_to_int(element_item, "repeatEffect", 0)
        
        mdd:ET.Element = xml_get_element_item(element_item, "0")
        if mdd != None:
            self.m_mob_skill:int = xml_get_element_to_int(mdd, "mobSkill", 0)
            self.m_level:int = xml_get_element_to_int(mdd, "level", 0)
            self.m_target:int = xml_get_element_to_int(mdd, "target", 0)
            pass
        else:
            self.m_mob_skill:int = 0
            self.m_level:int = 0
            self.m_target:int = 0
            pass
            
        mdds:ET.Element = xml_get_element_item(element_item, "mob")
        if mdds != None:
            pass

        self.m_sourceid = id
        self.m_skill = is_skill
        if self.m_skill == False and self.m_duration > -1:
            self.m_over_time:bool =  True
        else:
            self.m_duration = self.m_duration * 1000
            self.m_over_time = over_time

        return