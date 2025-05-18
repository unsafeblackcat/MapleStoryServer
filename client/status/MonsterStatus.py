from enum import Enum 

class MonsterStatus(Enum):
    WATK = (0x1, False)
    WDEF = (0x2, False)
    NEUTRALISE = (0x2, True)
    PHANTOM_IMPRINT = (0x4, True)
    MATK = (0x4, False)
    MDEF = (0x8, False)
    ACC = (0x10, False)
    AVOID = (0x20, False)
    SPEED = (0x40, False)
    STUN = (0x80, False)
    FREEZE = (0x100, False)
    POISON = (0x200, False)
    SEAL = (0x400, False)
    SHOWDOWN = (0x800, False)
    WEAPON_ATTACK_UP = (0x1000, False)
    WEAPON_DEFENSE_UP = (0x2000, False)
    MAGIC_ATTACK_UP = (0x4000, False)
    MAGIC_DEFENSE_UP = (0x8000, False)
    DOOM = (0x10000, False)
    SHADOW_WEB = (0x20000, False)
    WEAPON_IMMUNITY = (0x40000, False)
    MAGIC_IMMUNITY = (0x80000, False)
    HARD_SKIN = (0x200000, False)
    NINJA_AMBUSH = (0x400000, False)
    ELEMENTAL_ATTRIBUTE = (0x800000, False)
    VENOMOUS_WEAPON = (0x1000000, False)
    BLIND = (0x2000000, False)
    SEAL_SKILL = (0x4000000, False)
    INERTMOB = (0x10000000, False)
    WEAPON_REFLECT = (0x20000000, True)
    MAGIC_REFLECT = (0x40000000, True)

    def __init__(self, mask: int, is_first:bool = False):
        self.m_value = mask
        self.m_is_first = is_first
        return
    
    def is_first(self) -> bool:
        return self.m_is_first
    
    def get_value(self) -> int:
        return self.m_value