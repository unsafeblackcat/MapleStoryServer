from enum import Enum 

# 弓箭手
class Archer(Enum):
    BLESSING_OF_AMAZON = 3000000
    EYE_OF_AMAZON = 3000002
    CRITICAL_SHOT = 3000001
    FOCUS = 3001003
    DOUBLE_SHOT = 3001005
    ARROW_BLOW = 3001004

# 猎手
class Hunter(Enum):
    BOW_MASTERY = 3100000
    FINAL_ATTACK = 3100001
    BOW_BOOSTER = 3101002
    POWER_KNOCKBACK = 3101003
    SOUL_ARROW = 3101004
    ARROW_BOMB = 3101005

# 射手
class Ranger(Enum):
    THRUST = 3110000
    MORTAL_BLOW = 3110001
    PUPPET = 3111002
    INFERNO = 3111003
    ARROW_RAIN = 3111004
    SILVER_HAWK = 3111005
    STRAFE = 3111006

# 神射手
class Bowmaster(Enum):
    MAPLE_WARRIOR = 3121000
    SHARP_EYES = 3121002
    DRAGONS_BREATH = 3121003
    HURRICANE = 3121004
    BOW_EXPERT = 3120005
    PHOENIX = 3121006
    HAMSTRING = 3121007
    CONCENTRATE = 3121008
    HEROS_WILL = 3121009


# 弩弓手
class Crossbowman(Enum):
    CROSSBOW_MASTERY = 3200000
    FINAL_ATTACK = 3200001
    CROSSBOW_BOOSTER = 3201002
    POWER_KNOCKBACK = 3201003
    SOUL_ARROW = 3201004
    IRON_ARROW = 3201005

# 游侠
class Sniper(Enum):
    THRUST = 3210000
    MORTAL_BLOW = 3210001
    PUPPET = 3211002
    BLIZZARD = 3211003
    ARROW_ERUPTION = 3211004
    GOLDEN_EAGLE = 3211005
    STRAFE = 3211006

# 箭神
class Marksman(Enum):
    MAPLE_WARRIOR = 3221000
    PIERCING_ARROW = 3221001
    SHARP_EYES = 3221002
    DRAGONS_BREATH = 3221003
    MARKSMAN_BOOST = 3220004
    FROST_PREY = 3221005
    BLIND = 3221006
    SNIPE = 3221007
    HEROS_WILL = 3221008