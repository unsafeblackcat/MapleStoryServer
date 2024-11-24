from Config.ConfigBase import *

class ConfigDebug(ConfigBase):
    def __init__(self, config_path) -> None:
        super().__init__(config_path)

        self.m_useDebug = self.get_item('useDebug')
        self.m_debugLevel = self.get_item('debugLevel')
        self.m_useThreadTracker = self.get_item('useThreadTracker')
        return