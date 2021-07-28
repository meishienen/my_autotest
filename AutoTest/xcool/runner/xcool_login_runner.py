# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python20
# FileName:     python_lb.py
# Author:      liuyeyu
# Datetime:    2020/9/7 11:09
# Description:
#------------------------------------------------------------------------------------
import time
import unittest

from unittestreport import TestRunner

from common.read_ini import ReadIni
from common.send_email import SendEmail


class TestRunner1:
    def tset_xcool(self):
        #创建测试套
        suite=unittest.TestSuite()

        #通过addtest来添加用例，用TestLoader来加载用例，用discover找到用例，用pattern来匹配用例
        case_path = ReadIni().get_case_path()
        suite.addTest(unittest.TestLoader().discover(case_path,pattern='*t.py'))
        # #单个测试用例
        # suite.addTest()
        # #第二种方法
        #
        # #第三种方法
        # suite= unittest.defaultTestLoader.loadTestsFromTestCase()
        #创建报告，格式是html
        t = time.strftime('%Y_%m_%d_%H_%M_%S')
        report_path = ReadIni().get_report_path()+r'\report_%s.html'%t
        #wb表示以二进制导入
        report_file = open(report_path,mode='wb')
        ##第一种
        # test_runner=HTMLTestRunner(report_file,title='然之测试报告',description='下面是然之报告详情',
        #                tester='李四')
        # # 第二种
        test_runner = TestRunner(suite, filename=report_path, report_dir=report_path,
                                 title="xcool测试报告", tester="刘业宇", templates=1,
                                 desc="这是xcool的详细测试报告")
        #运行测试套
        test_runner.run()
        #关闭文件
        report_file.close()
        #发送邮件
        SendEmail().send_emali(report_path)

if __name__ == '__main__':
    TestRunner1().tset_xcool()
