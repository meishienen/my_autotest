# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   jiekouzidonghua
# FileName:     demo_tiaoshi
# Author:      liuyeyu
# Datetime:    2020/10/16 22:00
# Description:
#------------------------------------------------------------------------------------
import pytest

from InterfaceTest.common.read_excel import ReadExcel
from InterfaceTest.common.send_email import SendEmail


def data_gat():
    read_excel = ReadExcel()
    # list1=[]
    # for row in range(2, excel.get_row_count() + 1):
    #     if excel.get_case_if_execute(row) == "Y":
    #         method = excel.get_case_method(row)
    #         url = excel.get_case_url(row)
    #         precondition_id = excel.get_case_precondition_id(row)
    #         case_type=excel.get_case_type(row)
    #         expect=excel.get_case_except_value(row)
    #         if_execute=excel.get_case_if_execute(row)
    #         list1.append((method,url,precondition_id,case_type,expect,if_execute))
    #     return list1
    return [(read_excel.get_case_id(row),read_excel.get_case_method(row), read_excel.get_case_url(row), read_excel.get_case_precondition_id(row),
                    read_excel.get_case_except_value(row),
                 read_excel.get_case_type(row),row)
                for row in range(2, read_excel.get_row_count() + 1)
                if read_excel.get_case_if_execute(row)=="Y"]


if __name__ == '__main__':
    print(data_gat())