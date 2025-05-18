from typing import Optional
from enum import Enum

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
        