import os
import pytest
import time
from InterfaceTest.common.read_ini import ReadIni
readini =ReadIni()
case = readini.case_path()
temp = readini.temp_path()
report = readini.report_path()

if __name__ == '__main__':
    t = time.strftime('%Y_%m_%d_%H_%M_%S')
    pytest.main()
    # # # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', 'temp'])
    # # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report/allure%s.html'%t)