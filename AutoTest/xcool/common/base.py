# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python20
# FileName:     python_lb.py
# Author:      liuyeyu
# Datetime:    2020/9/7 11:09
# Description:
#------------------------------------------------------------------------------------
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from common.read_yaml_two import read_yaml_data
# from common.read_sql import real_sql


class Base:
    path2 = r'D:\ceshi\pythonAuto\xcool\data_config\yaml_config.yaml'
    data2 = read_yaml_data(path2)
    def __init__(self, browser,url):
        #选择浏览器
        if browser == 'Chrome':
            self.driver=webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver=webdriver.Ie()
        # 打开网址
        self.driver.get(url)
        # 窗口最大化
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(3)

    def imlicitly_wait(self,time):
        """
        隐式等待
        :param time:等待时间
        :return:
        """
        self.driver.implicitly_wait(time)
    def get_url(self,url):
        """
        获取url
        :param url:需要传入的URL地址
        :return:
        """
        self.driver.get(url)

    def maximize_window(self):
        """
        窗口最大化
        :return:
        """
        self.driver.maximize_window()
    def selector_to_locator(self,selector):
        """
        将selector：如id，account，转换成 locator 如（By.ID，‘account’）
        :param selector:
        :return:
        """
        selector_by=selector.split(',')[0].strip()
        selector_value=selector.split(',')[1].strip()
        if selector_by=='i' or selector_by =='id':
            locator = (By.ID,selector_value)
        elif selector_by=='n' or selector_by =='name':
            locator = (By.NAME,selector_value)
        elif selector_by == 't' or selector_by == 'tag_name':
            locator = (By.TAG_NAME, selector_value)
        elif selector_by == 's' or selector_by == 'css_selector':
            locator = (By.CSS_SELECTOR, selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            locator = (By.XPATH, selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            locator = (By.LINK_TEXT, selector_value)
        elif selector_by == 'p' or selector_by == 'partlal_link_text':
            locator = (By.PARTIAL_LINK_TEXT, selector_value)
        elif selector_by == 'c' or selector_by == 'class_name':
            locator = (By.CLASS_NAME, selector_value)
        else:
            print('请输入正确的定位方法')
        return locator
    def locator_element(self,selector):
        """
        定位元素
        :param selector: 将selector：如（id,account）转换成locator 如（By.ID,'account'）
        :param selector:
        :return:
        """
        locator=self.selector_to_locator(selector)
        # return self.driver.find_elements(*locator)
        return WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator))
    def send_keys(self,selector,txt):
        """
        输入内容
        :param selector:将selector：如（id,account）转换成locator 如（By.ID,'account'）
        :param txt:输入的内容
        :return:
        """
        ele=self.locator_element(selector)
        ele.clear()
        ele.send_keys(txt)

    def click(self,selector):
        """
        点击元素
        :param selector:将selector：如（id,account）转换成locator 如（By.ID,'account'）
        :param selector:
        :return:
        """
        self.locator_element(selector).click()
    def text(self,selector):
        return self.locator_element(selector).get_attribute("textContent")
    def switch_to_frame(self,selector):
        """
        进入iframe框架
        :param selector:iframe的 id 或者 name
        :return:
        """
        locator=self.selector_to_locator(selector)
        WebDriverWait(self.driver,15).until(EC.frame_to_be_available_and_switch_to_it(locator))
    def switch_go_frame(self):
        self.driver.switch_to.parent_frame()
    def select_by_value(self,selector,value):
        """
        使用value值随机选择部门
        :param selector:
        :param value:
        :return:
        """
        locator = self.selector_to_locator(selector)
        Select(self.driver.find_element(*locator)).select_by_value(value)
    def select_by_visible_text(self,selector,text):
        '''
        使用文本随机选择部门
        :param selector:
        :param text:
        :return:
        '''
        locator = self.selector_to_locator(selector)
        Select(self.driver.find_element(*locator)).select_by_visible_text(text)
    def select_by_index(self,selector,index):
        """
        使用索引定位
        :param selector:
        :param index:
        :return:
        """
        locator = self.selector_to_locator(selector)
        Select(self.driver.find_element(*locator)).select_by_index(index)
    def ele_option(self,selector1,selector2):
        '''
        二次定位随机选择角色
        :param selector1:
        :param selector2:
        :return:
        '''
        locator1 = self.selector_to_locator(selector1)
        locator2 = self.selector_to_locator(selector2)
        ele_dept=self.driver.find_element(*locator1).find_elements(*locator2)
        ele = random.choice(ele_dept)
        ele.click()
    def switch_to_alertyes(self):
        """
        点击alert框的确定
        :return:
        """
        self.driver.switch_to.alert.accept()  # 点击确定
    def switch_to_alertno(self):
        """
        点击alert框的取消
        :return:
        """
        self.driver.switch_to.alert.dismiss()#点击取消
    # def daunyan(self):
    #
    #     nameone = self.driver.find_element(By.CSS_SELECTOR,self.data2['BASE']['DUANYAN']).text
    #     real_name = real_sql(nameone)
    #     print('实际获取到的真实姓名是：%s,添加的时候的真实姓名是：%s' % (real_name, nameone))


    def quit(self):
        """
        杀进程
        :return:
        """
        self.driver.quit()
    def jietu(self,filename):
        """

        :param filename:
        :return:
        """
        self.driver.get_screenshot_as_file(filename)

