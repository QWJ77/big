"""
@Time    : 2019/10/28
@Author  : qiwj
@Contact : qiwj@gratone.cn
@Software: PyCharm
@Desc    : 封装视门诊服务公共方法（二级、三级菜单）
"""


from common import basePage
from selenium import webdriver
import time

from pages import login_page
from selenium.webdriver.common.keys import Keys




class OutpatientServicePublicPage(basePage.BasePage):
    """
    门诊服务页二级菜单
    """
    home_page = ('xpath', "//li[contains(.,'首页')]")
    registered_service = ('xpath', "//li[contains(.,'挂号服务')]")
    triage = ('xpath', "//li[contains(.,'分诊')]")
    outpatient_preview = ('xpath', "//li[contains(.,'门诊预检')]")
    check_registration = ('xpath', "//li[contains(.,'检查登记')]")
    workforce_management = ('xpath', "//li[contains(.,'排班管理')]")
    case_history_print = ('xpath', "//li[contains(.,'病历打印')]")
    cost_management = ('xpath', "//li[contains(.,'费用管理')]")
    outpatient_pharmacy = ('xpath', "//li[contains(.,'门诊药房')]")
    drug_administration = ('xpath', "//li[contains(.,'药品管理')]")
    visual_training = ('xpath', "//li[contains(.,'视觉训练')]")
    report_collection = ('xpath', "//li[contains(.,'报告采集')]")
    bill_management = ('xpath', "//li[contains(.,'票据管理')]")
    decision_management = ('xpath', "//li[contains(.,'决策管理')]")
    queue_number = ('xpath', "//li[contains(.,'排队叫号')]")


    """
    进入二级菜单的方法
    """

    def to_home_page(self):
        """进入首页"""
        login = login_page.LoginPage(self.driver)
        login.to_outpati_service()
        self.click(self.home_page)

    def to_registered_service(self):
        """进入挂号服务"""
        login = login_page.LoginPage(self.driver)
        login.to_outpati_service()
        self.click(self.registered_service)

    def to_triage(self):
        """进入分诊"""
        login = login_page.LoginPage(self.driver)
        login.to_outpati_service()
        self.click(self.triage)

    def to_outpatient_preview(self):
        """进入门诊预检"""
        login = login_page.LoginPage(self.driver)
        login.to_outpati_service()
        self.click(self.outpatient_preview)

    def to_check_registration(self):
        """进入检查登记"""
        login = login_page.LoginPage(self.driver)
        login.to_outpati_service()
        self.click(self.check_registration)

    def to_case_history_print(self):
        """进入病历打印"""
        login.to_outpati_service()
        self.click(self.case_history_print)

    def to_cost_management(self):
        """进入费用管理"""
        login.to_outpati_service()
        self.click(self.cost_management)

    def to_outpatient_pharmacy(self):
        """进入门诊药房"""
        login.to_outpati_service()
        self.click(self.outpatient_pharmacy)

    def to_drug_administration(self):
        """进入药品管理"""
        login.to_outpati_service()
        self.click(self.drug_administration)

    def to_visual_training(self):
        """进入视觉训练"""
        login.to_outpati_service()
        self.click(self.visual_training)

    def to_report_collection(self):
        """进入报告采集"""
        login.to_outpati_service()
        self.click(self.report_collection)

    def to_bill_managementg(self):
        """进入票据管理"""
        login.to_outpati_service()
        self.click(self.bill_management)

    def to_decision_management(self):
        """进入决策管理"""
        login.to_outpati_service()
        self.click(self.decision_management)

    def to_queue_number(self):
        """进入排队叫号"""
        login.to_outpati_service()
        self.click(self.queue_number)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    login = login_page.LoginPage(driver)
    login.login()
    out =OutpatientServicePublicPage(driver)
    out.to_registered_service()
    out.to_queue_number()

