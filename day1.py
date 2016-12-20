#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

class Mysql:
    def __init__(self,host,hostname,passwd,database):
        self.host = host
        self.hostname = hostname
        self.passwd = passwd
        self.database = database
    def lianjie(self):
         db = MySQLdb.connect(self.host,self.hostname,self.passwd,self.database)
         cursor = db.cursor()
         cursor.execute("SELECT VERSION()")
         data = cursor.fetchone()
         print data
         db.close()
    def createtable(self):
        db = MySQLdb.connect(self.host, self.hostname, self.passwd, self.database)
        cursor = db.cursor()
        #self.dataname =  dataname
        #self.databasename = databasename
        sql = """CREATE TABLE USEINFO (
                 USENAME  CHAR(20) NOT NULL,
                 PASSWD  CHAR(20))"""

        cursor.execute(sql)
        db.close()
    def createdatabase(self, dataname):
        db = MySQLdb.connect(self.host, self.hostname, self.passwd, self.database)
        cursor = db.cursor()
        self.dataname = dataname
        cursor.execute("CREATE DATABASE " + self.dataname)
    def insertdata(self):
         db = MySQLdb.connect(self.host, self.hostname, self.passwd, self.database)
         cursor = db.cursor()
         sql = """INSERT INTO EMPLOYEE(uaername,
                  password)
                  VALUES ('usename', 'passwd')"""
         try:
            cursor.execute(sql)
            db.commit()
         except:
             db.rollback()
         db.close()
    def query(self):
        db = MySQLdb.connect(self.host, self.hostname, self.passwd, self.database)
        cursor = db.cursor()
        sql = "SELECT * FROM user "
        try:
            # 执行SQL语句
            cursor.execute("use mysql")
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for i  in results:
                a =  i [1]
                b =  i [2]
                return (a,b)

        except:
            print "Error: unable to fecth data"

        # 关闭数据库连接
        db.close()



ip = Mysql("10.16.70.101","root","111111","TESTDB")
#ip.createdatabase("userinfo")
#ip.createtable()
a = ip.query()
myDict = dict.fromkeys(a[:1],a[1])
print myDict
print myDict.get('root')