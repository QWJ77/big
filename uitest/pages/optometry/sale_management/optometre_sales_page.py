
"""
@Time    : 2019/10/28
@Author  : qiwj
@Contact : qiwj@gratone.cn
@Software: PyCharm
@Desc    : 视光销售页面类
"""

from common import basePage
from selenium import webdriver
import time

from pages import login_page
from pages.public_page import optometre_public_page
from selenium.webdriver.common.keys import Keys


class OptometreSalesPage(basePage.BasePage):
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

    """新增验光记录"""
    add_optometry_button = ('xpath', '//*[@id="main"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/button[1]')
    optometrists = ('xpath', '/html/body/div[3]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/form/div/div[2]/div/div/div[2]/div/div[1]/div/div')
    select_optometrists = ('xpath', '/html/body/div[4]/div/div/div/ul/li[1]')
    near_od = ('id', 'opto_near_od_sphere')
    near_os = ('id', 'opto_near_os_sphere')
    save_optometry = ('xpath', '/html/body/div[3]/div/div[2]/div/div[1]/div[2]/button[2]')

    """删除验光记录"""
    delete_record = ('xpath', '//*[@id="main"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[5]/span/a[2]')
    delete_sure = ('xpath', '/html/body/div[5]/div/div/div/div[2]/div/div/div[2]/button[2]')

    def query_users(self, user_name='测试012'):
        """查询用户"""
        opto = optometre_public_page.OptometrePublicPage(self.driver)
        opto.to_opto_sale()
        time.sleep(1)
        self.sendKeys(self.user, text=user_name)
        time.sleep(2)
        self.sendKeys(self.user, Keys.DOWN)
        time.sleep(1)
        self.sendKeys(self.user, Keys.ENTER)

    def draw_a_bill(self):
        """销售开单"""
        self.click(self.to_sale)
        time.sleep(1)
        self.click(self.add_pro)
        time.sleep(1)
        self.click(self.custom_made_goods)
        time.sleep(3)
        # self.sendKeys(self.good_name_input, text=good_name)
        # self.sendKeys(self.good_name_input, Keys.ENTER)
        # wait = WebDriverWait(self.driver, 15, 0.5)
        # wait.until(EC.presence_of_element_located(self.choose))
        # self.driver.implicitly_wait(15)
        self.click(self.choose)
        time.sleep(2)
        self.click(self.sure)
        time.sleep(2)
        self.click(self.submit)
        time.sleep(1)
        self.click(self.print_sure)
        time.sleep(3)
        self.click(self.submit_sure)
        self.click(self.close)
        time.sleep(2)

    def add_optometry_record(self,  near_od='+12.00', near_os='+12.00'):
        """新增验光记录"""
        self.query_users()
        time.sleep(1)
        self.click(self.add_optometry_button)
        time.sleep(1)
        self.click(self.optometrists)
        time.sleep(1)
        self.click(self.select_optometrists)
        time.sleep(1)
        # self.sendKeys(self.optometrists, Keys.ENTER)
        # time.sleep(1)
        self.sendKeys(self.near_od, near_od)
        time.sleep(1)
        self.sendKeys(self.near_os, near_os)
        time.sleep(2)
        self.click(self.save_optometry)

    def delete_optometry_record(self):
        """删除验光记录"""
        self.click(self.delete_record)
        time.sleep(1)
        self.click(self.delete_sure)

    def bill_amount_wrong(self):
        """订单金额不能为0"""
        opto = optometre_public_page.OptometrePublicPage(self.driver)
        opto.to_sale_order()
        time.sleep(1)
        self.click(self.another_bill_button)
        time.sleep(1)
        self.click(self.add_pro)
        time.sleep(1)
        self.click(self.custom_made_goods)
        time.sleep(3)
        self.click(self.choose)
        time.sleep(2)
        self.click(self.sure)
        time.sleep(2)
        self.click(self.minus_one)
        time.sleep(1)
        # self.sendKeys(self.sale_number_input, 0)
        self.click(self.submit)


if __name__ == '__main__':

    driver = webdriver.Chrome()
    login = login_page.LoginPage(driver)
    login.login()
    op = OptometreSalesPage(driver)
    # op.add_optometry_record()
    # time.sleep(1)
    # op.delete_optometry_record()
    op.query_users()
    op.draw_a_bill()
    # op.bill_amount_wrong()

