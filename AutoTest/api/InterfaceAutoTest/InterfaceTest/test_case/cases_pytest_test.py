
#声明一个函数来获取所有用例的数据
import time

import pytest

from InterfaceTest.common.my_log import xcool_log
from InterfaceTest.common.read_excel import ReadExcel
from InterfaceTest.common.read_ini import ReadIni
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
class TestPyttest:
    #获取日志路径
    tt = time.strftime('%Y_%m_%d_%H_%M_%S')
    xcoollog = xcool_log(ReadIni().log_path() + r'\log%s.log'%tt)
    try:
        #获取用例
        @pytest.mark.parametrize("id,method,url,precondition_id,expect,case_type,row",data_gat())
        def test_all(self,get_request_20,id,method,url,precondition_id,expect,case_type,row):
            #获取请求参数，有两种场景：有数据关联和没有数据关联两种。
            if precondition_id:
                params=get_request_20[1].get_updated_params(row)
            else:
                params=get_request_20[0].get_case_params_value(row)
            #指定用例，获取实际结果
            actual = get_request_20[1].get_actual_result(method, url,row,params)
            actual2 = get_request_20[1].get_status_code(method, url,params)

            #断言
            if expect:
                if case_type=="JSON":
                    assert actual==expect and actual2==200
                elif case_type=="HTML":
                    assert expect in actual and actual2==200
    except:
        # 获取日志
        xcoollog.error('接口测试用例，%s条出错' % id)




if __name__ == '__main__':
    pytest.main()
