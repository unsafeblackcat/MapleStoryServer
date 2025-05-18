
from PublicFun import * 
from WZ.WZFile import *  
from WZ.Cash.CashItem import * 
from WZ.Cash.CashCategory import * 

class CashItemFactory:
    def __init__(self):
        self.m_items:dict[int, CashItem] = dict()
        self.m_packages:dict[int, list] = dict()
        self.m_modifiedCashItems:dict[int, CashItem] = dict()
        self.m_cash_categories:list[CashCategory] = list()
        pass

    def init(self):
        wz:WZFile = WZFile(WZFileEnum.ETC)
        ect_wz:str = wz.get_file_path()

        xml_parse = xml_get_file_parse(ect_wz, "Commodity.img")
        if xml_parse != None:
            root = xml_parse.getroot()  
            for it in root: 
                sn:int = xml_get_element_to_int(it, "SN")
                itemId:int = xml_get_element_to_int(it, "ItemId")
                price:int = xml_get_element_to_int(it, "Price")
                period:int = xml_get_element_to_int(it, "Period")
                count:int = xml_get_element_to_int(it, "Count")
                onSale:int = xml_get_element_to_int(it, "OnSale")
                priority:int = xml_get_element_to_int(it, "Priority")
 
                bonus:int = xml_get_element_to_int(it, "Bonus")
                maplePoint:int = xml_get_element_to_int(it, "MaplePoint")
                meso:int = xml_get_element_to_int(it, "Meso")
                forPremiumUser:int = xml_get_element_to_int(it, "ForPremiumUser")
                gender:int = xml_get_element_to_int(it, "Gender")
                clz:int = xml_get_element_to_int(it, "Class")

                # limit一堆问号，是有问题还是就是这样？暂不解析这个字段
                # Integer limit = DataTool.getInteger("Limit", item);
                limit = 0

                
                pbCash:int = xml_get_element_to_int(it, "PbCash")
                pbPoint:int = xml_get_element_to_int(it, "PbPoint")
                pbGift:int = xml_get_element_to_int(it, "PbGift")
                packageSN:int = xml_get_element_to_int(it, "PackageSN")

                if period == 0:
                    period = 90
                else:
                    period = period
                mcod:CashItem = CashItem(
                    sn
                    , itemId
                    , count
                    , price
                    , bonus
                    , priority
                    , period
                    , maplePoint
                    , meso
                    , forPremiumUser
                    , gender
                    , onSale
                    , clz
                    , limit
                    , pbCash
                    , pbPoint
                    , pbGift
                    , packageSN)
                self.m_items[sn] = mcod 
                pass
 
            pass
        

        xml_parse = xml_get_file_parse(ect_wz, "CashPackage.img")
        if xml_parse != None:
            root = xml_parse.getroot()  
            for it in root: 
                slist:list = list()
                for subit in it:
                    if subit.get('name') == 'SN': 
                        i:int = 0
                        for ssubit in subit:  
                            slist.append(xml_get_type_data(ssubit, str(i)))
                            i = i + 1
                            pass 
                        pass

                self.m_packages[it.get("name")] = slist
                pass

            pass # if xml_parse != None:
 
        self.load_cash_categories()
        self.load_all_modified_cash_items()
        return
    
    def load_cash_categories(self) -> None:
        self.m_modifiedCashItems.clear()
        self.m_cash_categories = self._get_all_category_list()
        return
        
    
    def _get_all_category_list(self) -> list[CashCategory]:
        wz:WZFile = WZFile(WZFileEnum.ETC)
        ect_wz:str = wz.get_file_path()

        ret_list:list[CashCategory] = None

        xml_parse = xml_get_file_parse(ect_wz, "Category.img")
        if xml_parse != None:
            root = xml_parse.getroot()  
            
            ret_list = list()
            
            for it in root:
                cc:CashCategory = CashCategory() 
                cc.m_id = xml_get_element_to_int(it, "Category")
                cc.m_sub_id = xml_get_element_to_int(it, "CategorySub")
                cc.m_sub_name = xml_get_element_to_str(it, "Name", "")
                cc.m_name = CategoryType.to_name(cc.m_id)
                
                ret_list.append(cc)
                pass
            pass

        return ret_list
    
    def load_all_modified_cash_items(self) -> None:
        self.m_modifiedCashItems.clear()  
        # loadAllModifiedCashItems 回调是空的
        return

g_CashItemFactory:CashItemFactory = None 

def get_cash_item_factory() -> CashItemFactory:
    global g_CashItemFactory
    if g_CashItemFactory == None:
        g_CashItemFactory = CashItemFactory()
        pass
    return g_CashItemFactory