from enum import Enum 

class ItemId(Enum):
    # Misc
    PENDANT_OF_THE_SPIRIT = 1122017
    HEART_SHAPED_CHOCOLATE = 5110000
    HAPPY_BIRTHDAY = 2022153
    FISHING_CHAIR = 3011000
    MINI_GAME_BASE = 4080000
    MATCH_CARDS = 4080100
    MAGICAL_MITTEN = 1472063
    RPS_CERTIFICATE_BASE = 4031332
    GOLDEN_MAPLE_LEAF = 4000313
    PERFECT_PITCH = 4310000
    MAGIC_ROCK = 4006000
    GOLDEN_CHICKEN_EFFECT = 4290000
    BUMMER_EFFECT = 4290001
    ARPQ_SHIELD = 2022269
    ROARING_TIGER_MESSENGER = 5390006

    def is_exp_increase(itemid:int) -> bool:
        return itemid >= 2022450 and itemid <= 2022452
    
    def is_rate_coupon(itemid:int) -> bool:
        itemType:int = int(itemid / 1000)
        return itemType == 5211 or itemType == 5360
    
    def is_monster_card(itemid:int) -> bool:
        itemType:int = int(itemid / 1000)
        return itemType == 238
    
    def is_pyramid_buff(itemid:int) -> bool:
        return (itemid >= 2022585 and itemid <= 2022588) or (itemid >= 2022616 and itemid <= 2022617)
    
    def is_dojo_buff(itemid:int) -> bool:
        return itemid >= 2022359 and itemid <= 2022421
    
    # Potion
    WHITE_POTION = 2000002
    BLUE_POTION = 2000003
    ORANGE_POTION = 2000001
    MANA_ELIXIR = 2000006

    # HP/MP recovery
    SORCERERS_POTION = 2022337
    RUSSELLONS_PILLS = 2022198

    # Environment
    RED_BEAN_PORRIDGE = 2022001
    SOFT_WHITE_BUN = 2022186
    AIR_BUBBLE = 2022040

    # Chair
    RELAXER = 3010000
    CHAIR_MIN = RELAXER
    CHAIR_MAX = FISHING_CHAIR
    
    def is_chair(itemid:int) -> bool:
        return itemid >= ItemId.CHAIR_MIN and itemid <= ItemId.CHAIR_MAX
    
    # Throwing star
    SUBI_THROWING_STARS = 2070000
    HWABI_THROWING_STARS = 2070007
    BALANCED_FURY = 2070018
    CRYSTAL_ILBI_THROWING_STARS = 2070016
    THROWING_STAR_MIN = SUBI_THROWING_STARS
    THROWING_STAR_MAX = 2070016
    DEVIL_RAIN_THROWING_STAR = 2070014

    def all_throwing_star_ids() -> list:
        return list(range(ItemId.THROWING_STAR_MIN, ItemId.THROWING_STAR_MAX + 1))
    
    # Bullet
    BULLET = 2330000
    BULLET_MIN = BULLET
    BULLET_MAX = 2330005
    BLAZE_CAPSULE = 2331000
    GLAZE_CAPSULE = 2332000

    def all_bullet_ids() -> list:
        return list(range(ItemId.BULLET_MIN, ItemId.BULLET_MAX + 1))
    
    # Starter
    BEGINNERS_GUIDE = 4161001
    LEGENDS_GUIDE = 4161048
    NOBLESSE_GUIDE = 4161047

    # Warrior
    RED_HWARANG_SHIRT = 1040021
    BLACK_MARTIAL_ARTS_PANTS = 1060016
    MITHRIL_BATTLE_GRIEVES = 1072039
    GLADIUS = 1302008
    MITHRIL_POLE_ARM = 1442001
    MITHRIL_MAUL = 1422001
    FIREMANS_AXE = 1312005
    DARK_ENGRIT = 1051010

    # Bowman
    GREEN_HUNTERS_ARMOR = 1040067
    GREEN_HUNTRESS_ARMOR = 1041054
    GREEN_HUNTERS_PANTS = 1060056
    GREEN_HUNTRESS_PANTS = 1061050
    GREEN_HUNTER_BOOTS = 1072081
    RYDEN = 1452005
    MOUNTAIN_CROSSBOW = 1462000

    # Magician
    BLUE_WIZARD_ROBE = 1050003
    PURPLE_FAIRY_TOP = 1041041
    PURPLE_FAIRY_SKIRT = 1061034
    RED_MAGICSHOES = 1072075
    MITHRIL_WAND = 1372003
    CIRCLE_WINDED_STAFF = 1382017

    # Thief
    DARK_BROWN_STEALER = 1040057
    RED_STEAL = 1041047
    DARK_BROWN_STEALER_PANTS = 1060043
    RED_STEAL_PANTS = 1061043
    BRONZE_CHAIN_BOOTS = 1072032
    STEEL_GUARDS = 1472008
    REEF_CLAW = 1332012

    # Pirate
    BROWN_PAULIE_BOOTS = 1072294
    PRIME_HANDS = 1482004
    COLD_MIND = 1492004
    BROWN_POLLARD = 1052107

    # Three snails
    SNAIL_SHELL = 4000019
    BLUE_SNAIL_SHELL = 4000000
    RED_SNAIL_SHELL = 4000016

    # Special scroll
    COLD_PROTECTION_SCROLl = 2041058
    SPIKES_SCROLL = 2040727
    VEGAS_SPELL_10 = 5610000
    VEGAS_SPELL_60 = 5610001
    CHAOS_SCROll_60 = 2049100
    LIAR_TREE_SAP = 2049101
    MAPLE_SYRUP = 2049102
    WHITE_SCROLL = 2340000
    CLEAN_SLATE_1 = 2049000
    CLEAN_SLATE_3 = 2049001
    CLEAN_SLATE_5 = 2049002
    CLEAN_SLATE_20 = 2049003
    RING_STR_100_SCROLL = 2041100
    DRAGON_STONE_SCROLL = 2041200
    BELT_STR_100_SCROLL = 2041300

    # Cure debuff
    ALL_CURE_POTION = 2050004
    EYEDROP = 2050001
    TONIC = 2050002
    HOLY_WATER = 2050003
    ANTI_BANISH_SCROLL = 2030100
    DOJO_PARTY_ALL_CURE = 2022433
    CARNIVAL_PARTY_ALL_CURE = 2022163
    WHITE_ELIXIR = 2022544
 
    def is_party_all_cure(itemid:int) -> bool:
        return itemid == ItemId.DOJO_PARTY_ALL_CURE and itemid == ItemId.CARNIVAL_PARTY_ALL_CURE
    
    # Special effect
    PHARAOHS_BLESSING_1 = 2022585
    PHARAOHS_BLESSING_2 = 2022586
    PHARAOHS_BLESSING_3 = 2022587
    PHARAOHS_BLESSING_4 = 2022588

    # Evolve pet
    DRAGON_PET = 5000028
    ROBO_PET = 5000047

    # Pet equip
    MESO_MAGNET = 1812000
    ITEM_POUCH = 1812001
    ITEM_IGNORE = 1812007

    def is_pet(itemid:int) -> bool:
        return (itemid / 1000) == 5000
    
    # Expirable pet
    PET_SNAIL = 5000054

    # Permanent pet
    PERMA_PINK_BEAN = 5000060
    PERMA_KINO = 5000100
    PERMA_WHITE_TIGER = 5000101
    PERMA_MINI_YETI = 5000102

    def get_perma_pets() -> list:
        return [ItemId.PERMA_PINK_BEAN, ItemId.PERMA_KINO, ItemId.PERMA_WHITE_TIGER, ItemId.PERMA_MINI_YETI]
    
    # Maker
    BASIC_MONSTER_CRYSTAL_1 = 4260000
    BASIC_MONSTER_CRYSTAL_2 = 4260001
    BASIC_MONSTER_CRYSTAL_3 = 4260002
    INTERMEDIATE_MONSTER_CRYSTAL_1 = 4260003
    INTERMEDIATE_MONSTER_CRYSTAL_2 = 4260004
    INTERMEDIATE_MONSTER_CRYSTAL_3 = 4260005
    ADVANCED_MONSTER_CRYSTAL_1 = 4260006
    ADVANCED_MONSTER_CRYSTAL_2 = 4260007
    ADVANCED_MONSTER_CRYSTAL_3 = 4260008

    # NPC weather (PQ)
    NPC_WEATHER_GROWLIE = 5120016

    # Safety charm
    SAFETY_CHARM = 5130000
    EASTER_BASKET = 4031283
    EASTER_CHARM = 4140903

    # Engagement box
    ENGAGEMENT_BOX_MOONSTONE = 2240000
    ENGAGEMENT_BOX_STAR = 2240001
    ENGAGEMENT_BOX_GOLDEN = 2240002
    ENGAGEMENT_BOX_SILVER = 2240003
    EMPTY_ENGAGEMENT_BOX_MOONSTONE = 4031357
    ENGAGEMENT_RING_MOONSTONE = 4031358
    EMPTY_ENGAGEMENT_BOX_STAR = 4031359
    ENGAGEMENT_RING_STAR = 4031360
    EMPTY_ENGAGEMENT_BOX_GOLDEN = 4031361
    ENGAGEMENT_RING_GOLDEN = 4031362
    EMPTY_ENGAGEMENT_BOX_SILVER = 4031363
    ENGAGEMENT_RING_SILVER = 4031364
 
    def is_wedding_token(itemid:int) -> bool:
        return itemid >= ItemId.EMPTY_ENGAGEMENT_BOX_MOONSTONE and itemid <= ItemId.ENGAGEMENT_RING_SILVER
    
    # Wedding etc
    PARENTS_BLESSING = 4031373
    OFFICIATORS_PERMISSION = 4031374
    ONYX_CHEST_FOR_COUPLE = 4031424

    # Wedding ticket
    NORMAL_WEDDING_TICKET_CATHEDRAL = 5251000
    NORMAL_WEDDING_TICKET_CHAPEL = 5251001
    PREMIUM_WEDDING_TICKET_CHAPEL = 5251002
    PREMIUM_WEDDING_TICKET_CATHEDRAL = 5251003

    # Wedding reservation
    PREMIUM_CATHEDRAL_RESERVATION_RECEIPT = 4031375
    PREMIUM_CHAPEL_RESERVATION_RECEIPT = 4031376
    NORMAL_CATHEDRAL_RESERVATION_RECEIPT = 4031480
    NORMAL_CHAPEL_RESERVATION_RECEIPT = 4031481

    # Wedding invite
    INVITATION_CHAPEL = 4031377
    INVITATION_CATHEDRAL = 4031395
    RECEIVED_INVITATION_CHAPEL = 4031406
    RECEIVED_INVITATION_CATHEDRAL = 4031407

    CARAT_RING_BASE = 1112300 # Unsure about math on this and the following one
    CARAT_RING_BOX_BASE = 2240004
    CARAT_RING_BOX_MAX = 2240015

    # Wedding ring
    WEDDING_RING_MOONSTONE = 1112803
    WEDDING_RING_STAR = 1112806
    WEDDING_RING_GOLDEN = 1112807
    WEDDING_RING_SILVER = 1112809

    def is_wedding_ring(itemid:int) -> bool:
        return (itemid == ItemId.WEDDING_RING_MOONSTONE 
                or itemid == ItemId.WEDDING_RING_STAR
                or  itemid == ItemId.WEDDING_RING_GOLDEN
                or  itemid == ItemId.WEDDING_RING_SILVER)
    
    # Priority buff
    ROSE_SCENT = 2022631
    FREESIA_SCENT = 2022632
    LAVENDER_SCENT = 2022633

    # Cash shop
    WHEEL_OF_FORTUNE = 5510000
    CASH_SHOP_SURPRISE = 5222000
    EXP_COUPON_2X_4H = 5211048
    DROP_COUPON_2X_4H = 5360042
    EXP_COUPON_3X_2H = 5211060
    QUICK_DELIVERY_TICKET = 5330000
    CHALKBOARD_1 = 5370000
    CHALKBOARD_2 = 5370001
    REMOTE_GACHAPON_TICKET = 5451000
    AP_RESET = 5050000
    NAME_CHANGE = 5400000
    WORLD_TRANSFER = 5401000
    MAPLE_LIFE_B = 5432000
    VICIOUS_HAMMER = 5570000

    NX_CARD_100 = 4031865
    NX_CARD_250 = 4031866

    
    def is_nx_card(itemid:int) -> bool:
        return (itemid == ItemId.NX_CARD_100 or itemid == ItemId.NX_CARD_250)
    
    
    def is_cash_package(itemid:int) -> bool:
        return (int(itemid / 10000) == 910)
    
    # Face expression
    FACE_EXPRESSION_MIN = 5160000
    FACE_EXPRESSION_MAX = 5160014
   
    def is_face_expression(itemid:int) -> bool:
        return itemid >= ItemId.FACE_EXPRESSION_MIN and itemid <= ItemId.FACE_EXPRESSION_MAX
    
    # New Year card
    NEW_YEARS_CARD = 2160101
    NEW_YEARS_CARD_SEND = 4300000
    NEW_YEARS_CARD_RECEIVED = 4301000

    # Popular owl items
    WORK_GLOVES = 1082002
    STEELY_THROWING_KNIVES = 2070005
    ILBI_THROWING_STARS = 2070006
    OWL_BALL_MASK = 1022047
    PINK_ADVENTURER_CAPE = 1102041
    CLAW_30_SCROLL = 2044705
    HELMET_60_ACC_SCROLL = 2040017
    MAPLE_SHIELD = 1092030
    GLOVES_ATT_60_SCROLL = 2040804
 
    def ge_owl_items() -> list:
        return [ ItemId.WORK_GLOVES, ItemId.STEELY_THROWING_KNIVES, ItemId.ILBI_THROWING_STARS, ItemId.OWL_BALL_MASK, ItemId.PINK_ADVENTURER_CAPE,
                ItemId.CLAW_30_SCROLL, ItemId.WHITE_SCROLL, ItemId.HELMET_60_ACC_SCROLL, ItemId.MAPLE_SHIELD, ItemId.GLOVES_ATT_60_SCROLL]
    
    # Henesys PQ
    GREEN_PRIMROSE_SEED = 4001095
    PURPLE_PRIMROSE_SEED = 4001096
    PINK_PRIMROSE_SEED = 4001097
    BROWN_PRIMROSE_SEED = 4001098
    YELLOW_PRIMROSE_SEED = 4001099
    BLUE_PRIMROSE_SEED = 4001100
    MOON_BUNNYS_RICE_CAKE = 4001101

    # Catch mobs items
    PHEROMONE_PERFUME = 2270000
    POUCH = 2270001
    GHOST_SACK = 4031830
    ARPQ_ELEMENT_ROCK = 2270002
    ARPQ_SPIRIT_JEWEL = 4031868
    MAGIC_CANE = 2270003
    TAMED_RUDOLPH = 4031887
    TRANSPARENT_MARBLE_1 = 2270005
    MONSTER_MARBLE_1 = 2109001
    TRANSPARENT_MARBLE_2 = 2270006
    MONSTER_MARBLE_2 = 2109002
    TRANSPARENT_MARBLE_3 = 2270007
    MONSTER_MARBLE_3 = 2109003
    EPQ_PURIFICATION_MARBLE = 2270004
    EPQ_MONSTER_MARBLE = 4001169
    FISH_NET = 2270008
    FISH_NET_WITH_A_CATCH = 2022323

    # Mount
    BATTLESHIP = 1932000

    # Explorer mount
    HOG = 1902000
    SILVER_MANE = 1902001
    RED_DRACO = 1902002
    EXPLORER_SADDLE = 1912000
 
    def is_explorer_mount(itemid:int) -> bool:
        return ((itemid >= ItemId.HOG and itemid <= ItemId.RED_DRACO)
                or itemid == ItemId.EXPLORER_SADDLE)
    
    # Cygnus mount
    MIMIANA = 1902005
    MIMIO = 1902006
    SHINJOU = 1902007
    CYGNUS_SADDLE = 1912005

    
    def is_cygnus_mount(itemid:int) -> bool:
        return ((itemid >= ItemId.MIMIANA and itemid <= ItemId.SHINJOU)
                or itemid == ItemId.CYGNUS_SADDLE)
    
    #  Dev equips
    GREEN_HEADBAND = 1002067
    TIMELESS_NIBLEHEIM = 1402046
    BLUE_KORBEN = 1082140
    MITHRIL_PLATINE_PANTS = 1060091
    BLUE_CARZEN_BOOTS = 1072154
    MITHRIL_PLATINE = 1040103

    '''
        判断装备的性别要求。
        @param {int} itemId - 装备的ID。
        @returns {int} - 返回装备的性别要求：
            0 - 仅限男性使用
            1 - 仅限女性使用
            2 - 无性别要求
    '''
    def get_gender(itemid:int) -> int:
        if (int(itemid / 1000000) != 1):
            return 2; # 默认值，表示无性别要求 

        genderPart:int = itemid / 1000 % 10
        if (genderPart == 0):
            return 0 # 仅限男性使用
        elif (genderPart == 1):
            return 1 # 仅限女性使用
        else:
            return 2 # 无性别要求
        