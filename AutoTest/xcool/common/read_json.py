# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python20
# FileName:     python_lb.py
# Author:      liuyeyu
# Datetime:    2020/9/7 11:09
# Description:
#------------------------------------------------------------------------------------
import json


def read_json_data(jsonfile):
    with open(jsonfile,mode='r',encoding='utf8') as fp:
        return json.load(fp)


if __name__ == '__main__':
    print(read_json_data(r"D:\ceshi\pythonAuto\xcool\data_config\login_data_config.json"))