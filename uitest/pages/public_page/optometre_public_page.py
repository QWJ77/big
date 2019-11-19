"""
@Time    : 2019/10/28
@Author  : qiwj
@Contact : qiwj@gratone.cn
@Software: PyCharm
@Desc    : 封装视光运营公共方法（二级、三级菜单）
"""


from common import basePage
from selenium import webdriver
import time

from pages import login_page
from selenium.webdriver.common.keys import Keys




class OptometrePublicPage(basePage.BasePage):
    """
    视光销售页二级菜单
    """
    sale_manage = ('xpath', '//*[@id="main"]/div/div[2]/div[1]/div[1]/ul/li[1]')
    after_sale_manage = ('xpath', '//*[@id="main"]/div/div[2]/div[1]/div[1]/ul/li[2]')
    price_manage = ('xpath', '//*[@id="main"]/div/div[2]/div[1]/div[1]/ul/li[3]')
    inventory_manage = ('xpath', '//*[@id="main"]/div/div[2]/div[1]/div[1]/ul/li[4]')
    purchase_manage = ('xpath', '//*[@id="main"]/div/div[2]/div[1]/div[1]/ul/li[5]')
    process_manage = ('xpath', '//*[@id="main"]/div/div[2]/div[1]/div[1]/ul/li[6]')
    chain_manage = ('xpath', '//*[@id="main"]/div/div[2]/div[1]/div[1]/ul/li[7]')
    chain_process = ('xpath', '//*[@id="main"]/div/div[2]/div[1]/div[1]/ul/li[8]')
    query_statistics = ('xpath', '//*[@id="main"]/div/div[2]/div[1]/div[1]/ul/li[9]')

    """
    视光销售三级菜单 
    """
    opto_sale = ('xpath', '//*[@id="0701$Menu"]/li[1]')  # 视光销售
    sale_order = ('xpath', '//*[@id="0701$Menu"]/li[2]')  # 销售订单
    account_record = ('xpath', '//*[@id="0701$Menu"]/li[3]')  # 挂账记录


    """
    进入二级菜单的方法
    """

    def to_sale_manage(self):
        """进入销售管理"""
        login = login_page.LoginPage(self.driver)
        login.to_opto_operation()
        self.click(self.sale_manage)

    def to_after_sale_manage(self):
        """进入售后管理"""
        login = login_page.LoginPage(self.driver)
        login.to_opto_operation()
        self.click(self.after_sale_manage)

    def to_price_manage(self):
        """进入价格管理"""
        login = login_page.LoginPage(self.driver)
        login.to_opto_operation()
        self.click(self.price_manage)

    def to_inventory_manage(self):
        """进入库存管理"""
        login = login_page.LoginPage(self.driver)
        login.to_opto_operation()
        self.click(self.inventory_manage)

    def to_purchase_manage(self):
        """进入采购管理"""
        login = login_page.LoginPage(self.driver)
        login.to_opto_operation()
        self.click(self.purchase_manage)

    def to_process_manage(self):
        """进入加工管理"""
        login.to_opto_operation()
        self.click(self.process_manage)

    def to_chain_manage(self):
        """进入连锁管理"""
        login.to_opto_operation()
        self.click(self.chain_manage)

    def to_chain_process(self):
        """进入连锁管理"""
        login.to_opto_operation()
        self.click(self.chain_process)

    def to_query_statistics(self):
        """进入查询统计"""
        login.to_opto_operation()
        self.click(self.query_statistics)

    """
    进入三级菜单
    """
    def to_opto_sale(self):
        """进入销售管理--视光销售"""
        opto = OptometrePublicPage(self.driver)
        opto.to_sale_manage()
        self.click(self.opto_sale)

    def to_sale_order(self):
        """进入销售管理--销售订单"""
        opto = OptometrePublicPage(self.driver)
        opto.to_sale_manage()
        self.click(self.sale_order)

    def to_account_record(self):
        """进入销售管理--挂账记录"""
        opto = OptometrePublicPage(self.driver)
        opto.to_sale_manage()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    login = login_page.LoginPage(driver)
    login.login()
    login.to_opto_operation()
    op = OptometrePublicPage(driver)
    op.to_opto_sale()

