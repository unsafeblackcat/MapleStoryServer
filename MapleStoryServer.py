import sys   
import asyncio 

from Config.MapleStoryConfig import *
from MySQLdb.MapleStroyDB import * 
from Socket.SocketLogin import SocketLogin
from Socket.SocketChannel import SocketChannel
from WZ.Skills.SkillFactory import * 
from WZ.Cash.CashItemFactory import *
 
async def socket_wait():
    socket_login = SocketLogin("127.0.0.1", 8484, 10)  
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
    get_skill_factory().init()
    get_cash_item_factory().init()
    # set_dbg()
    
    maplestory_config = get_MapleStoryConfig()

    maplestroy_db = MapleStroyDB(
        maplestory_config.m_database.m_dbUrl
        , maplestory_config.m_database.m_dbUser
        , maplestory_config.m_database.m_dbPass
        , os.getcwd() + '/Resources/sql/') 
    iret = maplestroy_db.init(maplestory_config.m_game)
    if iret :
        print('数据库初始化失败, Maplestory服务端停止启动。错误码: ' + iret)
        return
     
    print('开始加载技能WZ... ')    

    print('开始创建Socket... ')

    asyncio.run(socket_wait()) 
    while True:
        time.sleep(1000)
        pass
    
    return 0
 
# debian apt -y install python3-pycryptodome
# windows pip install pycryptodome
# pip install mysql-connector-python
if __name__ == "__main__":
    main(len(sys.argv), sys.argv)