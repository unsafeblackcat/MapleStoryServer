from Config.ConfigBase import *

class ConfigWorld(ConfigBase):
    def __init__(self, config_path) -> None:
        super().__init__(config_path)
 
        self.m_channelIds = self.get_item('channelIds')
        self.m_serverMessage = self.get_item('serverMessage')
        self.m_eventMessage = self.get_item('eventMessage')
        self.m_recommendedMessage = self.get_item('recommendedMessage')
        self.m_expRate = self.get_item('expRate')
        self.m_mesoRate = self.get_item('mesoRate')
        self.m_dropRate = self.get_item('dropRate')
        self.m_bossDropRate = self.get_item('bossDropRate')
        self.m_questRate = self.get_item('questRate')
        self.m_travelRate = self.get_item('travelRate')
        self.m_fishingRate = self.get_item('fishingRate')
        self.m_channelLoad = self.get_item('channelLoad')
        self.m_channelLocks = self.get_item('channelLocks')
        return