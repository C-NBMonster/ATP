# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: mysql.py
@time: 2019/3/21 14:49
@desc: 
"""

import pymysql.cursors

mysql_info = {"host": 'localhost',
              "port": 3306,
              "user": 'root',
              "passwd": 'cjx123456',
              "db": 'atp',
              "charset": 'utf8'}

class conn_mysql():
    '''
    mysql数据库相关操作
    连接数据库信息：mysql_info
    创建游标：mysql_execute
    查询某个字段对应的字符串：mysql_getstring
    查询一组数据：mysql_getrows
    关闭mysql连接：mysql_close
    '''
    def __init__(self,mysql_info=mysql_info):
        self.db_info = mysql_info
        u'''连接池方式'''
        self.conn = conn_mysql.__getConnect(self.db_info)

    @staticmethod
    def __getConnect(db_info):
        '''静态方法，从连接池中取出连接'''
        try:
            conn = pymysql.connect(host=db_info['host'],
                                   port=db_info['port'],
                                   user=db_info['user'],
                                   passwd=db_info['passwd'],
                                   db=db_info['db'],
                                   charset=db_info['charset'])
            return conn
        except Exception as a:
            print("数据库连接异常：%s"%a)

    def mysql_execute(self, sql):
        '''执行sql语句'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            self.conn.rollback()         # sql执行异常后回滚
            print("执行SQL语句出现异常：%s"%a)
        else:
            cur.close()
            self.conn.commit()          # sql无异常时提交

    def mysql_getrows(self, sql):
        ''' 返回查询结果'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            print("执行SQL语句出现异常：%s"%a)
        else:
            rows = cur.fetchall()
            cur.close()
            return rows

    # 查询数据
    def Search(self, sql, data=''):
        """
        插入数据
        :param sql: SQL语句
        :param data: 插入字段的值，根据表字段顺序填写。设定空值是为了解放sql，不受固定形式限制
        :usage:
        sql = "SELECT name,saving FROM trade WHERE account = '%s' "
        data = ('13512345678')
        :return:
        """
        cursor = self.conn.cursor()
        if data == '':
            cursor.execute(sql)
        else:
            cursor.execute(sql % data)
        for row in cursor.fetchall():
            print("Name:%s\tSaving:%.2f" % row)
        print('共查找出:', cursor.rowcount, '条数据')
        return cursor.fetchall()

    def mysql_getstring(self, sql):
        '''查询某个字段的对应值'''
        rows = self.mysql_getrows(sql)
        if rows != None:
            for row in rows:
                for i in row:
                    return i

    def mysql_Update(self, sql, data=''):
        """
        插入数据
        :param sql: SQL语句
        :param data: 插入字段的值，根据表字段顺序填写。设定空值是为了解放sql，不受固定形式限制
        :usage:
        sql = "UPDATE trade SET saving = '%.2f' WHERE account = '%s' "
        data = (8888, '13512345678')
        :return:
        """
        cur = self.conn.cursor()
        if data == '':
            cur.execute(sql)
        else:
            cur.execute(sql % data)
            self.conn.commit()
        self.conn.commit()
        print('成功修改 %s 条数据' % cur.rowcount)

    def mysql_close(self):
        ''' 关闭 close mysql'''
        try:
            self.conn.close()
        except Exception as a:
            print("数据库关闭时异常：%s"%a)





# MySQLdb.connect()     建立数据库连接
# cur = conn.cursor()    #通过获取到的数据库连接conn下的cursor()方法来创建游标。
# cur.execute()    #过游标cur 操作execute()方法可以写入纯sql语句。通过execute()方法中写如sql语句来对数据进行操作。
# cur.close()     # cur.close() 关闭游标
# conn.commit()   # conn.commit()方法在提交事物，在向数据库插入(或update)一条数据时必须要有这个方法，否则数据不会被真正的插入。
# conn.rollback() # 发生错误时候回滚
# conn.close()     # Conn.close()关闭数据库连接

if __name__ == "__main__":
    A = conn_mysql()
    # sql = "SELECT  *FROM notify_request t where TEMPLATE_ID LIKE '16091%' ORDER BY t.REQUEST_TIME DESC  limit 0,1"
    ud=9527
    sql = "select * from app_project_base_machineinfo where uid='%s'" % ud
    #A.Search(sql)
    print(A.mysql_getrows(sql))
    A.mysql_close()

