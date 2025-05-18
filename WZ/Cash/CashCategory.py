from enum import Enum

class CategoryType(Enum):
    MAIN = (8, "MAIN")
    EVENT = (1, "EVENT")
    EQUIP = (2, "EQUIP")
    USE = (3, "USE")
    SET = (4, "SET")
    ETC = (5, "ETC")
    PET = (6, "PET")
    PACKAGE = (7, "PACKAGE")

    def __init__(self, id:int, name:str):
        self.m_id:int = id
        self.m_name:str = name 
        return
    
    @classmethod
    def of_id(cls, id):
        for type_ in cls:
            if type_.m_id == id:
                return type_
        return None
     
  
    def to_name(id:int) -> str:
        ct:CategoryType = CategoryType.of_id(id)
        if ct == None:
            return ""
        
        return ct.m_name

class CashCategory: 
    def __init__(self,):
        self.m_id:int = 0
        self.m_name:str = ""
        self.m_sub_id:int = 0
        self.m_sub_name:str = ""
        self.m_on_sale:bool = False
        self.m_item_id:int = 0
        pass