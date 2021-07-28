# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   jiekouzidonghua
# FileName:     read_json
# Author:      liuyeyu
# Datetime:    2020/10/14 18:57
# Description:
#------------------------------------------------------------------------------------
import json

def read_json(fail_path):
    #打开json文件
    with open(fail_path,encoding="utf8") as fp:
        return json.loads(fp.read())

if __name__ == '__main__':
    a=r'C:\Users\Administrator\PycharmProjects\jiekouzidonghua\InterfaceTest\data\except.json'
    print(read_json(a))

