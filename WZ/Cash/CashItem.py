
class CashItem:
    def __init__(self
                 , sn:int
                 , itemid:int
                 , count:int
                 , price:int
                 , bouns:int
                 , priority:int
                 , period:int
                 , maplepoint:int
                 , meso:int
                 , fpu:int
                 , cg:int
                 , os:int
                 , clz:int
                 , limit:int
                 , pbc:int
                 , pbp:int
                 , pbg:int
                 , psn:int):
        # sn码
        self.m_sn = sn
        # 物品id
        self.m_item_id = itemid
        # 数量
        self.m_count = count
        # 价格
        self.m_price = price
        # 属性奖励
        self.m_bonus = bouns
        # 优先级
        self.m_priority = priority
        # 有效期
        self.m_period = period
        # 抵用券
        self.m_maple_point = maplepoint
        # 金币
        self.m_meso = meso
        # 高级用户
        self.m_for_premium_user = fpu
        # 性别
        self.m_commodity_gender = cg
        # 是否销售
        self.m_on_sale = os

        self.m_clz = clz

        self.m_limit = limit

        self.m_pb_cash = pbc

        self.m_pb_point = pbp

        self.m_pb_gift = pbg

        # 礼包SN
        self.m_package_sn = psn

        return

    def is_selling(self) -> bool:
        return self.m_on_sale != 0 and self.m_on_sale == 1