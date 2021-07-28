# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python20
# FileName:     python_lb.py
# Author:      liuyeyu
# Datetime:    2020/9/7 11:09
# Description:
#------------------------------------------------------------------------------------
import time
from time import sleep
from common.read_ini import ReadIni
from common.base import Base
from common.read_yaml_two import read_yaml_data
from selenium.common.exceptions import TimeoutException



class Loginpe(Base):
    readini = ReadIni()
    yamldata = read_yaml_data(ReadIni().get_yaml_path())
    def secceed_realname(self):
        """
        获取登录成功后的“新建”文字
        :return:
        """
        # sleep(2)
        # return self.text('x,/html/body/app-root/layout-basic/div/div[2]/div[1]/div[1]/div[1]/div[2]')
        return self.text(self.yamldata['DuanYan']['LOGINSECCEED'])
    def failed_login(self):
        """
        获取登录失败提示框文本
        :return:
        """
        try:

            # return self.text("x,/html/body/app-root/layout-passport/div/div[2]/div[2]/passport-login/div/div[2]/form/nz-form-item[2]/nz-form-control/div[2]/div")
            return self.text(self.yamldata['DuanYan']['LOGINFAILER1'])
        except TimeoutException:
            try:
                # return self.text("x,/html/body/app-root/layout-passport/div/div[2]/div[2]/passport-login/div/div[2]/form/nz-form-item[2]/nz-form-control/div[2]/div")
                return self.text(self.yamldata['DuanYan']['LOGINFAILER2'])
            except TimeoutException:
                # return self.text('x,/html/body/app-root/layout-passport/div/div[2]/div[2]/passport-login/div/div[2]/form/nz-form-item[1]/nz-form-control/div[2]/div')
                return self.text(self.yamldata['DuanYan']['LOGINFAILER3'])
    def failed_adduser(self):
        try:
            # return self.text("x,/html/body/app-root/layout-passport/div/div[2]/div[2]/passport-register/div/div[2]/form/nz-form-item[1]/nz-form-control/div[2]/div")
            return self.text(self.yamldata['DuanYan']['ADDUSERFAILER1'])
        except TimeoutException:
            try:
                # return self.text("x,/html/body/app-root/layout-passport/div/div[2]/div[2]/passport-register/div/div[2]/form/nz-form-item[2]/nz-form-control/div[2]/div")
                return self.text(self.yamldata['DuanYan']['ADDUSERFAILER2'])
            except TimeoutException:
                # return self.text("x,/html/body/app-root/layout-passport/div/div[2]/div[2]/passport-register/div/div[2]/form/nz-form-item[3]/nz-form-control/div[2]/div")
                return self.text(self.yamldata['DuanYan']['ADDUSERFAILER3'])
    def failed_reset(self):
        try:
            # return self.text("x,/html/body/app-root/layout-passport/div/div[2]/div[2]/app-reset-password/div/div[2]/form/nz-form-item[1]/nz-form-control/div[2]/div")
            return self.text(self.yamldata['DuanYan']['RELETPWDFAILER1'])
        except TimeoutException:
            try:
                # return self.text("x,/html/body/app-root/layout-passport/div/div[2]/div[2]/app-reset-password/div/div[2]/form/nz-form-item[2]/nz-form-control/div[2]/div")
                return self.text(self.yamldata['DuanYan']['RELETPWDFAILER2'])
            except TimeoutException:
                # return self.text("x,/html/body/app-root/layout-passport/div/div[2]/div[2]/app-reset-password/div/div[2]/form/nz-form-item[3]/nz-form-control/div[2]/div")
                return self.text(self.yamldata['DuanYan']['RELETPWDFAILER3'])





class LoginPage(Loginpe):
    readini = ReadIni()
    yamldata = read_yaml_data(ReadIni().get_yaml_path())
    path=readini.get_yaml_path()
    data=read_yaml_data(path)
    def adduser(self,addusername,adduseryanzheng,adduserpwd):
        '''
        注册
        :param addusername:
        :param adduseryanzheng:
        :param adduserpwd:
        :return:
        '''
        self.click(self.data['AddUser']['ADDUSER'])    # 点击免费注册
        self.send_keys(self.data['AddUser']['USERNAME'],addusername)   # 输入账号
        self.send_keys(self.data['AddUser']['YANZHENG'], adduseryanzheng)   # 输入验证码
        self.send_keys(self.data['AddUser']['PWD'], adduserpwd)    # 输入密码
        self.click(self.data['AddUser']['STARTADDUSER'])    # 点击注册
    def login_page(self,loginname,loginpwd):
        '''
        账号密码登录
        :param loginname:
        :param loginpwd:
        :return:
        '''
        self.send_keys(self.data['LoginPage']['USERNAME'], loginname)  # 输入账号
        self.send_keys(self.data['LoginPage']['PASSWORD'] ,loginpwd)  # 输入密码
        self.click(self.data['LoginPage']['LOGIN'])  # 点击登录
        sleep(2)
    def login_page2(self,loginname,loginpwd):
        '''
        手机号登录
        :param loginname:
        :param loginpwd:
        :return:
        '''
        self.click(self.data["LoginPage"]["PHONELOGIN"])
        self.send_keys(self.data['LoginPage']['PHONE'], loginname)  # 输入账号
        self.send_keys(self.data['LoginPage']['PHONEPWD'], loginpwd)  # 输入密码
        self.click(self.data['LoginPage']['PHONELOGING'])  # 点击登录

    def reset_page(self, resetname, resetyanzheng,resetpwd):
        '''
        重置密码
        :param resetname:
        :param resetyanzheng:
        :param resetpwd:
        :return:
        '''
        self.click(self.data['ReletPwd']['RELETPWD'])
        self.send_keys(self.data['ReletPwd']['PHONE'],resetname)
        self.send_keys(self.data['ReletPwd']['YANZHENG'], resetyanzheng)
        self.send_keys(self.data['ReletPwd']['PWD'], resetpwd)
        self.click(self.data['ReletPwd']['PELET'])
    def page_skip(self):
        '''
        页面跳转
        :return:
        '''
        self.click(self.data["PageSkip"]["PHONEYANZHENG"])
        self.click(self.data["PageSkip"]["PWDLOGIN"])
        self.click(self.data["PageSkip"]["SKIPRELET"])
        self.click(self.data["PageSkip"]["RELETLOGIN"])
        self.click(self.data["PageSkip"]["SKIPADDUSER"])
        self.click(self.data["PageSkip"]["SKIPLOGIN"])

if __name__=="__main__":
    loginpage=LoginPage('Chrome','http://fe-dev.xtect.site2e.cn/')
    loginpage.adduser("18731138350",'123456',"abcdefgh12345678")
    print(loginpage.failed_adduser())
    # time.sleep(3)
    loginpage.quit()
