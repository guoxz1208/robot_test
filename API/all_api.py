# coding:utf -8
import os,sys
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)

from base.run_method import RunMethod
from common.excel_openpyxl import excel_openpyxl
from common.excel_xrld import excel_xrld
from common.handle_ini import hand_init
from common.get_log import get_log
import json

class ALLApi:

    # 接口请求封装
    def send_request(self,key,value):
        try:
            base_url = hand_init.get_value(key,value)
            print(base_url)
            row = excel_xrld.get_row()
            header = None
            for i in range(row):
                print('=============')
                data = excel_xrld.get_row_value(i+1)
                # print(data)
                name = data[1]
                print(name)
                methon = data[5]
                print(methon)
                path_url = data[4]
                url = base_url + data[4]
                print(url)
            #     headers = data[6]
            #     # print(url)
            #     if methon == "GET":
            #         response = RunMethod.run_main(methon,url,headers)
            #     elif methon == "POST":
            #         payload = data[8]
            #         response = RunMethod.run_main(methon,url,payload,headers)
            #     elif methon == "":
            #         pass
        except:
            print('===============')

if __name__ == '__main__':
    all_api = ALLApi()
    print(all_api.send_request("HOST","qiaoliang_url"))