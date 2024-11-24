from Config.ConfigServer import *
from Config.ConfigDataBase import *
from Config.ConfigDebug import *
from Config.ConfigGame import *
from Config.ConfigGM import *
from Config.ConfigWorld import *


class MapleStoryConfig:
    def __init__(self, config_dir:str) -> None:
        
        server = config_dir + 'server.config' 
        self.m_server = ConfigServer(server)

        database = config_dir + 'database.config' 
        self.m_database = ConfigDataBase(database)

        debug = config_dir + 'debug.config' 
        self.m_debug = ConfigDebug(debug)

        game = config_dir + 'game.config' 
        self.m_game = ConfigGame(game)

        world = config_dir + 'world.config' 
        self.m_world = ConfigWorld(world)
         
        gm = config_dir + 'gm.config' 
        self.m_gm = ConfigGM(gm)
        pass