
#声明一个函数来获取所有用例的数据
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
class TestPyttest:
    #获取用例
    @pytest.mark.parametrize("id,method,url,precondition_id,expect,case_type,row",data_gat())
    def test_all(self,get_request_20,id,method,url,precondition_id,expect,case_type,row):
        #获取请求参数，有两种场景：有数据关联和没有数据关联两种。
        if precondition_id:
            params=get_request_20[1].get_updated_params(row)
        else:
            params=get_request_20[0].get_case_params_value(row)
        #指定用例，获取实际结果
        actual = get_request_20[1].get_status_code(method,url,params)
        #断言
        assert actual==200




if __name__ == '__main__':
    pytest.main()