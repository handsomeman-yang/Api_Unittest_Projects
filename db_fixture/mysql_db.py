#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting
from pymysql import connect,cursors
from pymysql.err import OperationalError
import configparser as cparser
import logging

# --------- 读取config.ini配置文件 ---------------
cf = cparser.ConfigParser()
cf.read(setting.TEST_CONFIG,encoding='UTF-8')
host = cf.get("mysqlconf","host")
port = cf.get("mysqlconf","port")
user = cf.get("mysqlconf","user")
password = cf.get("mysqlconf","password")
db = cf.get("mysqlconf","db_name")

class DB:
    """
    MySQL基本操作
    """
    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(host = host,
                                user = user,
                                password = password,
                                db = db,
                                charset = 'utf8mb4',
                                cursorclass = cursors.DictCursor
                                )
        except OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0],e.args[1]))

   # # 执行封装好的sql
   #  def find(self,real_sql):
   #      try:
   #          with self.conn.cursor() as cursor:
   #              cursor.execute(real_sql)
   #
   #      except:
   #          logging.log(logging.WARNING, "This is a warning log.")
   #          logging.log(logging.ERROR, "This is a error log.")
   #
   # # 清除表数据
   #  def clear(self,table_name):
   #      real_sql = "delete from " + table_name + ";"
   #      with self.conn.cursor() as cursor:
   #           # 取消表的外键约束
   #          cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
   #          cursor.execute(real_sql)
   #      self.conn.commit()
   #
   #  # 插入表数据
   #  def insert(self, table_name, table_data):
   #      for key in table_data:
   #          table_data[key] = "'"+str(table_data[key])+"'"
   #      key = ','.join(table_data.keys())
   #      value = ','.join(table_data.values())
   #      real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
   #
   #      with self.conn.cursor() as cursor:
   #          cursor.execute(real_sql)
   #      self.conn.commit()

    # 关闭数据库
    def close(self):
        self.conn.close()

    def select(self,sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                fc = cursor.fetchall()
                return fc
        except:
            logging.log(logging.WARNING, "This is a warning log.")
            logging.log(logging.ERROR, "This is a error log.")

    def update(self,sql):
        try:
            with self.conn.cursor() as cursor:
                count = cursor.execute(sql)
                return count
        except:
            print('更新失败')


if __name__ == "__main__":
    db = DB()

    def get():
        sql = "select * from sme_company where client_code like 'ecotest%%'"
        fc = db.select(sql)
        for row in fc:
            print(row["chinese"])

    get()

    # def ins():
    #     sql = "insert into pythontest values(5,'数据结构','this is a big book',now())"
    #     count = db.update(sql)


    #
    # def insparam():
    #     sql = "insert into pythontest values(%s,%s,%s,now())"
    #     params = (6, 'C#', 'good book')
    #     count = db.updateByParam(sql, params)

    # def delop():
    #     sql = "delete from pythontest where pid=4"
    #     count = db.update(sql)
    #     print
    #     "the：" + str(count)
    #

    # def change():
    #     sql = "update pythontest set pcontent='c# is a good book' where pid=6"
    #     count = db.update(sql)

