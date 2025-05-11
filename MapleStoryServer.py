import sys  
import os 
import asyncio
import xml.etree.ElementTree as ET

from Config.MapleStoryConfig import *
from MySQLdb.MapleStroyDB import * 
from Socket.SocketLogin import SocketLogin
from Socket.SocketChannel import SocketChannel
from WZ.SkillFactory import *
 
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


def list_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            file_list.append(full_path)
    return file_list


def getInt(path, xmlit, re = -1):
    iret = re

    for node in xmlit.iter():
        print(node.tag, node.attrib, node.text)
 
    return  iret

def loadFromData(id, xmlit):

    id = getInt("skillType", xmlit, -1)

    return

def main(argc, argv):    

    strpath = os.getcwd() + '/Resources/wz/Skill.wz' 
    files = list_all_files(strpath)
    for it in files: 
        tree = ET.parse(it)
        root = tree.getroot()
        for child in root:
            print(child.tag, child.attrib, child.text)
            if (child.tag == 'imgdir' and child.attrib.get('name') == 'skill'):
                for skill_entry in child:
                    skillid = int(skill_entry.get('name'))

                    loadFromData(skillid, skill_entry)
 
                pass
            pass
        pass
    

    i = 0



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
    load_skill()


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