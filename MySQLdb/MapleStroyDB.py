import time
import re

from MySQLdb.MySQLdb import *
from Config.ConfigGame import *
from pathlib import Path
from mysql.connector import (
    Error,
    InterfaceError,
    DatabaseError,
    OperationalError,
    IntegrityError
)


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
   
 
            break
            pass # while True:

        return iret
     
    def _init_db(self) -> int:
        iret = 0
        
        sql_history = "sql_history.txt"
    
        sql_list = list() 
        for p in Path(self.m_sql_dir).iterdir():
            if os.path.basename(p) == sql_history:
                pass
            else:
                sql_list.append(p)
            pass
        sql_list = sorted(sql_list, key=lambda f: tuple(map(int, re.search(r'V(\d+\.\d+\.\d+)', str(f)).group(1).split('.'))))
  
        if Path(self.m_sql_dir + sql_history).is_file():

            sql_file = str()
            with open(self.m_sql_dir + sql_history, "r", encoding="utf-8") as f:
                sql_file = f.read()

            sql_list_new = list()

            updata:int = 0
            for it in sql_list:
                if os.path.basename(it) == sql_file:
                    updata = 1
                    continue

                if updata: 
                    sql_list_new.append(it)

                pass

            sql_list = sql_list_new 
            pass
        else:
            pass

        sql_count = len(sql_list)
        if sql_count:  
            print(f"[数据库] 新的脚本: " + sql_count)

            tail_sql:str = str()
            for it in sql_list: 
                
                try: 
                    print(f"[数据库] 执行新的sql脚本: {it}")
                    self.excel_file_sql(it)  
                except InterfaceError as e:
                    print(f"[数据库] 接口错误: {e}")
                except OperationalError as e:
                    print(f"[数据库] 操作错误: {e}")
                except IntegrityError as e:
                    print(f"[数据库] 完整性错误: {e}")
                except Error as e:
                    print(f"[数据库] 数据库错误: {e}")
                except Exception as e:
                    print(f"[数据库] 其他错误: {e}")
                
                tail_sql = os.path.basename(it)
                pass
    
            with open(self.m_sql_dir + sql_history, "w", encoding="utf-8") as f:
                f.write(tail_sql)

            pass

        return iret