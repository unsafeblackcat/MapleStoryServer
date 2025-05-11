 
class Skill:
    def __init__(self):
        pass

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


g_SkillFactory:SkillFactory = None 

def load_skill():
    global g_SkillFactory
    if g_SkillFactory == None:
        g_SkillFactory = SkillFactory()
        pass
    return