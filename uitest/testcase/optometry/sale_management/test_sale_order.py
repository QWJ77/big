#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from time import sleep

import pytest
from allure import MASTER_HELPER as helper
from selenium import webdriver

from pages.optometry.sale_management import sales_order_page
from pages import login_page


@helper.feature("视光运营")
@helper.story("销售订单")
class TestSaleorder():
    @helper.step("初始化启动浏览器")
    def setup_class(self):
        '''用例执行前，启动浏览器，创建chrome实例'''
        driver = webdriver.Chrome()
        driver.maximize_window()
        # 实例化页面
        self.lg = login_page.LoginPage(driver)
        self.sa = sales_order_page.SalesOrderPage(driver)

    @helper.step("关闭浏览器")
    def teardown_class(self):
        '''用例执行完毕，关闭浏览器'''
        self.lg.quit()

    @helper.testcase("测试选择优惠方案")
    def test_choose_discount(self):
        with helper.step("再开一单--选择优惠"):
            self.sa.choose_discount()
            time.sleep(2)

    @helper.testcase("测试更换处方")
    def test_bill_amount_wrong(self):
        with helper.step("再开一单--更换处方"):
            self.sa.replace_prescription()
            time.sleep(2)

    @helper.testcase("测试订单金额不允许为0")
    def test_bill_amount_wrong(self):
        with helper.step("再开一单--订单数量为0"):
            self.sa.replace_prescription()
            time.sleep(2)
            assert self.sa.get_text(self.op.amount_tip) == '订单总额不允许为0'


if __name__ == '__main__':
    pytest.main(['-s', 'test_sale_order.py'])
