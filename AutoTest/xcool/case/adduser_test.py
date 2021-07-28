import time
import unittest


from parameterized import parameterized
from common.my_log import xcool_log
from common.read_ini import ReadIni
from common.read_json import read_json_data
from common.read_sql import select_sql
from common.read_yaml_two import read_yaml_data
from pages.xcool_login import LoginPage





class AdduserText(unittest.TestCase):
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
        # self.addusertext = LoginPage('Chrome', 'http://fe-dev.xtect.site2e.cn/')
        self.addusertext = LoginPage(self.yaml_data['Browser']['BROWSER1'],self.yaml_data['Browser']['URL1'])
        print("*"*50+'分割线'+"*"*50)

    def tearDown(self):
        # 退出
        # time.sleep(3)
        self.addusertext.quit()
        print("*" * 50 + '分割线' + "*" * 50)
    @parameterized.expand(json_data['test_adduser_failed'])
    def test_login_failed(self,username,yanzheng,pwd,qiwang,xuhao):
        """
        这是注册失败的用例
        :param username:
        :param pwd:
        :param qiwang:
        :param xuhao:
        :return:
        """
        try:
            #调用注册方法
            self.addusertext.adduser(username,yanzheng,pwd)
            # 获取日志
            self.xcoollog.info('进行注册动作')
            print(123456)
            #取注册失败后文字
            realname=self.addusertext.failed_adduser()
            print(789)
            #断言
            self.assertEqual(realname,qiwang,'实际结果与预期结果不一致')
        except:
            #获取日志
            self.xcoollog.error('注册失败用例，第%s条出错'%xuhao)
            # 获取截图
            t = time.strftime('%Y_%m_%d_%H_%M_%S')
            self.addusertext.jietu(ReadIni().get_jietu_path()+r'\xcool_login_%s.png'%t)
            raise AssertionError('注册失败用例，第%s条出错'%xuhao)
        finally:
            pass
            # select_sql(username)




if __name__=="__main__":
    unittest.main()
