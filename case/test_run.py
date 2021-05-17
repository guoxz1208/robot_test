# coding = utf -8
import requests

from common.excel_xrld import excel_xrld
from common.handle_ini import hand_init
from base.run_method import run_method
import json
import os,sys
base_path = os.getcwd()
sys.path.append(base_path)

class AllApi:

    def read_value(self):
        row = excel_xrld.get_rows()
        print(row)
        for i in range(row):
            data = excel_xrld.get_rows_value(i+2)
            # print(data)
            # base_url = hand_init.get_value("HOST", "study_url")
            base_url = hand_init.get_value("HOST","study_url")
            print(data)
            is_run = data[2]
            if is_run == 'yes':
                path_url = data[4]
                method = data[5]
                is_header = data[7]
                url = base_url + path_url
                print(url)
                if is_header == 'yes':
                    payload = json.loads(data[8])
                    print(payload)
                else:
                    payload = None
                res = run_method.run_main(method,url,payload)
                print(res)
                # codes = str(res['code'])
                # mess = str(res['message'])
                # print('------>',codes)
                # print('------>',mess)
                expect_data = data[10]
                # if codes in expect_data:
                #     print("通过")
                #     excel_data.excel_write_data(i + 2, 12, json.dumps(res), '龙路口桥梁登录系统')
                # else:
                #     print("不通过")
                #     excel_data.excel_write_data(i+2,12,json.dumps(res),'龙路口桥梁登录系统')
                #     excel_data.excel_write_data(i + 2, 13, 'error', '龙路口桥梁登录系统')










if __name__ == '__main__':
    all_api = AllApi()
    all_api.read_value()
    # url = "http://127.0.0.1:8099/api/departments/study001"
    # data = {"data": [{"dep_id": "study001","dep_name": "study01学院","master_name": "study01校长","slogan": "Here is Slogan"}]}
    # # res = requests.post(url=url,json=data)
    # res = requests.delete(url=url)
    # print(res.json())
