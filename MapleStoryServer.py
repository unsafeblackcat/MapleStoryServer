import sys  
import os 
import asyncio

from Config.MapleStoryConfig import *
from MySQLdb.MapleStroyDB import * 
from Socket.SocketLogin import SocketLogin
from Socket.SocketChannel import SocketChannel
 
async def socket_wait():
    socket_login = SocketLogin("127.0.0.1", 8484, 30)  
    socket_login.m_server = await asyncio.start_server(socket_login._socket_callback
                , socket_login.m_ip
                , socket_login.m_port)
    
    socket_channel = SocketChannel("127.0.0.1", 7575, 30) 
    socket_channel.m_server = await asyncio.start_server(socket_channel._socket_callback
                , socket_channel.m_ip
                , socket_channel.m_port)
    

    async with socket_login.m_server, socket_channel.m_server:
        await asyncio.gather(
            socket_login.m_server.serve_forever()
            , socket_channel.m_server.serve_forever())

    pass

def main(argc, argv):  
    
    maplestory_config = MapleStoryConfig(os.getcwd() + '/Resources/config/')
    maplestroy_db = MapleStroyDB(
        maplestory_config.m_database.m_dbUrl
        , maplestory_config.m_database.m_dbUser
        , maplestory_config.m_database.m_dbPass
        , os.getcwd() + '/Resources/sql/')
      
    #iret = 0
    #while True:

     #   iret = maplestroy_db.init(maplestory_config.m_game)
      #  if iret :
       #     break
        
        #break

    asyncio.run(socket_wait()) 
    while True:
        time.sleep(1000)
        pass
    
    return 0
 
#debian apt -y install python3-pycryptodome
#windows pip install pycryptodome
if __name__ == "__main__":
    main(len(sys.argv), sys.argv)