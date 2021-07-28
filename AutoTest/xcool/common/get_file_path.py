# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python20
# FileName:     python_lb.py
# Author:      liuyeyu
# Datetime:    2020/9/7 11:09
# Description:
#------------------------------------------------------------------------------------

import os

def get_path(path):
    pro_name = path.split("/")[0]
     #获取文件绝对路径
    file_path=os.path.dirname(__file__)
    #分割路径
    fenge = file_path.split(pro_name)
    # print(fenge)
    #拼接路径
    all_path = str(fenge[0])+path
    return all_path
    # return os.path.join(fenge[0],path)

if __name__ == '__main__':
    print(get_path("proranzhi20/data_config/login_data_config.json"))