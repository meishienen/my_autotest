# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   jiekouzidonghua
# FileName:     read_ini
# Author:      liuyeyu
# Datetime:    2020/10/14 18:59
# Description:
#------------------------------------------------------------------------------------
from configparser import ConfigParser
import os



class ReadIni:
    path1 = os.path.dirname(os.getcwd())
    def __init__(self):
        #创建对象
        self.config=ConfigParser()
        #获取ini文件绝对路径
        path2="common\path.ini"
        self.fail_path=os.path.join(self.path1,path2)
        #打开读取ini文件
        with open(self.fail_path,encoding='utf-8') as fp:
            self.config.read_string(fp.read())

    #获取excel文件绝对路径
    def excel_path(self):
        #获取ini文件里excel的值
        path2= self.config.get("Path","excel")
        #拼接返回excel的绝对路径
        return os.path.join(self.path1,path2)

    #获取ini文件里Sheet的值
    def Sheet_path(self):
        #读取Sheet的值
        return self.config.get("Path","Sheet")

    #获取ini文件里params的路径
    def params_path(self):
        # 获取ini文件里params的值
        path2 = self.config.get("Path", "params")
        # 拼接返回params的绝对路径
        return os.path.join(self.path1, path2)

    # 获取ini文件里except的路径
    def except_path(self):
        # 获取ini文件里except的值
        path2 = self.config.get("Path", "except")
        # 拼接返回except的绝对路径
        return os.path.join(self.path1, path2)

    def report_path(self):
        path2 =self.config.get("Path","report")
        return os.path.join(self.path1,path2)

    def case_path(self):
        path2 = self.config.get("Path", "casepath")
        return os.path.join(self.path1, path2)

    def temp_path(self):
        path2 = self.config.get("Path", "temppath")
        return os.path.join(self.path1, path2)
    def log_path(self):
        path2 = self.config.get("Path", "logpath")
        return os.path.join(self.path1, path2)

if __name__ == '__main__':
    read=ReadIni()
    a=read.case_path()
    print(a)
