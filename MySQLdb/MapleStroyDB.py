import time

from MySQLdb.MySQLdb import *
from Config.ConfigGame import *

class MapleStroyDB(MySQLdb):
    def __init__(self, ip:str, user:str, password:str, sql_dir:str):
        super().__init__(ip, user, password)
        self.m_sql_dir = sql_dir
        return
    
    def init(self, config_gm:ConfigGame) -> int:
        iret = 0

        while True:

            print('[数据库]: 准备连接数据库 ' + self.m_ip + ', ' + self.m_user + ', ' + self.m_password)

            iret = self.connect()
            if iret: break
  
            print('[数据库]: 数据库连接成功... 开始初始化数据库. ')

            self._init_db()
 
            print('[数据库]: 开始更新数据库. ')

            iret = self._updateDataBase()
            if iret : break

            iret = self._init_account()
            if iret : break

            #iret = self._clear_nx_code_coupons(config_gm.m_useClearOutdatedCoupons)
            #if iret : break
 
            break

        return iret
      
    def _init_db(self) -> int:
        iret = 0

        if self._is_maplestory_table():
            return 0

        db_database = self.m_sql_dir + 'db_database.sql'
        self.excel_file_sql(db_database, db_name=None) 

        db_drops = self.m_sql_dir + 'db_drops.sql' 
        self.excel_file_sql(db_drops, db_name=None)

        db_shopupdate = self.m_sql_dir + 'db_shopupdate.sql' 
        self.excel_file_sql(db_shopupdate, db_name=None)
        return iret
    
    def _is_maplestory_table(self) -> int:
        iret = 0
        
        cnx, cursor = self.get_connect_cursor(None) 
        cursor.execute('show databases')
        list_data = cursor.fetchall()
        for it in list_data:
            if len(it):
                if it[0] == 'MapleStoryDB':
                    iret = 1
                    break
            pass

        self.free_connect_cursor(cnx, cursor)
        return iret
    
    def _updateDataBase(self) -> int:
          
        while True:
            iret = self._check_update_log()
            if iret : break  

            break

        return iret
     
    def _check_update_log(self) -> int:
        iret = 0

        connect, cursor =self.get_connect_cursor()

        brequery = True
        while True:  
            cursor.execute('show tables like \'db_update_log\'')
            list_data = cursor.fetchall()
            if not list_data:
                db_update_log = self.m_sql_dir + 'db_update_log.sql'
                iret = self.excel_file_sql(db_update_log)
                if brequery:
                    brequery = False
                    continue
                else: 
                    pass
 
            break

        self.free_connect_cursor(connect, cursor)
        return iret
    
    def _init_account(self) -> int:
        iret  = 0 
        self.excel_sql('UPDATE accounts SET loggedin = 0')
        self.excel_sql('UPDATE characters SET HasMerchant = 0') 
        return iret
    
    def _clear_nx_code_coupons(self, clear:int): 
        if not clear:
            return
        
        current_time = time.localtime()
        current_time = time.mktime(current_time) 
        current_time =  current_time - (14 * 24 * 60 * 60 * 1000)
        
        self.get_connect_cursor()

        cnx, cursor = self.get_connect_cursor()
        cursor.execute('SELECT id FROM nxcode WHERE expiration <= ?', current_time) 
        list_data = cursor.fetchall()
        if list_data: 
            pass
        
        self.free_connect_cursor(cnx, cursor)
        return