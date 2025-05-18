from enum import Enum 

class SummonMovementType(Enum):
    STATIONARY =(0)
    FOLLOW = (1)
    CIRCLE_FOLLOW = (3)

    def __init__(self, value:int):
        self.m_value:int = value   

    def get_value(self) -> int:
        return self.m_value 