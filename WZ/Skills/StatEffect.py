import xml.etree.ElementTree as ET

from PublicFun import *
from WZ.Skills.Disease import *
from WZ.Skills.Job.FaShi import *
from WZ.Skills.Job.FeiXia import *
from WZ.Skills.Job.GongJianShou import *
from WZ.Skills.Job.HaiDao import *
from WZ.Skills.Job.QiShiTuan import *
from WZ.Skills.Job.ShenLong import *
from WZ.Skills.Job.SuperGM import *
from WZ.Skills.Job.XinShou import *
from WZ.Skills.Job.ZhanShen import *
from WZ.Skills.Job.ZhanShi import *  
from client.BuffStat import *
from client.status.MonsterStatus import *
from constants.id.ItemId import *
from maps.SummonMovementType import *
from Config.MapleStoryConfig import *

class CardItemupStats:
    def __init__(self, code:int, prob:int, areas:dict, inParty:bool):
        self.m_itemCode = code
        self.m_prob = prob
        self.m_areas = areas
        self.m_party = inParty
        pass

    def is_in_area(self, mapid:int) -> bool:
        if self.m_areas == None:
            return True
        
        for it, value in self.m_areas:
            if mapid >= it and mapid <= value:
                return True
            
        return False

class StatEffect:
    def __init__(self, element_item:ET.Element, id:int, is_skill:bool, over_time:bool):
        self.m_duration:int = xml_get_element_to_int(element_item, "time", -1)
        self.m_hp:int = xml_get_element_to_int(element_item, "hp")
        self.m_hpR:int = xml_get_element_to_int(element_item, "hpR") / 100.0
        self.m_mp:int = xml_get_element_to_int(element_item, "mp")
        self.m_mpR:int = xml_get_element_to_int(element_item, "mpR") / 100.0
        self.m_hpCon:int = xml_get_element_to_int(element_item, "hpCon")
        self.m_mpCon:int = xml_get_element_to_int(element_item, "mpCon")

        ipro:int = xml_get_element_to_int(element_item, "prop")
        self.m_prop = ipro / 100.0

        self.m_cp = xml_get_element_to_int(element_item, "cp")

        cure:list = list()
        if xml_get_element_to_int(element_item, "poison") > 0:
            cure.append(Disease.POISON)
            pass

        if xml_get_element_to_int(element_item, "seal") > 0:
            cure.append(Disease.SEAL)
            pass
        
        if xml_get_element_to_int(element_item, "darkness") > 0:
            cure.append(Disease.DARKNESS)
            pass

        if xml_get_element_to_int(element_item, "weakness") > 0:
            cure.append(Disease.WEAKEN)
            cure.append(Disease.SLOW)
            pass

        if xml_get_element_to_int(element_item, "curse") > 0:
            cure.append(Disease.CURSE)
            pass

        self.m_cure_debuffer:list = cure
        self.m_nuff_skill:int = xml_get_element_to_int(element_item, "nuffSkill")
        self.m_mob_count:int = xml_get_element_to_int(element_item, "mobCount")
        self.m_cool_time:int = xml_get_element_to_int(element_item, "cooltime")
        self.m_morph:int = xml_get_element_to_int(element_item, "morph")
        self.m_ghost:int = xml_get_element_to_int(element_item, "ghost")
        self.m_inc_fatigue:int = xml_get_element_to_int(element_item, "incFatigue")
        self.m_repeat_effect:int = xml_get_element_to_int(element_item, "repeatEffect")
        
        mdd:ET.Element = xml_get_element_item(element_item, "0")
        if mdd != None and len(mdd) > 0:
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
        if mdds != None and len(mdds) > 0:
            self.m_mob:int = xml_get_element_to_int(mdds, "mob")
            pass

        self.m_sourceid = id
        self.m_skill = is_skill
        if self.m_skill == False and self.m_duration > -1:
            self.m_over_time:bool =  True
        else:
            self.m_duration = self.m_duration * 1000
            self.m_over_time = over_time


        self.m_watk:int = xml_get_element_to_int(element_item, "pad")
        self.m_wdef:int = xml_get_element_to_int(element_item, "pdd")
        self.m_matk:int = xml_get_element_to_int(element_item, "mad")
        self.m_mdef:int = xml_get_element_to_int(element_item, "mdd")
        self.m_acc:int = xml_get_element_to_int(element_item, "acc")
        self.m_avoid:int = xml_get_element_to_int(element_item, "source")
        self.m_expbuff:int = xml_get_element_to_int(element_item, "expBuff")
        self.m_speed:int = xml_get_element_to_int(element_item, "speed")
        self.m_jump:int = xml_get_element_to_int(element_item, "jump")
        self.m_barrier:int = xml_get_element_to_int(element_item, "barrier")

        statups:list = list() 
        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.AURA, self.m_barrier)
        
        self.m_map_protection:int = self.map_protection(id)
        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.MAP_PROTECTION, self.m_map_protection)

        if self.m_over_time and self.get_summon_movement_type() == None:
            if is_skill == False:
                if ItemId.is_party_all_cure(id):
                    self.m_berserk:int = xml_get_element_to_int(element_item, "berserk")
                    self.m_booster:int = xml_get_element_to_int(element_item, "booster")

                    self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.BERSERK, self.m_berserk)
                    self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.BOOSTER, self.m_booster)
                    pass
                elif ItemId.is_dojo_buff(id) or self.is_hp_mp_recovery(id):
                    self.m_hpR:int = xml_get_element_to_int(element_item, "mhpR")
                    self.m_hpRRate:int = xml_get_element_to_int(element_item, "mhpRRate") * 100
                    self.m_mpR:int = xml_get_element_to_int(element_item, "mmpR")
                    self.m_mpRRate:int = xml_get_element_to_int(element_item, "mmpRRate") * 100

                    self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.HPREC, self.m_hpR)
                    self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.MPREC, self.m_mpR)
                    pass
                elif ItemId.is_rate_coupon(id):
                    expR:int = xml_get_element_to_int(element_item, "expR")
                    if expR == 1:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.COUPON_EXP1, 1)
                    elif expR == 2:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.COUPON_EXP2, 2)
                    elif expR == 3:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.COUPON_EXP3, 3)
                    elif expR == 4:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.COUPON_EXP4, 4)
                    pass

                    drpR:int = xml_get_element_to_int(element_item, "drpR")
                    if drpR == 1:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.COUPON_DRP1, 1)
                    elif drpR == 2:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.COUPON_DRP2, 2)
                    elif drpR == 3:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.COUPON_DRP3, 3)

                    pass
                elif ItemId.is_monster_card(id): 
                    prob:int = 0
                    itemupCode:int = 0x7fffffff # Integer.MAX_VALUE
                    areas:dict = None
                    inParty:bool = False

                    con:ET.Element = xml_get_element_item(element_item, "con")
                    if con != None:
                        areas:list = list()
                        
                        for it in con:
                            type:int = xml_get_element_to_int(it, "type", -1)
                            if type == 0:
                                startMap:int = xml_get_element_to_int(it, "sMap")
                                endMap:int = xml_get_element_to_int(it, "endMap")
                                areas.append(dict(startMap, endMap))
                                pass
                            elif type == 2:
                                inParty = True
                                pass
                            pass

                        if len(areas) == 0:
                            pass 

                        pass

                    if xml_get_element_to_int(element_item, "mesoupbyitem") != 0:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.MESO_UP_BY_ITEM, 4)
                        prob = xml_get_element_to_int(element_item, "prob", 1)
                        pass

                    itemupType:int = xml_get_element_to_int(element_item, "itemupbyitem")
                    if itemupType != 0:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.ITEM_UP_BY_ITEM, 4)
                        prob = xml_get_element_to_int(element_item, "prob", 1)

                        if itemupType == 2:
                            itemupCode = xml_get_element_to_int(element_item, "itemCode", 1)
                        elif itemupType == 3:
                            itemupCode = xml_get_element_to_int(element_item, "itemRange", 1)
                            
                        pass

                    if xml_get_element_to_int(element_item, "respectPimmune") != 0:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.RESPECT_PIMMUNE, 4)

                    
                    if xml_get_element_to_int(element_item, "respectMimmune") != 0:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.RESPECT_MIMMUNE, 4)

                    if xml_get_element_to_int(element_item, "defenseAtt") != 0:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.DEFENSE_ATT, 4)

                    if xml_get_element_to_int(element_item, "defenseState") != 0:
                        self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.DEFENSE_STATE, 4)

                    thaw:int = xml_get_element_to_int(element_item, "thaw")
                    if thaw != 0:
                        if thaw > 0:
                            self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.MAP_PROTECTION, 1)
                        else:
                            self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.MAP_PROTECTION, 2)

                    self.m_cardStats:CardItemupStats = CardItemupStats(itemupCode, prob, areas, inParty)
                    pass
                elif ItemId.is_exp_increase(id):
                    self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.EXP_INCREASE, xml_get_element_to_int(element_item, "expinc"))

            else: # if is_skill == False:
                if self.is_map_chair(id):
                    self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.MAP_CHAIR, 1)
                elif ((id == Beginner.NIMBLE_FEET
                      or id == Noblesse.NIMBLE_FEET
                      or id == Evan.NIMBLE_FEET
                      or id == Legend.AGILE_BODY)
                    and get_MapleStoryConfig().m_use_ultra_nimble_feet):
                    self.m_jump = self.m_speed * 4
                    self.m_speed = self.m_speed * 15
                pass 

            
            self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.WATK, self.m_watk)
            self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.WDEF, self.m_wdef)
            self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.MATK, self.m_matk)
            self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.MDEF, self.m_mdef)
            self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.ACC, self.m_acc)
            self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.AVOID, self.m_avoid)
            self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.SPEED, self.m_speed)
            self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.JUMP, self.m_jump)
            self.add_buff_statPair_to_list_if_not_zero(statups, BuffStat.EXP_BUFF, self.m_expbuff)
            
            pass # if self.m_over_time and self.get_summon_movement_type() == None:
            
        ltd:ET.Element = xml_get_element_item(element_item, "ltd")
        if ltd != None:
            # debug 
            if (get_MapleStoryConfig().m_use_ultra_nimble_feet 
                and (id == Beginner.ECHO_OF_HERO
                     or id == Noblesse.ECHO_OF_HERO
                     or id == Legend.ECHO_OF_HERO
                     or id == Evan.ECHO_OF_HERO)):
                self.m_lt:tuple = tuple(0x80000000, 0x80000000)
                self.m_rb:tuple = tuple(0x80000000, 0x80000000)
            pass

        x:int = xml_get_element_to_int(element_item, "x")
        if ((id == Beginner.ECHO_OF_HERO
                or id == Noblesse.ECHO_OF_HERO
                or id == Legend.ECHO_OF_HERO
                or id == Evan.ECHO_OF_HERO)
            and get_MapleStoryConfig().m_use_ultra_nimble_feet):
            x = x * 10
            pass

        self.m_x = x
        self.m_y = xml_get_element_to_int(element_item, "y")
        
        self.m_damage = xml_get_element_to_int(element_item, "damage")
        self.m_fixdamage = xml_get_element_to_int(element_item, "fixdamage")
        self.m_attackCount = xml_get_element_to_int(element_item, "attackCount")
        self.m_bulletCount = xml_get_element_to_int(element_item, "bulletCount")
        self.m_bulletConsume = xml_get_element_to_int(element_item, "bulletConsume")
        self.m_moneyCon = xml_get_element_to_int(element_item, "moneyCon")
        self.m_itemCon = xml_get_element_to_int(element_item, "itemCon")
        self.m_itemConNo = xml_get_element_to_int(element_item, "itemConNo")
        self.m_moveTo = xml_get_element_to_int(element_item, "moveTo")

        monsterStatus:dict = dict()
        if is_skill:
            if (id == Beginner.RECOVERY
                or id == Noblesse.RECOVERY
                or id == Legend.RECOVERY
                or id == Evan.RECOVERY):
                statups.append(dict(BuffStat.RECOVERY, x)) 
                pass
            elif (id == Beginner.ECHO_OF_HERO
                or id == Noblesse.ECHO_OF_HERO
                or id == Legend.ECHO_OF_HERO
                or id == Evan.ECHO_OF_HERO):
                statups.append(dict(BuffStat.ECHO_OF_HERO, self.m_x))
                pass
            elif (id == Beginner.MONSTER_RIDER
                or id == Noblesse.MONSTER_RIDER
                or id == Legend.MONSTER_RIDER
                or id == Corsair.BATTLE_SHIP
                or id == Beginner.SPACESHIP
                or id == Noblesse.SPACESHIP
                or id == Beginner.YETI_MOUNT1
                or id == Beginner.YETI_MOUNT2
                or id == Noblesse.YETI_MOUNT1
                or id == Noblesse.YETI_MOUNT2
                or id == Legend.YETI_MOUNT1
                or id == Legend.YETI_MOUNT2
                or id == Beginner.WITCH_BROOMSTICK
                or id == Noblesse.WITCH_BROOMSTICK
                or id == Legend.WITCH_BROOMSTICK
                or id == Beginner.BALROG_MOUNT
                or id == Noblesse.BALROG_MOUNT
                or id == Legend.BALROG_MOUNT):
                statups.append(dict(BuffStat.MONSTER_RIDING, id)) 
                pass
            elif (id == Beginner.INVINCIBLE_BARRIER
                or id == Noblesse.INVINCIBLE_BARRIER
                or id == Legend.INVICIBLE_BARRIER
                or id == Evan.INVINCIBLE_BARRIER):
                statups.append(dict(BuffStat.DIVINE_BODY, 1)) 
                pass
            elif (id == Fighter.POWER_GUARD
                or id == Page.POWER_GUARD):
                statups.append(dict(BuffStat.POWERGUARD, x)) 
                pass
            elif (id == Spearman.HYPER_BODY
                or id == GM.HYPER_BODY
                or id == SuperGM.HYPER_BODY):
                statups.append(dict(BuffStat.HYPERBODYHP, x))
                statups.append(dict(BuffStat.HYPERBODYMP, self.m_x))  
                pass
            elif (id == Crusader.COMBO
                or id == DawnWarrior.COMBO):
                statups.append(dict(BuffStat.COMBO, 1)) 
                pass
            elif (id == WhiteKnight.BW_FIRE_CHARGE
                or id == WhiteKnight.BW_ICE_CHARGE
                or id == WhiteKnight.BW_LIT_CHARGE
                or id == WhiteKnight.SWORD_FIRE_CHARGE
                or id == WhiteKnight.SWORD_ICE_CHARGE
                or id == WhiteKnight.SWORD_LIT_CHARGE
                or id == Paladin.BW_HOLY_CHARGE
                or id == Paladin.SWORD_HOLY_CHARGE
                or id == DawnWarrior.SOUL_CHARGE
                or id == ThunderBreaker.LIGHTNING_CHARGE): 
                statups.append(dict(BuffStat.WK_CHARGE, x)) 
                pass
            elif (id == DragonKnight.DRAGON_BLOOD):
                statups.append(dict(BuffStat.DRAGONBLOOD, self.m_x)) 
                pass 
            elif (id == Hero.STANCE
                or id == Paladin.STANCE
                or id == DarkKnight.STANCE
                or id == Aran.FREEZE_STANDING): 
                statups.append(dict(BuffStat.STANCE, ipro)) 
                pass
            elif (id == DawnWarrior.FINAL_ATTACK
                or id == WindArcher.FINAL_ATTACK):
                statups.append(dict(BuffStat.FINALATTACK, x)) 
                pass
            elif (id == Magician.MAGIC_GUARD
                or id == BlazeWizard.MAGIC_GUARD
                or id == Evan.MAGIC_GUARD):
                statups.append(dict(BuffStat.MAGIC_GUARD, x)) 
                pass
            elif (id == Cleric.INVINCIBLE):
                statups.append(dict(BuffStat.INVINCIBLE, x))  
                pass
            elif (id == Priest.HOLY_SYMBOL
                or id == SuperGM.HOLY_SYMBOL):
                statups.append(dict(BuffStat.HOLY_SYMBOL, x))   
                pass
            elif (id == FPArchMage.INFINITY
                or id == ILArchMage.INFINITY
                or id == Bishop.INFINITY):
                statups.append(dict(BuffStat.INFINITY, x)) 
                pass
            elif (id == FPArchMage.MANA_REFLECTION
                or id == ILArchMage.MANA_REFLECTION
                or id == Bishop.MANA_REFLECTION):
                statups.append(dict(BuffStat.MANA_REFLECTION, x))  
                pass
            elif (id == Bishop.HOLY_SHIELD):
                statups.append(dict(BuffStat.HOLY_SHIELD, x))   
                pass
            elif (id == BlazeWizard.ELEMENTAL_RESET
                or id == Evan.ELEMENTAL_RESET):
                statups.append(dict(BuffStat.ELEMENTAL_RESET, x))    
                pass
            elif (id == Evan.MAGIC_SHIELD):
                statups.append(dict(BuffStat.MAGIC_SHIELD, x))  
                pass
            elif (id == Evan.MAGIC_RESISTANCE):
                statups.append(dict(BuffStat.MAGIC_RESISTANCE, x))   
                pass 
            elif (id == Evan.SLOW):
                statups.append(dict(BuffStat.SLOW, x)) 
                pass 
            elif (id == Priest.MYSTIC_DOOR
                or id == Hunter.SOUL_ARROW
                or id == Crossbowman.SOUL_ARROW
                or id == WindArcher.SOUL_ARROW): 
                statups.append(dict(BuffStat.SOULARROW, x))  
                pass
            elif (id == Ranger.PUPPET
                or id == Sniper.PUPPET
                or id == WindArcher.PUPPET
                or id == Outlaw.OCTOPUS
                or id == Corsair.WRATH_OF_THE_OCTOPI): 
                statups.append(dict(BuffStat.PUPPET, 1)) 
                pass
            elif (id == Bowmaster.CONCENTRATE):
                statups.append(dict(BuffStat.CONCENTRATE, x)) 
                pass
            elif (id == Bowmaster.HAMSTRING): 
                statups.append(dict(BuffStat.HAMSTRING, x))
                monsterStatus[MonsterStatus.SPEED] = x
                pass
            elif (id == Marksman.BLIND):
                statups.append(dict(BuffStat.BLIND, x)) 
                monsterStatus[MonsterStatus.ACC] = x
                pass
            elif (id == Bowmaster.SHARP_EYES
                or id == Marksman.SHARP_EYES):
                statups.append(dict(BuffStat.SHARP_EYES, (self.m_x << 8) | self.m_y))  
                pass
            elif (id == WindArcher.WIND_WALK):
                statups.append(dict(BuffStat.WIND_WALK, x)) 
                statups.append(dict(BuffStat.DARKSIGHT, x))  
                pass
            elif (id == Rogue.DARK_SIGHT
                or id == NightWalker.DARK_SIGHT):
                statups.append(dict(BuffStat.DARKSIGHT, x))   
                pass
            elif (id == Hermit.MESO_UP):
                statups.append(dict(BuffStat.MESOUP, x))
                pass
            elif (id == Hermit.SHADOW_PARTNER
                or id == NightWalker.SHADOW_PARTNER):
                statups.append(dict(BuffStat.SHADOWPARTNER, x)) 
                pass
            elif (id == ChiefBandit.MESO_GUARD):
                statups.append(dict(BuffStat.MESOGUARD, x)) 
                pass 
            elif (id == ChiefBandit.PICKPOCKET):
                statups.append(dict(BuffStat.PICKPOCKET, x)) 
                pass
            elif (id == NightLord.SHADOW_STARS):
                statups.append(dict(BuffStat.SHADOW_CLAW, 0)) 
                pass
            # PIRATE
            elif (id == Pirate.DASH
                or id == ThunderBreaker.DASH
                or id == Beginner.SPACE_DASH
                or id == Noblesse.SPACE_DASH): 
                statups.append(dict(BuffStat.DASH2, self.m_x)) 
                statups.append(dict(BuffStat.DASH, self.m_y))  
                pass
            elif (id == Corsair.SPEED_INFUSION
                or id == Buccaneer.SPEED_INFUSION
                or id == ThunderBreaker.SPEED_INFUSION): 
                statups.append(dict(BuffStat.SPEED_INFUSION, x)) 
                pass
            elif (id == Outlaw.HOMING_BEACON
                or id == Corsair.BULLSEYE): 
                statups.append(dict(BuffStat.HOMING_BEACON, x)) 
                pass
            elif (id == ThunderBreaker.SPARK):
                statups.append(dict(BuffStat.SPARK, x)) 
                pass
            # MULTIPLE
            elif (id == Aran.POLEARM_BOOSTER
                or id == Fighter.AXE_BOOSTER
                or id == Fighter.SWORD_BOOSTER
                or id == Page.BW_BOOSTER
                or id == Page.SWORD_BOOSTER
                or id == Spearman.POLEARM_BOOSTER
                or id == Spearman.SPEAR_BOOSTER
                or id == Hunter.BOW_BOOSTER
                or id == Crossbowman.CROSSBOW_BOOSTER
                or id == Assassin.CLAW_BOOSTER
                or id == Bandit.DAGGER_BOOSTER
                or id == FPMage.SPELL_BOOSTER
                or id == ILMage.SPELL_BOOSTER
                or id == Brawler.KNUCKLER_BOOSTER
                or id == Gunslinger.GUN_BOOSTER
                or id == DawnWarrior.SWORD_BOOSTER
                or id == BlazeWizard.SPELL_BOOSTER
                or id == WindArcher.BOW_BOOSTER
                or id == NightWalker.CLAW_BOOSTER
                or id == ThunderBreaker.KNUCKLER_BOOSTER
                or id == Evan.MAGIC_BOOSTER
                or id == Beginner.POWER_EXPLOSION
                or id == Noblesse.POWER_EXPLOSION
                or id == Legend.POWER_EXPLOSION): 
                statups.append(dict(BuffStat.BOOSTER, x)) 
                pass
            elif (id == Hero.MAPLE_WARRIOR
                or id == Paladin.MAPLE_WARRIOR
                or id == DarkKnight.MAPLE_WARRIOR
                or id == FPArchMage.MAPLE_WARRIOR
                or id == ILArchMage.MAPLE_WARRIOR
                or id == Bishop.MAPLE_WARRIOR
                or id == Bowmaster.MAPLE_WARRIOR
                or id == Marksman.MAPLE_WARRIOR
                or id == NightLord.MAPLE_WARRIOR
                or id == Shadower.MAPLE_WARRIOR
                or id == Corsair.MAPLE_WARRIOR
                or id == Buccaneer.MAPLE_WARRIOR
                or id == Aran.MAPLE_WARRIOR
                or id == Evan.MAPLE_WARRIOR):
                statups.append(dict(BuffStat.MAPLE_WARRIOR,  self.m_x))  
                pass
            # SUMMON
            elif (id == Ranger.SILVER_HAWK
                or id == Sniper.GOLDEN_EAGLE):
                statups.append(dict(BuffStat.SUMMON,  self.m_x))   
                monsterStatus[MonsterStatus.STUN] = 1
                pass
            elif (id == FPArchMage.ELQUINES
                or id == Marksman.FROST_PREY):
                statups.append(dict(BuffStat.SUMMON,  self.m_x))    
                monsterStatus[MonsterStatus.FREEZE] = 1
                pass
            elif (id == Priest.SUMMON_DRAGON
                or id == Bowmaster.PHOENIX
                or id == ILArchMage.IFRIT
                or id == Bishop.BAHAMUT
                or id == DarkKnight.BEHOLDER
                or id == Outlaw.GAVIOTA
                or id == DawnWarrior.SOUL
                or id == BlazeWizard.FLAME
                or id == WindArcher.STORM
                or id == NightWalker.DARKNESS
                or id == ThunderBreaker.LIGHTNING
                or id == BlazeWizard.IFRIT):
                statups.append(dict(BuffStat.SUMMON,  self.m_x))
                pass
            # ----------------------------- MONSTER STATUS ----------------------------------
            elif (id == Crusader.ARMOR_CRASH
                or id == DragonKnight.POWER_CRASH
                or id == WhiteKnight.MAGIC_CRASH):  
                monsterStatus[MonsterStatus.SEAL_SKILL] = 1
                pass
            elif (id == Rogue.DISORDER):
                monsterStatus[MonsterStatus.WATK] = self.m_x
                monsterStatus[MonsterStatus.WDEF] = self.m_y
                pass
            elif (id == Corsair.HYPNOTIZE):
                monsterStatus[MonsterStatus.INERTMOB] = 1
                pass
            elif (id == NightLord.NINJA_AMBUSH
                  or id == Shadower.NINJA_AMBUSH):
                monsterStatus[MonsterStatus.NINJA_AMBUSH] = self.m_damage
                pass
            elif (id == Page.THREATEN):
                monsterStatus[MonsterStatus.WATK] = self.m_x
                monsterStatus[MonsterStatus.WDEF] = self.m_y
                pass
            elif (id == DragonKnight.DRAGON_ROAR):
                self.m_hpR = -x / 100.0
                monsterStatus[MonsterStatus.STUN] = 1
                pass
            elif (id == Crusader.AXE_COMA
                or id == Crusader.SWORD_COMA
                or id == Crusader.SHOUT
                or id == WhiteKnight.CHARGE_BLOW
                or id == Hunter.ARROW_BOMB
                or id == ChiefBandit.ASSAULTER
                or id == Shadower.BOOMERANG_STEP
                or id == Brawler.BACK_SPIN_BLOW
                or id == Brawler.DOUBLE_UPPERCUT
                or id == Buccaneer.DEMOLITION
                or id == Buccaneer.SNATCH
                or id == Buccaneer.BARRAGE
                or id == Gunslinger.BLANK_SHOT
                or id == DawnWarrior.COMA
                or id == ThunderBreaker.BARRAGE
                or id == Aran.ROLLING_SPIN
                or id == Evan.FIRE_BREATH
                or id == Evan.BLAZE):  
                monsterStatus[MonsterStatus.STUN] = 1
                pass
            elif (id == NightLord.TAUNT
                or id == Shadower.TAUNT):  
                monsterStatus[MonsterStatus.SHOWDOWN] = self.m_x
                monsterStatus[MonsterStatus.MDEF] = self.m_x
                monsterStatus[MonsterStatus.WDEF] = self.m_x
                pass
            elif (id == ILWizard.COLD_BEAM
                or id == ILMage.ICE_STRIKE
                or id == ILArchMage.BLIZZARD
                or id == ILMage.ELEMENT_COMPOSITION
                or id == Sniper.BLIZZARD
                or id == Outlaw.ICE_SPLITTER
                or id == FPArchMage.PARALYZE
                or id == Aran.COMBO_TEMPEST
                or id == Evan.ICE_BREATH):  
                monsterStatus[MonsterStatus.FREEZE] = 1
                self.m_duration = self.m_duration * 2
                pass
            elif (id == FPWizard.SLOW
                or id == ILWizard.SLOW
                or id == BlazeWizard.SLOW):  
                monsterStatus[MonsterStatus.SPEED] = 1
                pass
            elif (id == FPWizard.POISON_BREATH
                or id == FPMage.ELEMENT_COMPOSITION):  
                monsterStatus[MonsterStatus.POISON] = 1
                pass 
            elif (id == Priest.DOOM):  
                monsterStatus[MonsterStatus.DOOM] = 1
                pass
            elif (id == ILMage.SEAL
                or id == FPMage.SEAL
                or id == BlazeWizard.SEAL):  
                monsterStatus[MonsterStatus.SEAL] = 1
                pass
            elif (id == Hermit.SHADOW_WEB # shadow web
                or id == NightWalker.SHADOW_WEB):  
                monsterStatus[MonsterStatus.SHADOW_WEB] = 1
                pass 
            elif (id == FPArchMage.FIRE_DEMON
                or id == ILArchMage.ICE_DEMON):  
                monsterStatus[MonsterStatus.POISON] = 1
                monsterStatus[MonsterStatus.FREEZE] = 1
                pass 
            elif (id == Evan.PHANTOM_IMPRINT):
                monsterStatus[MonsterStatus.PHANTOM_IMPRINT] = x
                pass 
            # ARAN 
            elif (id == Aran.COMBO_ABILITY):
                statups[BuffStat.ARAN_COMBO] = 100 
                pass
            elif (id == Aran.COMBO_BARRIER):
                statups[BuffStat.COMBO_BARRIER] = self.m_x 
                pass
            elif (id == Aran.COMBO_DRAIN):
                statups[BuffStat.COMBO_DRAIN] = self.m_x 
                pass
            elif (id == Aran.SMART_KNOCKBACK):
                statups[BuffStat.SMART_KNOCKBACK] = self.m_x 
                pass
            elif (id == Aran.BODY_PRESSURE):
                statups[BuffStat.BODY_PRESSURE] = self.m_x 
                pass
            elif (id == Aran.SNOW_CHARGE):
                statups[BuffStat.WK_CHARGE] = self.m_duration 
                pass
            else:
                pass
 
            pass # if is_skill:

        if self.is_morph():
            statups.append({BuffStat.MORPH,  self.get_morph()})
            
        if self.m_ghost > 0 and is_skill == False:
            statups.append({BuffStat.GHOST_MORPH,  self.m_ghost}) 
        
        self.m_monsterStatus:dict = monsterStatus
        self.m_statups:list = statups 
        return
    

    def add_buff_statPair_to_list_if_not_zero(self, statups:list, buffstat:BuffStat, val:int) -> None:
        if val != 0:
            statups.append({buffstat.get_value(), val}) 


    def map_protection(self, sourceid:int) -> int: 
        if sourceid == ItemId.RED_BEAN_PORRIDGE or sourceid == ItemId.SOFT_WHITE_BUN:
            return 1
        elif sourceid == ItemId.AIR_BUBBLE:
            return 2
        else:
            return 0
    
    def get_summon_movement_type(self) -> SummonMovementType:
        if self.m_skill == False:
            return None
        
        if (self.m_sourceid == Ranger.PUPPET
            or self.m_sourceid == Sniper.PUPPET
            or self.m_sourceid == WindArcher.PUPPET
            or self.m_sourceid == Outlaw.OCTOPUS
            or self.m_sourceid == Corsair.WRATH_OF_THE_OCTOPI):
            return SummonMovementType.STATIONARY
        
        if (self.m_sourceid == Ranger.SILVER_HAWK
            or self.m_sourceid == Sniper.GOLDEN_EAGLE
            or self.m_sourceid == Priest.SUMMON_DRAGON
            or self.m_sourceid == Marksman.FROST_PREY
            or self.m_sourceid == Bowmaster.PHOENIX
            or self.m_sourceid == Outlaw.GAVIOTA):
            return SummonMovementType.CIRCLE_FOLLOW
        
        if (self.m_sourceid == DarkKnight.BEHOLDER
            or self.m_sourceid == FPArchMage.ELQUINES
            or self.m_sourceid == ILArchMage.IFRIT
            or self.m_sourceid == Bishop.BAHAMUT
            or self.m_sourceid == DawnWarrior.SOUL
            or self.m_sourceid == BlazeWizard.FLAME
            or self.m_sourceid == BlazeWizard.IFRIT
            or self.m_sourceid == WindArcher.STORM
            or self.m_sourceid == NightWalker.DARKNESS
            or self.m_sourceid == ThunderBreaker.LIGHTNING):
            return SummonMovementType.FOLLOW
        
        return None
    
    def is_hp_mp_recovery(self, id:int) -> bool:
        return id == ItemId.RUSSELLONS_PILLS or id == ItemId.SORCERERS_POTION
    
    def is_map_chair(self) -> bool:
        return self.m_sourceid == Beginner.MAP_CHAIR or self.m_sourceid == Noblesse.MAP_CHAIR or self.m_sourceid == Legend.MAP_CHAIR    
    
    def is_map_chair(self, id:int) -> bool:
        return id == Beginner.MAP_CHAIR or id == Noblesse.MAP_CHAIR or id == Legend.MAP_CHAIR
    
    def is_morph(self) -> bool:
        return self.m_morph > 0
    
    def get_morph(self) -> int:
        return self.m_morph