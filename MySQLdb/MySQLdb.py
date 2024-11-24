import os
import time

import mysql.connector
from mysql.connector import errorcode

class MySQLdb:
    def __init__(self, ip:str, user:str, password:str):
        self.m_ip = ip
        self.m_user = user
        self.m_password = password

        self.m_db:mysql.connector
        return
    
    def connect(self) -> int: 
        config = {
            'user': self.m_user
            , 'password': self.m_password
            , 'host': self.m_ip
            , 'charset': 'gbk'
        }

        iret = 0

        try:
            self.m_connect = mysql.connector.pooling.MySQLConnectionPool(
                pool_name = 'MapleStory'
                , pool_size = 5
                ,  **config)
        except mysql.connector.Error as err:
            iret = 1
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("提供的数据库账户或密码不正确!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("数据库不存在")
            else:
                print(err)
        return iret
     
    
    def excel_file_sql(self, sql_file:str, db_name:str = 'MapleStoryDB') -> int: 
        with open(sql_file, "rb") as f:
            sql = f.read()

        cnx, cursor = self.get_connect_cursor(db_name)
 
        for result in cursor.execute(sql, multi=True):
            result.fetchall() 

        self.free_connect_cursor(cnx, cursor)
        return
    

    def excel_sql(self, sql:str, db_name:str = 'MapleStoryDB') -> None:
        cnx = self.m_connect.get_connection()
        cursor = cnx.cursor() 

        if db_name is not None:
            cut_db = 'USE '+ db_name + ';'
            cursor.execute(cut_db)
            cnx.commit() 
        
        cursor.execute(sql) 
        cnx.commit()
        cursor.close()
        cnx.close()
        return
   
    def get_connect_cursor(self, db_name:str = 'MapleStoryDB'):
        cnx = self.m_connect.get_connection()
        cursor = cnx.cursor() 
        if db_name is not None:
            cut_db = 'USE '+ db_name + ';'
            cursor.execute(cut_db)
            cnx.commit() 
        return cnx, cursor
    
    def free_connect_cursor(self, cnx, cursor):
        cnx.commit()
        cursor.close()
        cnx.close()
        return