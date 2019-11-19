#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from time import sleep

import pytest
from allure import MASTER_HELPER as helper
from selenium import webdriver

from pages.optometry.sale_management import optometre_sales_page
from pages import login_page


@helper.feature("视光运营")
@helper.story("视光销售")
class TestOptometre():
    @helper.step("初始化启动浏览器")
    def setup_class(self):
        '''用例执行前，启动浏览器，创建chrome实例'''
        driver = webdriver.Chrome()
        driver.maximize_window()
        # 实例化页面
        self.lg = login_page.LoginPage(driver)
        self.op = optometre_sales_page.OptometreSalesPage(driver)

    @helper.step("关闭浏览器")
    def teardown_class(self):
        '''用例执行完毕，关闭浏览器'''
        self.lg.quit()

    @helper.testcase("新增验光记录")
    def test_add_optometry_record(self):
        with helper.step("新增验光记录"):
            self.lg.login()
            self.op.add_optometry_record()
            time.sleep(2)

    @helper.testcase("删除验光记录")
    def test_delete_optometry_record(self):
        with helper.step("删除验光记录"):
            self.op.delete_optometry_record()
            time.sleep(2)

    @helper.testcase("进行销售开单")
    def test_draw_a_bill(self):
        with helper.step("进入视光销售--查询用户"):
            self.op.query_users()
        with helper.step("销售开单"):
            self.op.draw_a_bill()
            time.sleep(1)



if __name__ == '__main__':
    pytest.main(['-s', 'test_optometre_sales.py'])
