from WZ.Skills.SkillElement import *
from WZ.Skills.StatEffect import *

class Skill:
    def __init__(self, id:int):
        self.m_id:int = id
        self.m_job:int = id // 10000
        self.m_element:SkillElement = None
        self.m_action = False
        self.m_stat_effect:list = list()
        self.m_animationTime:int = 0
        pass

    def set_animation_time(self, value:int):
        self.m_animationTime = value

    def inc_animation_time(self, value:int):
        self.m_animationTime = self.m_animationTime + value