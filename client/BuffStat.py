from enum import Enum 
from typing import Optional

class BuffStat(Enum):
    MORPH = (0x2, False)
    RECOVERY = (0x4, False)
    MAPLE_WARRIOR = (0x8, False)
    STANCE = (0x10, False)
    SHARP_EYES = (0x20, False)
    MANA_REFLECTION = (0x40, False)
    SHADOW_CLAW = (0x100, False)
    INFINITY = (0x200, False)
    HOLY_SHIELD = (0x400, False)
    HAMSTRING = (0x800, False)
    BLIND = (0x1000, False)
    CONCENTRATE = (0x2000, False)
    PUPPET = (0x4000, False)
    ECHO_OF_HERO = (0x8000, False)
    MESO_UP_BY_ITEM = (0x10000, False)
    GHOST_MORPH = (0x20000, False)
    AURA = (0x40000, False)
    CONFUSE = (0x80000, False)
    COUPON_EXP1 = (0x100000, False)
    EXP_BUFF = (0x40000000, False)
    COUPON_EXP2 = (0x200000, False)
    COUPON_EXP3 = (0x400000, False)
    COUPON_EXP4 = (0x400000, False)
    COUPON_DRP1 = (0x800000, False)
    COUPON_DRP2 = (0x1000000, False)
    COUPON_DRP3 = (0x1000000, False)
    ITEM_UP_BY_ITEM = (0x100000, False)
    RESPECT_PIMMUNE = (0x200000, False)
    RESPECT_MIMMUNE = (0x400000, False)
    DEFENSE_ATT = (0x800000, False)
    DEFENSE_STATE = (0x1000000, False)
    HPREC = (0x2000000, False)
    MPREC = (0x4000000, False)
    BERSERK_FURY = (0x8000000, False)
    DIVINE_BODY = (0x10000000, False)
    SPARK = (0x20000000, False)
    MAP_CHAIR = (0x40000000, False)
    FINALATTACK = (0x80000000, False)
    WATK = (0x100000000, False)
    WDEF = (0x200000000, False)
    MATK = (0x400000000, False)
    MDEF = (0x800000000, False)
    ACC = (0x1000000000, False)
    AVOID = (0x2000000000, False)
    HANDS = (0x4000000000, False)
    SPEED = (0x8000000000, False)
    JUMP = (0x10000000000, False)
    MAGIC_GUARD = (0x20000000000, False)
    DARKSIGHT = (0x40000000000, False)
    BOOSTER = (0x80000000000, False)
    POWERGUARD = (0x100000000000, False)
    HYPERBODYHP = (0x200000000000, False)
    HYPERBODYMP = (0x400000000000, False)
    INVINCIBLE = (0x800000000000, False)
    SOULARROW = (0x1000000000000, False)
    STUN = (0x2000000000000, False)
    POISON = (0x4000000000000, False)
    SEAL = (0x8000000000000, False)
    DARKNESS = (0x10000000000000, False)
    COMBO = (0x20000000000000, False)
    SUMMON = (0x20000000000000, False)
    WK_CHARGE = (0x40000000000000, False)
    DRAGONBLOOD = (0x80000000000000, False)
    HOLY_SYMBOL = (0x100000000000000, False)
    MESOUP = (0x200000000000000, False)
    SHADOWPARTNER = (0x400000000000000, False)
    PICKPOCKET = (0x800000000000000, False)
    MESOGUARD = (0x1000000000000000, False)
    EXP_INCREASE = (0x2000000000000000, False)
    WEAKEN = (0x4000000000000000, False)
    MAP_PROTECTION = (0x8000000000000000, False)

    # incorrect（特殊标记）的项目
    SLOW = (0x200000000, True)
    ELEMENTAL_RESET = (0x200000000, True)
    MAGIC_SHIELD = (0x400000000, True)
    MAGIC_RESISTANCE = (0x800000000, True)
    WIND_WALK = (0x400000000, True)
    ARAN_COMBO = (0x1000000000, True)
    COMBO_DRAIN = (0x2000000000, True)
    COMBO_BARRIER = (0x4000000000, True)
    BODY_PRESSURE = (0x8000000000, True)
    SMART_KNOCKBACK = (0x10000000000, True)
    BERSERK = (0x20000000000, True)
    ENERGY_CHARGE = (0x4000000000000, True)
    DASH2 = (0x8000000000000, True)
    DASH = (0x10000000000000, True)
    MONSTER_RIDING = (0x20000000000000, True)
    SPEED_INFUSION = (0x40000000000000, True)
    HOMING_BEACON = (0x80000000000000, True)

    def __init__(self, value:int, first:bool=False):
        self.m_value = value
        self.m_first = first

    def get_value(self) -> int:
        return self.m_value
    
    def is_first(self) -> bool:
        return self.m_first
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name