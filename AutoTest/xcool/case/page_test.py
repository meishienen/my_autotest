import time
import unittest


from parameterized import parameterized
from common.my_log import xcool_log
from common.read_ini import ReadIni
from common.read_json import read_json_data
from common.read_yaml_two import read_yaml_data
from pages.xcool_login import LoginPage



class LoginText(unittest.TestCase):
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
    def test_login_secceed(self):
        """
        这是页面跳转的用例
        :param username:
        :param pwd:
        :param qiwang:
        :param xuhao:
        :return:
        """
        try:
            self.logintext.page_skip()
            # 获取日志
            self.xcoollog.info('进行测试动作')
        except:
            t = time.strftime('%Y_%m_%d_%H_%M_%S')
            #获取日志
            self.xcoollog.error('跳转页面用例出错，具体查看'+ t + "截图")
            # 获取截图
            self.logintext.jietu(ReadIni().get_jietu_path()+r'\xcool_login_%s.png'%t)
            raise AssertionError('跳转页面用例出错，具体查看'+ t + "截图")
        finally:
            # time.sleep(3)
            # self.logintext.quit()
            pass
if __name__ == '__main__':
    unittest.main()