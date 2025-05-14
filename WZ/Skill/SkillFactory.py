import xml.etree.ElementTree as ET

from PublicFun import * 
from WZ.WZFile import *  
from WZ.Skill.Job.FaShi import *
from WZ.Skill.Job.FeiXia import *
from WZ.Skill.Job.GongJianShou import *
from WZ.Skill.Job.HaiDao import *
from WZ.Skill.Job.QiShiTuan import *
from WZ.Skill.Job.ShenLong import *
from WZ.Skill.Job.SuperGM import *
from WZ.Skill.Job.XinShou import *
from WZ.Skill.Job.ZhanShen import *
from WZ.Skill.Job.ZhanShi import *  
from WZ.Skill.Skill import *
 
class SkillFactory:
    def __init__(self):
        self.m_skills:dict[int, Skill] = {}
        pass

    def get_skill(self, id:int) -> Skill:
        return self.m_skills[id]
    
    def get_skill_name(self, id:int) -> str:
        return '' 
    
    def _load_all_skill(self):
        return
    
    def init(self):
        wz:WZFile = WZFile(WZFileEnum.SKILL)
        skill_wz:str = wz.get_file_path()

        files = enum_dir(skill_wz)
        for it in files: 
            tree = ET.parse(it)
            root = tree.getroot()
            for child in root:
                print(child.tag, child.attrib, child.text)
                if (child.tag == 'imgdir' and child.attrib.get('name') == 'skill'):
                    for skill_element in child:
                        skillid = int(skill_element.get('name'))  
                        skill:Skill = self._get_skill(skillid, skill_element)
                        self.m_skills[skillid] = skill
                        pass   
                    pass
                pass
            pass
        pass

        return
    
    def _get_skill(self, skillid:int, skill_element:ET.Element) -> Skill:
        skill_ret:Skill = Skill(skillid)

        is_buffer:bool = False
        skill_type:int = xml_get_element_to_int(skill_element, "skillType", -1)
        elem:str = xml_get_element_to_str(skill_element, "elemAttr", None)
        if elem != None:
            skill_ret.m_element.from_initial(elem[0])
            pass
        else:
            skill_ret.m_element = SkillElement.NEUTRAL
            pass

        effect_item:ET.Element = xml_get_element_item(skill_element, "effect")

        if skill_type != -1:
            if skill_type == 2:
                is_buffer = True
            pass  
        else:
            is_action:bool = False
            action_item:ET.Element = xml_get_element_item(skill_element, "action")
            if action_item == None: 
                if xml_is_element(skill_element, "prepare/action"):
                    is_action = True
                    pass
                else: 
                    if (id == Gunslinger.INVISIBLE_SHOT 
                        or id == Corsair.HYPNOTIZE):
                        is_action = True
                    pass
                pass
            else:
                is_action = True
                pass

            skill_ret.m_action = is_action
            hit_item:ET.Element = xml_get_element_item(skill_element, "hit")
            ball_item:ET.Element = xml_get_element_item(skill_element, "ball")
            is_buffer = (effect_item != None and hit_item == None and ball_item == None)
            is_buffer = is_buffer | ((action_item != None) and (xml_get_element_to_str(action_item, "0", "") == "alert2"))

            if (id == Hero.RUSH or 
                id == Paladin.RUSH or 
                id == DarkKnight.RUSH or 
                id == DragonKnight.SACRIFICE or 
                id == FPMage.EXPLOSION or 
                id == FPMage.POISON_MIST or 
                id == Cleric.HEAL or 
                id == Ranger.MORTAL_BLOW or 
                id == Sniper.MORTAL_BLOW or 
                id == Assassin.DRAIN or 
                id == Hermit.SHADOW_WEB or 
                id == Bandit.STEAL or 
                id == Shadower.SMOKE_SCREEN or 
                id == SuperGM.HEAL_PLUS_DISPEL or 
                id == Hero.MONSTER_MAGNET or 
                id == Paladin.MONSTER_MAGNET or 
                id == DarkKnight.MONSTER_MAGNET or 
                id == Evan.ICE_BREATH or 
                id == Evan.FIRE_BREATH or 
                id == Gunslinger.RECOIL_SHOT or 
                id == Marauder.ENERGY_DRAIN or 
                id == BlazeWizard.FLAME_GEAR or 
                id == NightWalker.SHADOW_WEB or 
                id == NightWalker.POISON_BOMB or 
                id == NightWalker.VAMPIRE or 
                id == ChiefBandit.CHAKRA or 
                id == Aran.COMBAT_STEP or 
                id == Evan.RECOVERY_AURA):
                is_buffer = False
                pass
            elif (id == Beginner.RECOVERY or 
                id == Beginner.NIMBLE_FEET or 
                id == Beginner.MONSTER_RIDER or 
                id == Beginner.ECHO_OF_HERO or 
                id == Beginner.MAP_CHAIR or 
                id == Warrior.IRON_BODY or 
                id == Fighter.AXE_BOOSTER or 
                id == Fighter.POWER_GUARD or 
                id == Fighter.RAGE or 
                id == Fighter.SWORD_BOOSTER or 
                id == Crusader.ARMOR_CRASH or 
                id == Crusader.COMBO or 
                id == Hero.ENRAGE or 
                id == Hero.HEROS_WILL or 
                id == Hero.MAPLE_WARRIOR or 
                id == Hero.STANCE or 
                id == Page.BW_BOOSTER or 
                id == Page.POWER_GUARD or 
                id == Page.SWORD_BOOSTER or 
                id == Page.THREATEN or 
                id == WhiteKnight.BW_FIRE_CHARGE or 
                id == WhiteKnight.BW_ICE_CHARGE or 
                id == WhiteKnight.BW_LIT_CHARGE or 
                id == WhiteKnight.MAGIC_CRASH or 
                id == WhiteKnight.SWORD_FIRE_CHARGE or 
                id == WhiteKnight.SWORD_ICE_CHARGE or 
                id == WhiteKnight.SWORD_LIT_CHARGE or 
                id == Paladin.BW_HOLY_CHARGE or 
                id == Paladin.HEROS_WILL or 
                id == Paladin.MAPLE_WARRIOR or 
                id == Paladin.STANCE or 
                id == Paladin.SWORD_HOLY_CHARGE or 
                id == Spearman.HYPER_BODY or 
                id == Spearman.IRON_WILL or 
                id == Spearman.POLEARM_BOOSTER or 
                id == Spearman.SPEAR_BOOSTER or 
                id == DragonKnight.DRAGON_BLOOD or 
                id == DragonKnight.POWER_CRASH or 
                id == DarkKnight.AURA_OF_BEHOLDER or 
                id == DarkKnight.BEHOLDER or 
                id == DarkKnight.HEROS_WILL or 
                id == DarkKnight.HEX_OF_BEHOLDER or 
                id == DarkKnight.MAPLE_WARRIOR or 
                id == DarkKnight.STANCE or 
                id == Magician.MAGIC_GUARD or 
                id == Magician.MAGIC_ARMOR or 
                id == FPWizard.MEDITATION or 
                id == FPWizard.SLOW or 
                id == FPMage.SEAL or 
                id == FPMage.SPELL_BOOSTER or 
                id == FPArchMage.HEROS_WILL or 
                id == FPArchMage.INFINITY or 
                id == FPArchMage.MANA_REFLECTION or 
                id == FPArchMage.MAPLE_WARRIOR or 
                id == ILWizard.MEDITATION or 
                id == ILMage.SEAL or 
                id == ILWizard.SLOW or 
                id == ILMage.SPELL_BOOSTER or 
                id == ILArchMage.HEROS_WILL or 
                id == ILArchMage.INFINITY or 
                id == ILArchMage.MANA_REFLECTION or 
                id == ILArchMage.MAPLE_WARRIOR or 
                id == Cleric.INVINCIBLE or 
                id == Cleric.BLESS or 
                id == Priest.DISPEL or 
                id == Priest.DOOM or 
                id == Priest.HOLY_SYMBOL or 
                id == Priest.MYSTIC_DOOR or 
                id == Bishop.HEROS_WILL or 
                id == Bishop.HOLY_SHIELD or 
                id == Bishop.INFINITY or 
                id == Bishop.MANA_REFLECTION or 
                id == Bishop.MAPLE_WARRIOR or 
                id == Archer.FOCUS or 
                id == Hunter.BOW_BOOSTER or 
                id == Hunter.SOUL_ARROW or 
                id == Ranger.PUPPET or 
                id == Bowmaster.CONCENTRATE or 
                id == Bowmaster.HEROS_WILL or 
                id == Bowmaster.MAPLE_WARRIOR or 
                id == Bowmaster.SHARP_EYES or 
                id == Crossbowman.CROSSBOW_BOOSTER or 
                id == Crossbowman.SOUL_ARROW or 
                id == Sniper.PUPPET or 
                id == Marksman.BLIND or 
                id == Marksman.HEROS_WILL or 
                id == Marksman.MAPLE_WARRIOR or 
                id == Marksman.SHARP_EYES or 
                id == Rogue.DARK_SIGHT or 
                id == Assassin.CLAW_BOOSTER or 
                id == Assassin.HASTE or 
                id == Hermit.MESO_UP or 
                id == Hermit.SHADOW_PARTNER or 
                id == NightLord.HEROS_WILL or 
                id == NightLord.MAPLE_WARRIOR or 
                id == NightLord.NINJA_AMBUSH or 
                id == NightLord.SHADOW_STARS or 
                id == Bandit.DAGGER_BOOSTER or 
                id == Bandit.HASTE or 
                id == ChiefBandit.MESO_GUARD or 
                id == ChiefBandit.PICKPOCKET or 
                id == Shadower.HEROS_WILL or 
                id == Shadower.MAPLE_WARRIOR or 
                id == Shadower.NINJA_AMBUSH or 
                id == Pirate.DASH or 
                id == Marauder.TRANSFORMATION or 
                id == Buccaneer.SUPER_TRANSFORMATION or 
                id == Corsair.BATTLE_SHIP or 
                id == GM.HIDE or 
                id == SuperGM.HASTE or 
                id == SuperGM.HOLY_SYMBOL or 
                id == SuperGM.BLESS or 
                id == SuperGM.HIDE or 
                id == SuperGM.HYPER_BODY or 
                id == Noblesse.BLESSING_OF_THE_FAIRY or 
                id == Noblesse.ECHO_OF_HERO or 
                id == Noblesse.MONSTER_RIDER or 
                id == Noblesse.NIMBLE_FEET or 
                id == Noblesse.RECOVERY or 
                id == Noblesse.MAP_CHAIR or 
                id == DawnWarrior.COMBO or 
                id == DawnWarrior.FINAL_ATTACK or 
                id == DawnWarrior.IRON_BODY or 
                id == DawnWarrior.RAGE or 
                id == DawnWarrior.SOUL or 
                id == DawnWarrior.SOUL_CHARGE or 
                id == DawnWarrior.SWORD_BOOSTER or 
                id == BlazeWizard.ELEMENTAL_RESET or 
                id == BlazeWizard.FLAME or 
                id == BlazeWizard.IFRIT or 
                id == BlazeWizard.MAGIC_ARMOR or 
                id == BlazeWizard.MAGIC_GUARD or 
                id == BlazeWizard.MEDITATION or 
                id == BlazeWizard.SEAL or 
                id == BlazeWizard.SLOW or 
                id == BlazeWizard.SPELL_BOOSTER or 
                id == WindArcher.BOW_BOOSTER or 
                id == WindArcher.EAGLE_EYE or 
                id == WindArcher.FINAL_ATTACK or 
                id == WindArcher.FOCUS or 
                id == WindArcher.PUPPET or 
                id == WindArcher.SOUL_ARROW or 
                id == WindArcher.STORM or 
                id == WindArcher.WIND_WALK or 
                id == NightWalker.CLAW_BOOSTER or 
                id == NightWalker.DARKNESS or 
                id == NightWalker.DARK_SIGHT or 
                id == NightWalker.HASTE or 
                id == NightWalker.SHADOW_PARTNER or 
                id == ThunderBreaker.DASH or 
                id == ThunderBreaker.ENERGY_CHARGE or 
                id == ThunderBreaker.ENERGY_DRAIN or 
                id == ThunderBreaker.KNUCKLER_BOOSTER or 
                id == ThunderBreaker.LIGHTNING or 
                id == ThunderBreaker.SPARK or 
                id == ThunderBreaker.LIGHTNING_CHARGE or 
                id == ThunderBreaker.SPEED_INFUSION or 
                id == ThunderBreaker.TRANSFORMATION or 
                id == Legend.BLESSING_OF_THE_FAIRY or 
                id == Legend.AGILE_BODY or 
                id == Legend.ECHO_OF_HERO or 
                id == Legend.RECOVERY or 
                id == Legend.MONSTER_RIDER or 
                id == Legend.MAP_CHAIR or 
                id == Aran.MAPLE_WARRIOR or 
                id == Aran.HEROS_WILL or 
                id == Aran.POLEARM_BOOSTER or 
                id == Aran.COMBO_DRAIN or 
                id == Aran.SNOW_CHARGE or 
                id == Aran.BODY_PRESSURE or 
                id == Aran.SMART_KNOCKBACK or 
                id == Aran.COMBO_BARRIER or 
                id == Aran.COMBO_ABILITY or 
                id == Evan.BLESSING_OF_THE_FAIRY or 
                id == Evan.RECOVERY or 
                id == Evan.NIMBLE_FEET or 
                id == Evan.HEROS_WILL or 
                id == Evan.ECHO_OF_HERO or 
                id == Evan.MAGIC_BOOSTER or 
                id == Evan.MAGIC_GUARD or 
                id == Evan.ELEMENTAL_RESET or 
                id == Evan.MAPLE_WARRIOR or 
                id == Evan.MAGIC_RESISTANCE or 
                id == Evan.MAGIC_SHIELD or 
                id == Evan.SLOW):
                is_buffer = True
                pass
            else:
                pass

            # skill_element
            skill_ret.m_stat_effect.append()

            pass # else
        
        return


g_SkillFactory:SkillFactory = None 

def get_skill_factory() -> SkillFactory:
    global g_SkillFactory
    if g_SkillFactory == None:
        g_SkillFactory = SkillFactory()
        pass
    return g_SkillFactory