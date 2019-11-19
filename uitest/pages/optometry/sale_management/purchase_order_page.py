"""
@Time    : 2019/11/13
@Author  : qiwj
@Contact : qiwj@gratone.cn
@Software: PyCharm
@Desc    : 申购单页面类
"""


from common import basePage
from selenium import webdriver
import time

from pages import login_page
from selenium.webdriver.common.keys import Keys

class PurchaseOrderPage(basePage.BasePage):
    """
    申购单相关元素
    """
    add_purchase_button = ('xpath', '//button[contains(.,"新增申请单")]')
    choose_goods = ('xpath', '//button[contains(.,"选择商品")]')
