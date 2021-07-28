# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python20
# FileName:     python_lb.py
# Author:      liuyeyu
# Datetime:    2020/9/7 11:09
# Description:
#------------------------------------------------------------------------------------
import configparser
import os

from common.get_file_path import get_path




class ReadIni:
    def __init__(self):
        # path = r"C:\ronghua\TestTools\pycharm\pro_ranzhi_20\data_config\file_path.ini"
        # 创建对象
        self.config = configparser.ConfigParser()
        #调用get_path()函数，获取到项目的绝对路径
        self.before_path = get_path("xcool")
        # 获取到file_path.ini文件的路径,读取内部数据
        self.config.read(self.before_path+r'\data_config\file_path.ini',encoding='utf8')


    def get_yaml_path(self):
        #读取ini配置文件中配置的路径
        path = self.config.get('path', 'yamllogindatapath')
        #路径拼接
        return os.path.join(self.before_path,path)

    def get_json_path(self):
        path = self.config.get('path', 'jsonlogindatapath')
        return os.path.join( self.before_path,path)

    def get_excel_path(self):
        path = self.config.get('path', 'excellogindatapath')
        return os.path.join( self.before_path,path)
    def get_jietu_path(self):
        path = self.config.get('path', 'jietulogindatapath')
        return os.path.join( self.before_path,path)
    def get_log_path(self):
        path = self.config.get('path', 'logpath')
        return os.path.join( self.before_path,path)
    def get_case_path(self):
        path = self.config.get('path', 'casepath')
        return os.path.join( self.before_path,path)
    def get_report_path(self):
        path = self.config.get('path', 'reportpath')
        return os.path.join( self.before_path,path)
    def get_useryaml_path(self):
        path = self.config.get('path', 'yamladduserdatapath')
        return os.path.join( self.before_path,path)
    def get_documentjson_path(self):
        path = self.config.get('path', 'jsondocumentdatapath')
        return os.path.join( self.before_path,path)
if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_yaml_path())
