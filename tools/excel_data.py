# coding: utf -8

from common.excel_xrld import excel_xrld
from common.handle_ini import hand_init
from base.run_method import RunMethod
from common.handle_cookie import get_cookie_value,write_cookie
from common.handle_header import get_header

from tools.excel_new import ExcelData

import json
import os
import sys
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
# base_path = os.getcwd()
sys.path.append(base_path)

print('------接口测试用例------')
def excel_data(caseName):
    resList = []
    cookie = None
    herder = None
    # 获取url域名
    base_url = hand_init.get_value("HOST","study_url")
    idx = 0
    for one in excel_xrld.get_col_value():
        if caseName in one:
            if excel_xrld.get_cell_value(idx,5) == "yes":
                # 获取用例名称
                name = excel_xrld.get_cell_value(idx, 1)
                print(name)
                # 获取Excel用例是否执行
                is_run = excel_xrld.get_cell_value(idx,2)
                # 获取url路径
                path_url = excel_xrld.get_cell_value(idx,4)
                # 获取请求头是否操作
                is_header = excel_xrld.get_cell_value(idx,6)
                # 获取预期结果方式
                excepect_method = excel_xrld.get_cell_value(idx,10)
                # 获取预期结果
                excepect_result = excel_xrld.get_cell_value(idx,11)
                cookie_method = excel_xrld.get_cell_value(idx,7)
                if cookie_method == 'yes':
                    cookie = get_cookie_value("token")
                    print(cookie)
                if cookie_method == 'write':
                    get_cookie = {"is_cookie": "app"}
                    print(get_cookie)
                if is_header == 'yes':
                    herder = get_header()
                    print(herder)
                if is_run in 'yes':
                    # 获取请求类型
                    resMethod = excel_xrld.get_cell_value(idx,5)
                    # 获取整体的url
                    resUrl = base_url + path_url
                    resBaby = excel_xrld.get_cell_value(idx,9)
                    is_Header = excel_xrld.get_cell_value(idx,6)
                    if is_Header == 'yes':
                        baby = json.loads(resBaby)
                    else:
                        Baby = None


            # resList.append(resBaby)
        idx += 1
    # return resList

if __name__ == '__main__':

    print(excel_data('new'))
