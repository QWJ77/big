
"""
@Time    : 2019/11/13
@Author  : qiwj
@Contact : qiwj@gratone.cn
@Software: PyCharm
@Desc    : 销售订单页面类
"""

from common import basePage
from selenium import webdriver
import time

from pages import login_page
from pages.public_page import optometre_public_page


class SalesOrderPage(basePage.BasePage):
    """
    视光销售页面相关元素
    """
    user = ('xpath', "//*[@id='main']/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div/ul/li/div/input")
    test_name = ('xpath','//*[@id="main"]/div/div[2]/div[2]/div/div/div[1]/div/div[1]')
    to_sale = ('xpath', '//*[@id="main"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/button[2]')
    add_pro = ('xpath', '//*[@id="main"]/div/div[2]/div[2]/div/div/div[5]/div[3]/button[1]')
    custom_made_goods = ('xpath', '//*[@id="main"]/div/div[2]/div[2]/div/div/div[6]/div/div/div[1]/div/div/div/div/div[3]')
    good_name_input = ('xpath', '//*[@id="key_2"]')
    choose = ('xpath', '//*[@id="main"]/div/div[2]/div[2]/div/div/div[6]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[4]/span')
    sure = ('xpath', '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/button[2]')
    submit = ('xpath', '//*[@id="main"]/div/div[2]/div[2]/div/div/div[5]/div[3]/button[2]')
    print_sure = ('xpath', '/html/body/div[4]/div/div[2]/div/div[1]/div/div/div[2]/button')
    submit_sure = ('xpath', '/html/body/div[3]/div/div[2]/div/div[1]/div[3]/div/button[1]')
    another_bill_button = ('xpath', '//*[@id="main"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[10]/div/a[2]')
    sale_number_input = ('xpath', '//input[@type="text" and @placeholder="数量"]')
    close = ('xpath', '/html/body/div[3]/div/div[2]/div/div[1]/button/span')
    minus_one = ('xpath', '//*[@id="main"]/div/div[2]/div[2]/div/div/div[5]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr/td[3]/div/div[1]/span[2]')
    """订单金额为0，TIP"""
    amount_tip = ('xpath', '//div[text()="订单总额不允许为0"]')

    """优惠相关元素"""
    js_coupon = "document.getElementsByClassName('body-theme-default ant-layout')[0].scrollLeft=1000"
    choose_coupon = ('link text', '选择整体优惠方案')
    label1 = ('xpath', '/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li[1]/div[2]/div/div[1]/div/div[1]/label/span/input')
    coupon_sure_button = ('xpath', '/html/body/div[3]/div/div[2]/div/div[1]/div[3]/button[2]')

    """更换处方相关元素"""
    replace_button = ('xpath', '//*[@id="main"]/div/div[2]/div[2]/div/div/a')
    new_prescription = ('xpath', '//*[@id="main"]/div/div[2]/div[2]/div/div/div[8]/div/div/div[1]/div[2]')
    choose_prescription = ('link text', '选择')
    replacr_return = ('xpath', '//*[@id="main"]/div/div[2]/div[2]/div/div/div[8]/p/a')

    def another_bill(self):
        """再开一单"""
        public = optometre_public_page.OptometrePublicPage(self.driver)
        public.to_sale_order()
        time.sleep(1)
        self.click(self.another_bill_button)
        time.sleep(1)
        self.click(self.add_pro)
        time.sleep(2)
        self.click(self.custom_made_goods)
        time.sleep(3)
        self.click(self.choose)
        time.sleep(2)
        self.click(self.sure)
        time.sleep(2)

    def submi_bill(self):
        """提交订单"""
        self.click(self.submit)
        time.sleep(2)
        self.click(self.print_sure)
        time.sleep(3)
        self.click(self.submit_sure)
        self.click(self.close)
        time.sleep(2)

    def choose_discount(self):
        """再开一单--选择优惠券"""
        self.another_bill()
        time.sleep(2)
        self.driver.execute_script(self.js_coupon)
        time.sleep(1)
        self.js_focus_element(self.choose_coupon)
        self.click(self.choose_coupon)
        time.sleep(3)
        self.click(self.label1)
        time.sleep(1)
        self.js_focus_element(self.coupon_sure_button)
        self.click(self.coupon_sure_button)
        time.sleep(1)
        self.submi_bill()

    def bill_amount_wrong(self):
        """再开一单--订单金额不能为0"""
        self.another_bill()
        self.click(self.minus_one)
        time.sleep(1)
        # self.sendKeys(self.sale_number_input, 0)
        self.click(self.submit)

    def replace_prescription(self):
        """更换处方"""
        self.another_bill()
        self.click(self.replace_button)
        time.sleep(5)
        self.click(self.new_prescription)
        time.sleep(1)
        self.click(self.choose_prescription)
        time.sleep(1)
        self.submi_bill()


if __name__ == '__main__':

    driver = webdriver.Chrome()
    login = login_page.LoginPage(driver)
    login.login()
    sa = SalesOrderPage(driver)
    time.sleep(1)
    # sa.choose_discount()
    # sa.bill_amount_wrong()
    sa.replace_prescription()

