#coding=utf-8
"""
@Time    : 2019/10/28
@Author  : qiwj
@Contact : qiwj@gratone.cn
@Software: PyCharm
@Desc    : 封装登录页面和一级菜单页面
"""
import time

from common.basePage import BasePage
from selenium import webdriver
from env_switch import constants


class LoginPage(BasePage):

    """试用环境"""
    url = constants.url

    # 登录系统
    account_input = ('id', 'account')
    password_input = ('id', 'password')
    login_button = ('xpath', '//*[@id="main"]/div/div/div[2]/div/div/form/div[2]/div/div/button')
    # 一级菜单
    outpati_service = ('xpath', "//li[contains(.,'门诊服务')]")
    outpati_doctor_station = ('xpath', "//li[contains(.,'门诊医生站')]")
    opto_operation = ('xpath', "//li[contains(.,'视光运营')]")

    def login(self,username=constants.username, pwd=constants.pwd):
        """登陆，账号：sqm，密码：aaaaaaa1"""
        self.get(self.url)
        self.sendKeys(self.account_input, text=username)
        self.sendKeys(self.password_input, text=pwd)
        self.click(self.login_button)
        self.maximize_window()

    def to_outpati_service(self):
        """进入门诊服务"""
        self.click(self.outpati_service)

    def to_outpati_doctor_station(self):
        """进入门诊医生站"""
        self.click(self.outpati_doctor_station)

    def to_opto_operation(self):
        """进入视光运营"""
        self.click(self.opto_operation)


if __name__ == '__main__':
    driver=webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.login()
    time.sleep(2)
    login_page.to_opto_operation()

