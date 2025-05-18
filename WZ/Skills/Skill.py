from WZ.Skill.SkillElement import *
from WZ.Skill.StatEffect import *

class Skill:
    def __init__(self, id:int):
        self.m_id:int = id
        self.m_job:int = id // 10000
        self.m_element:SkillElement = None
        self.m_action = False
        self.m_stat_effect:list = list(StatEffect)
        pass
