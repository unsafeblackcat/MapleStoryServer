import random
from enum import Enum 


from WZ.Skill.MobSkillType import *
from constants.game.GameConstants import GameConstants

class Disease(Enum):
    NULL = (0x0, None)
    SLOW = (0x1, MobSkillType.SLOW)
    SEDUCE = (0x80, MobSkillType.SEDUCE)
    FISHABLE = (0x100, None)
    ZOMBIFY = (0x4000, None)
    CONFUSE = (0x80000, MobSkillType.REVERSE_INPUT)
    STUN = (0x2000000000000, MobSkillType.STUN)
    POISON = (0x4000000000000, MobSkillType.POISON)
    SEAL = (0x8000000000000, MobSkillType.SEAL)
    DARKNESS = (0x10000000000000, MobSkillType.DARKNESS)
    WEAKEN = (0x4000000000000000, MobSkillType.WEAKNESS)
    CURSE = (0x8000000000000000, MobSkillType.CURSE)

    def __init__(self, value:int, mob_skill_type:MobSkillType):
        self.m_value:int = value   
        self.m_mob_skill_type:MobSkillType = mob_skill_type

    def get_valie(self) -> int:
        return self.m_value
    
    def get_mob_skill_type(self) -> MobSkillType:
        return self.m_mob_skill_type
    
    def is_first(self) -> bool:
        return False
    
    @classmethod
    def from_id(cls, id_value:int) -> Optional['Disease']:
        try:
            return cls(id_value)
        except ValueError:
            return None
         
    def get_random() -> int:
        return random.choice(GameConstants.CPQ_DISEASES)
    
    @classmethod
    def get_by_skill(cls, skill:Optional[MobSkillType]) -> Optional['Disease']:
        if skill is None:
            return None
        for disease in cls:
            if disease.m_mob_skill_type == skill:
                return disease
        return None