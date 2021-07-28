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


from parameterized import parameterized
from common.my_log import xcool_log
from common.read_ini import ReadIni
from common.read_json import read_json_data
from common.read_yaml_two import read_yaml_data
from pages.xcool_login import LoginPage
from selenium.common.exceptions import NoSuchElementException



class LoginText(unittest.TestCase):
    # file_data1 = read_excel_data(ReadIni().get_excel_path(),'succeed')
    # file_data2 = read_excel_data(ReadIni().get_excel_path(),'filled')
    yaml_data = read_yaml_data(ReadIni().get_yaml_path())
    json_data = read_json_data(ReadIni().get_json_path())
    #获取日志路径
    tt = time.strftime('%Y_%m_%d_%H_%M_%S')
    xcoollog = xcool_log(ReadIni().get_log_path() + r'\log%s.log'%tt)
    # @classmethod
    # def setUpClass(self):
    #     #实例化动作类
    #     self.logintext = LoginPage('Chrome', 'http://127.0.0.1/ranzhi/sys/user-login.html')
    # @classmethod
    # def tearDownClass(self):
    #     # 退出
    #     self.logintext.quit()
    #
    def setUp(self):
        #实例化动作类
        self.logintext = LoginPage(self.yaml_data['Browser']['BROWSER1'],self.yaml_data['Browser']['URL1'])
        print("*"*50+'分割线'+"*"*50)
    def tearDown(self):
        # 退出
        time.sleep(3)
        self.logintext.quit()
        print("*" * 50 + '分割线' + "*" * 50)
    @parameterized.expand(json_data['test_login_succeed'])
    # @parameterized.expand(yaml_data['test_longin_succeed'])
    # @parameterized.expand(file_data1)
    def test_login_secceed(self,username,pwd,qiwang,xuhao):
        """
        这是登录成功的用例
        :param username:
        :param pwd:
        :param qiwang:
        :param xuhao:
        :return:
        """
        try:
            #调用登录方法
            self.logintext.login_page(username,pwd)
            # 获取日志
            self.xcoollog.info('进行登录动作')
            #取登陆成功后首页的“新建”
            realname=self.logintext.secceed_realname()
            #断言
            self.assertEqual(realname,qiwang,'实际结果与预期结果不一致')
        except:
            #获取日志
            self.xcoollog.error('登陆成功用例，第%s条出错'%xuhao)
            # 获取截图
            t = time.strftime('%Y_%m_%d_%H_%M_%S')
            self.logintext.jietu(ReadIni().get_jietu_path()+r'\xcool_login_%s.png'%t)
            raise AssertionError('登录成功用例，第%s条出错'%xuhao)
        finally:
            # time.sleep(3)
            # self.logintext.quit()
            pass
    @parameterized.expand(json_data['test_login_failed'])
    def test_login_failde(self,username,pwd,qiwang,xuhao):
        """
        这是登录失败的用例
        :param username:
        :param pwd:
        :param qiwang:
        :param xuhao:
        :return:
        """
        try:

            #调用登录方法
            self.logintext.login_page(username,pwd,)
            #获取日志
            self.xcoollog.info('进行登录动作')
            #定义获取的登录失败文本
            faillog=self.logintext.failed_login()
            #断言
            self.assertEqual(faillog,qiwang,'实际结果与预期结果不一致')
        except:
            # 获取日志
            self.xcoollog.error('登录失败用例，第%s条出错'%xuhao)
            # 获取截图
            t = time.strftime('%Y_%m_%d_%H_%M_%S')
            self.logintext.jietu(ReadIni().get_jietu_path()+r'\ranzhi_login_%s.png'%t)
            raise AssertionError('登录失败用例，第%s条出错'%xuhao)

        finally:
            pass
            # # time.sleep(3)
            # self.logintext.quit()
    @parameterized.expand(json_data['test_login_fild2'])
    def test_login_failde2(self,username,pwd,qiwang,xuhao):
        """
        这是登录失败的用例
        :param username:
        :param pwd:
        :param qiwang:
        :param xuhao:
        :return:
        """
        try:

            #调用登录方法
            self.logintext.login_page2(username,pwd,)
            #获取日志
            self.xcoollog.info('进行登录动作')
            #定义获取的登录失败文本
            faillog=self.logintext.failed_login()
            #断言
            self.assertEqual(faillog,qiwang,'实际结果与预期结果不一致')
        except:
            # 获取日志
            self.xcoollog.error('登录失败用例，第%s条出错'%xuhao)
            # 获取截图
            t = time.strftime('%Y_%m_%d_%H_%M_%S')
            self.logintext.jietu(ReadIni().get_jietu_path()+r'\ranzhi_login_%s.png'%t)
            raise AssertionError('登录失败用例，第%s条出错'%xuhao)

        finally:
            pass
            # # time.sleep(3)
            # self.logintext.quit()

    @parameterized.expand(json_data['test_reset_pwd'])
    def test_reset_pwd(self,username,yanzheng,pwd,qiwang,xuhao):
        """
        这是登录失败的用例
        :param username:
        :param pwd:
        :param qiwang:
        :param xuhao:
        :return:
        """
        try:

            #调用登录方法
            self.logintext.reset_page(username,yanzheng,pwd,)
            #获取日志
            self.xcoollog.info('进行重置动作')
            #定义获取的登录失败文本
            faillog=self.logintext.failed_reset()
            #断言
            self.assertEqual(faillog,qiwang,'实际结果与预期结果不一致')
        except:
            # 获取日志
            self.xcoollog.error('第%s条用例出错'%xuhao)
            # 获取截图
            t = time.strftime('%Y_%m_%d_%H_%M_%S')
            self.logintext.jietu(ReadIni().get_jietu_path()+r'\xcool_login_%s.png'%t)
            raise AssertionError('第%s条用例出错'%xuhao)

        finally:
            pass
            # # time.sleep(3)
            # self.logintext.quit()



if __name__ == '__main__':
    unittest.main()