# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python20
# FileName:     python_lb.py
# Author:      liuyeyu
# Datetime:    2020/9/7 11:09
# Description:
#------------------------------------------------------------------------------------
import yaml
from common.read_ini import ReadIni


def read_yaml_data(file):
    # print(ReadIni().get_yaml_path())
    with open(file,mode='r',encoding='utf8') as yaml_file:
        return yaml.safe_load(yaml_file)
    # print(open(ReadIni().get_yaml_path(), mode='r', encoding='utf8'))


if __name__ == '__main__':
    a=read_yaml_data(ReadIni().get_yaml_path())



