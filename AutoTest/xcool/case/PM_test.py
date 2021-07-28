import unittest

from pages.xcool_login import LoginPage
from common.read_yaml_two import read_yaml_data
from common.read_ini import ReadIni
class PMcaseTest(unittest.TestCase):
    yaml_data = read_yaml_data(ReadIni().get_yaml_path())
    @classmethod
    def setUpClass(self):
        loginpage = LoginPage(self.yaml_data['Browser']['BROWSER1'],self.yaml_data['Browser']['URL1'])
        loginpage.login_page("18731138350", 'liu123456')

    def tearDownClass(self):
        print("*"*50+"分割线"+"*"*50)
