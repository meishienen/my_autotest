# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   jiekouzidonghua
# FileName:     request_method
# Author:      liuyeyu
# Datetime:    2020/10/14 18:56
# Description:
#------------------------------------------------------------------------------------
import re
import requests
from InterfaceTest.common.read_excel import ReadExcel

class RequestMethod:
    def __init__(self):
        #实例化session
        self.session=requests.session()
        self.read_excel = ReadExcel()
        self.session.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})

    #封装一个支持get和post的请求方法
    def get_or_post(self,method,url,params):
        if method=="GET":
            return self.session.get(url,params=params,verify=False)
        elif method=="POST":
            return self.session.post(url,data=params,verify=False)
    #请求接口，获取响应对象
    def get_response(self,method,url,params):
        return self.get_or_post(method,url,params)

    #获取响应内容，可能是json也可能是xml
    def get_actual_result(self,method,url,row,params=None):
        response=self.get_response(method, url, params)
        type=self.read_excel.get_case_type(row)
        if type=="JSON":
            return response.json()
        elif type=="HTML":
            return response.text
    def get_status_code(self,method,url,params=None):
        response = self.get_response(method, url, params)
        return response.status_code


    #获取前置用例的行号
    def get_precondition_row(self,row):
        #读取前置用例的编号
        preconditon_id=self.read_excel.get_case_precondition_id(row)
        #遍历用例行数
        for row in range(2,self.read_excel.get_row_count()+1):
            #为用例编号设置变量
            case_id=self.read_excel.get_case_id(row)
            #如果用例编号等于前置用例编号，返回行号
            if case_id==preconditon_id:
                return row

    # 执行前置用例，从响应中提取结果
    def get_precondion_value(self, row):
        #为行号定义变量
        precondition_row = self.get_precondition_row(row)
        method = self.read_excel.get_case_method(precondition_row)
        url = self.read_excel.get_case_url(precondition_row)
        params = self.read_excel.get_case_params_value(precondition_row)
        pattern = self.read_excel.get_re(precondition_row)
        #请求前置用例
        actual = self.get_actual_result(method, url,row,params)
        #用正则表达式提取数据
        return re.findall(pattern, actual)[0]

    # 将提取的数据更新到请求参数中
    def get_updated_params(self, row):
        # 获取用例params(json文件中的value值)用例参数
        dict1 = self.read_excel.get_case_params_value(row)
        #获取依赖字段设为key值
        key = self.read_excel.get_case_depend_key(self.get_precondition_row(row))
        #获取正则表达式提取到的值设为value值
        value = self.get_precondion_value(row)
        #将key值与value值添加到zidainz
        dict1[key]=value
        return dict1


if __name__ == '__main__':
    request = RequestMethod()
    excel = ReadExcel()
    for row in range(2, excel.get_row_count() + 1):
        if excel.get_case_if_execute(row) == "Y":
            method = excel.get_case_method(row)
            url = excel.get_case_url(row)
            precondition_id = excel.get_case_precondition_id(row)
            if precondition_id:
                params = request.get_updated_params(row)
            else:
                params = excel.get_case_params_value(row)
            print(method, url, params)
            actual = request.get_status_code(method, url, params)
            print(actual)
    # request.get_actual_result("GET","https://www.daidu.com","4","")
