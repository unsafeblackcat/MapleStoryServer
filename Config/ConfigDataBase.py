from Config.ConfigBase import *

class ConfigDataBase(ConfigBase):
    def __init__(self, config_path) -> None:
        super().__init__(config_path)

        # database
        self.m_dbUrl = self.get_item('dbUrl')
        self.m_dbUser = self.get_item('dbUser')
        self.m_dbPass = self.get_item('dbPass')
        self.m_dbMaxConnect = self.get_item('dbMaxConnect')
        return