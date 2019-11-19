# -*- coding=utf-8 -*-
import copy
from requester.web_requester import WebRequester
from service.optometry_service import charg_account_list
from requester.base_requester import check_fields
from env_switch import constants
import pdb
import datetime
import time
#import xlrd
import os
# import pdfminer
# from xlwt import Workbook

REQUESTER = WebRequester()


def get_date():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    return today.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d")


def export_one():
    """导出一个excel文件"""
    resp = REQUESTER.get('/jasreport_service/sale_service/supplier_query/print/excel?start_time={}&end_time={}'
                         '&good_supplier=147624202915152807'.format(get_date()[0], get_date()[0]))
    file_name = int(time.time())
    with open('./cases/excel/{}.xls'.format(file_name), "wb") as fp:
        # fp.write(resp.content)数据量不大时可用。数据量大时用下面的方法
        for chunk in resp.iter_content(chunk_size=128):
            fp.write(chunk)
    return file_name


def export_pdf():
    """导出一个pdf文件"""
    resp = REQUESTER.get('/jasreport_service/sale_service/supplier_query/print/pdf?start_time={}&end_time={}'
                         '&state=null&good_supplier=147624202915152807'.format(get_date()[0], get_date()[0]))
    # resp = REQUESTER.get('/jasreport_service/sale_service/supplier_query/print/excel?start_time=2018-12-01&
    # end_time=2018-12-31&good_supplier=1000005')
    file_name = int(time.time())
    with open('./cases/excel/{}.pdf'.format(file_name), "wb") as fp:
        # fp.write(resp.content)数据量不大时可用。数据量大时用下面的方法
        for chunk in resp.iter_content(chunk_size=128):
            fp.write(chunk)
    return file_name


def sale():
    """新增一个销售单"""
    resp = REQUESTER.post('/sale_service/sales_order', data=constants.SALE_INFO)
    return resp['data']['sale_id']


def pay():
    """收费"""
    bill_id = sale()
    constants.PAY_INFO['bill_id'] = bill_id
    REQUESTER.post('/charge_service/business/pay', data=constants.PAY_INFO)
    resp = REQUESTER.get('/sale_service/sales_order/list?page_size=9&page_num=1&start_time={}&end_time={}'
                         '&readLoading=false'.format(get_date()[0], get_date()[0]))
    for item in resp['data']['list']:
        if item['sale_id'] == bill_id:
            return item['sale_no']
        break


def custom_warehousing():
    """定做入库"""
#     定做入库
    global SALE_NO
    SALE_NO = pay()
    resp = REQUESTER.get('/opto_service/stock_manage/custom_good/list?key={}&page_size=50&depo_id={}'
                         .format(SALE_NO, constants.DEPOT_ID_))
    print SALE_NO
    if resp['data']['list']:
        stat_id = resp['data']['list'][0]['stat_id']
        constants.ARRIVE_INFO['item'][0]['sale_no'] = SALE_NO
        constants.ARRIVE_INFO['item'][0]['stat_id'] = stat_id
        today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        constants.ARRIVE_INFO['arri_time'] = today
        REQUESTER.post('/opto_service/stock_manage/arrival', data=constants.ARRIVE_INFO)


def pick():
    """取件"""
    # 查询需要取件的单号
    resp = REQUESTER.get('/depo_service/pick/list?stat_depo_id={}&start_date={}&end_date={}&key={}&page_num=1'
                         '&page_size=5&stat_purchase=1&stat_pickup=0'.format(constants.WDEPOT_ID, get_date()[0],
                                                                             get_date()[0], SALE_NO))
    stat_id = resp['data']['list'][0]['stat_id']
    stoc_id = resp['data']['list'][0]['stoc_id']
    PICK_INFO = {
        "stat_purchase": 1,
        "stat_id": stat_id,
        "stoc_id": stoc_id
    }
    REQUESTER.post('/depo_service/pick', data=PICK_INFO)


def pick_yestody():
    """取件昨天的"""
    # 查询需要取件的单号
    resp = REQUESTER.get('/depo_service/pick/list?stat_depo_id={}&start_date={}&end_date={}&keys=耐克T36151红色&page_num=1&page_size=5&stat_purchase=1&stat_pickup=0'.format(constants.WDEPOT_ID, get_date()[1],get_date()[1]))
    stat_id = resp['data']['list'][0]['stat_id']
    resp = REQUESTER.get('/depo_service/pick/batc/cust/list?goods_id=175773347802644969&stat_id={}&stat_depo_id={}'.
                         format(stat_id, constants.WDEPOT_ID))
    stoc_id = resp['data']['list'][0]['stoc_id']
    PICK_INFO = {"stat_purchase": 1, "stat_id": stat_id, "stoc_id": stoc_id}
    REQUESTER.post('/depo_service/pick', data=PICK_INFO)


def read_excel():
    # 打开文件
    file_name = export_one()
    workbook = xlrd.open_workbook(r'./cases/excel/{}.xls'.format(file_name))
    # 获取所有sheet
    print workbook.sheet_names()  # [u'sheet1', u'sheet2']
    sheet_name = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    # sheet2 = workbook.sheet_by_index(1)  # sheet索引从0开始
    sheet2 = workbook.sheet_by_name(sheet_name)
    # sheet的名称，行数，列数
    print sheet2.name, sheet2.nrows, sheet2.ncols

    # 获取整行和整列的值（数组）
    # rows = sheet2.row_values(3)  # 获取第四行内容
    # cols = sheet2.col_values(2)  # 获取第三列内容
    # print rows
    # print cols

    # 获取单元格内容
    resp = REQUESTER.get('/sale_service/query/custom_statistics?start_time={}&end_time={}&page_size=2'
                         .format(get_date()[0], get_date()[0]))
    for item in resp['data']['list']:
        if item['good_supplier'] == constants.SUPPLIER_ID:
            total = item['total']
            break
    for row in range(0, sheet2.nrows):
        if sheet2.cell(row, 0).value == u"合计":
            row_ = row
            break
    assert sheet2.cell(row_, 9).value == str(total)
    assert sheet2.cell(4, 4).value == u"耐克T36151红色"
    # print sheet2.cell_value(1, 0).encode('utf-8')
    # print sheet2.row(1)[0].value.encode('utf-8')

    # 获取单元格内容的数据类型
    # print sheet2.cell(1, 0).ctype
    os.remove('./cases/excel/{}.xls'.format(file_name))


# def test_case():
#     # 新生成一个单子
#     custom_warehousing()
#     # 取件其中的一个
#     pick()
#     # 取件一个昨天付款的
#     # custom_warehousing()
#     pick_yestody()
#     # 定做查询，找到今天的，导出。查看数据是否正确
#     read_excel()


def test_add_anthor():
    """再新增一个销售单不取件，给明天用"""
    custom_warehousing()


if __name__ == '__main__':
    export_pdf()
