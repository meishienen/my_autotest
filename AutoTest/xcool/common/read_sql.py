# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python20
# FileName:     python_lb.py
# Author:      liuyeyu
# Datetime:    2020/9/7 11:09
# Description:
#------------------------------------------------------------------------------------
#-*-coding:utf-8-*-

import psycopg2

# 通过connect方法创建数据库连接
conn = psycopg2.connect(dbname="xcool", user="xcool_dbuser", password="jk7cj=x9cv9sswa-q",
                        host="pgm-bp11809g9a85h74gko.pg.rds.aliyuncs.com", port="1921")
curs = conn.cursor()
def select_sql(username):

    select_sql = """select username from auth_user"""  # 查询语句
    curs.execute(select_sql)
    data = curs.fetchall()  # 获取数据
    print(data)
    # for i in data:
    #     # print(i)
    #     if i[0]== str(username):
    #         print("i与username一致","i=",i[0],"username=",username)
    #         delete_sql = """delete  from organ_employee where display_name=%s""" # 删除语句
    #         delete_sql2 = """delete from auth_user where username=%s""" # 删除语句
    #         params = (i[0],)
    #         curs.execute(delete_sql,params)  # 执行该sql语句
    #         curs.execute(delete_sql2,params)  # 执行该sql语句
    #         conn.commit() #提交事务
    #     else:
    #         print("i没有username一致的值","i=",i[0],"username=",str(username))

    # 关闭连接
    conn.close()

if __name__ == '__main__':

    print(select_sql(13355555555))