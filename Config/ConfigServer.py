from Config.ConfigBase import *

class ConfigServer(ConfigBase):
    def __init__(self, config_path) -> None:
        super().__init__(config_path)
    
        self.m_timeTaskPurge = self.get_item('timeTaskPurge')
        self.m_commonRefresh = self.get_item('commonRefresh')
        self.m_host = self.get_item('host')
        self.m_localServer = self.get_item('localServer')
        self.m_useIpValidation = self.get_item('useIpValidation')
        self.m_useCharacterAccountCheck = self.get_item('useCharacterAccountCheck')
        self.m_useMaxRange = self.get_item('useMaxRange')
        self.m_lockMonitorTime = self.get_item('lockMonitorTime')

    
        return
     