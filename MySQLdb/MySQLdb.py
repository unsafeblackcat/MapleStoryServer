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
            , 'charset': 'utf8mb4'
            , 'collation': 'utf8mb4_general_ci'
        }

        iret = 0 
        try:  
            conn = mysql.connector.connect(
                host=self.m_ip
                , user=self.m_user
                , password=self.m_password)
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES LIKE \'beidou\'")
            result = cursor.fetchone() 
            if result:
                print('[MySQLdb]: 北斗数据库已存在.')
                pass
            else:
                cursor.execute("CREATE DATABASE beidou DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci")
                print('[MySQLdb]: 北斗数据库创建成功!')
                pass
            
            cursor.close()
            conn.close()

            self.m_connect = mysql.connector.pooling.MySQLConnectionPool(
                pool_name = 'beidou'
                , pool_size = 5
                ,  **config)
        except mysql.connector.Error as err:
            iret = 1
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("[MySQLdb]: 提供的数据库账户或密码不正确!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("[MySQLdb]: 数据库不存在")
            else:
                print(err)
        return iret
     
    
    def excel_file_sql(self, sql_file:str, db_name:str = 'beidou') -> int: 
        with open(sql_file, "rb") as f:
            sql = f.read()

        cnx, cursor = self.get_connect_cursor(db_name)
 
        for result in cursor.execute(sql, multi=True):
            result.fetchall() 

        self.free_connect_cursor(cnx, cursor)
        return
    

    def excel_sql(self, sql:str, db_name:str = 'beidou') -> None:
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
   
    def get_connect_cursor(self, db_name:str = 'beidou'):
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