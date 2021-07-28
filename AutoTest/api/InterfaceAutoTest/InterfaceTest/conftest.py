# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   InterfaceAutoTest
# FileName:     conftest
# Author:      liuyeyu
# Datetime:    2020/10/17 15:45
# Description:
#------------------------------------------------------------------------------------
import pytest,os
#自定义一个固件
from InterfaceTest.common.read_excel import ReadExcel
from InterfaceTest.requst_method.request_method import RequestMethod


@pytest.fixture(scope="module")
def get_request_20():
    yield ReadExcel(),RequestMethod()

if __name__ == '__main__':
    print(get_request_20)