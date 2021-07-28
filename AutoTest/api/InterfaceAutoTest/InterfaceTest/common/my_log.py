# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python20
# FileName:     python_lb.py
# Author:      liuyeyu
# Datetime:    2020/9/7 11:09
# Description:
#------------------------------------------------------------------------------------
import logging
import sys


def xcool_log(log_path):
    #创建对象
    log_opj=logging.Logger("InterfaceAutoTest")
    #设置日志等级
    log_opj.setLevel(logging.DEBUG)
    #定义日志格式
    formatter_opj=logging.Formatter('[%(asctime)s][%(levelname)s][%(filename)s]:%(message)s')
    #设置日志名字（）路径
    fillename=log_path
    #把日志保存到本地
    #创建FileHandler对象
    fh=logging.FileHandler(fillename,encoding='utf8')
    #调用Handler对象，传入日志格式
    fh.setFormatter(formatter_opj)
    #把日志对象中添加到Handler对象
    log_opj.addHandler(fh)

    #把日志打印到控制台
    sh = logging.StreamHandler(sys.stdout)
    #传入格式
    sh.setFormatter(formatter_opj)
    # 把日志对象中添加到Handler对象
    log_opj.addHandler(sh)
    return log_opj































