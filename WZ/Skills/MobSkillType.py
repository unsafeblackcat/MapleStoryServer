from enum import Enum 
from typing import Optional

class MobSkillType(Enum):
    ATTACK_UP = 100
    MAGIC_ATTACK_UP = 101
    DEFENSE_UP = 102
    MAGIC_DEFENSE_UP = 103
    ATTACK_UP_M = 110
    MAGIC_ATTACK_UP_M = 111
    DEFENSE_UP_M = 112
    MAGIC_DEFENSE_UP_M = 113
    HEAL_M = 114
    HASTE_M = 115
    SEAL = 120
    DARKNESS = 121
    WEAKNESS = 122
    STUN = 123
    CURSE = 124
    POISON = 125
    SLOW = 126
    DISPEL = 127
    SEDUCE = 128
    BANISH = 129
    AREA_POISON = 131
    REVERSE_INPUT = 132
    UNDEAD = 133
    STOP_POTION = 134
    STOP_MOTION = 135
    FEAR = 136
    PHYSICAL_IMMUNE = 140
    MAGIC_IMMUNE = 141
    HARD_SKIN = 142
    PHYSICAL_COUNTER = 143
    MAGIC_COUNTER = 144
    PHYSICAL_AND_MAGIC_COUNTER = 145
    PAD = 150
    MAD = 151
    PDR = 152
    MDR = 153
    ACC = 154
    EVA = 155
    SPEED = 156
    SEAL_SKILL = 157
    SUMMON = 200

    def __init__(self, value:int): 
        self.m_id = value

    @classmethod 
    def is_from(cls, id:int) -> Optional['MobSkillType']:
        try:
            return cls(id)
        except ValueError:
            return None
        
    def get_id(self) -> int:
        return self.m_id