# coding:utf -8
import os,sys
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)
import requests
import json
from common.excel_openpyxl import excel_openpyxl
from common.excel_xrld import excel_xrld
from common.handle_cookie import write_cookie
from common.handle_json import hand_json
from common.handle_ini import hand_init

class RunMethod:

    def post_main(self,url,data,headers=None,cookie=None,get_cookie=None):

        # 遇到requests的ssl验证，若想直接跳过不验证，设置verify=False即可
        response = requests.post(url=url, json=data,cookies=cookie, headers=headers,cookie=cookie, verify=False)
        if get_cookie != None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        res = response.text
        return res


    def get_main(self,url,data=None,herders=None,cookie=None,get_cookie=None):

        if data is not None:
            response = requests.get(url=url,data=data,herders=herders,cookie=cookie, verify=False)
        else:
            response = requests.get(url=url,headers=herders, verify=False)
        res = response.text
        return res


    def put_main(self,url,data=None,headers=None,cookie=None,get_cookie=None):

        response = requests.post(url=url,json=data,headers=headers,cookie=cookie, verify=False)
        res = response.text
        return res


    def delete_main(self,url,data=None,headers=None,cookie=None,get_cookie=None):

        if data is not None:
            response = requests.delete(url=url, data=data, herders=headers,cookie=cookie, verify=False)
        else:
            response = requests.delete(url=url, headers=headers, verify=False)
        res = response.text
        return res


    def run_main(self,methon,url,data=None,headers=None,cookie=None,get_cookie=None):

        # base_url = hand_init.get_value('HOST','study_url')
        # if 'http' not in url:
            # url = base_url + url

        if methon == "GET":
            res = self.get_main(url,data,headers,cookie,get_cookie)
        elif methon == "POST":
            res = self.post_main(url,data,headers,cookie,get_cookie)
        elif methon == "PUT":
            res = self.put_main(url,data,headers,cookie,get_cookie)
        else:
            res = self.delete_main(url,data,headers,cookie,get_cookie)
        try:
            res = res.json()
        except:
            print("这个结果是一个text")
            # return res
        return res

run_method = RunMethod()

if __name__ == '__main__':


    methon = "SELECT"
    url = "http://127.0.0.1:8099/api/departments/study002/"
    # data = {"data": [{"dep_id": "study001","dep_name": "study01学院","master_name": "study01校长","slogan": "Here is Slogan"}]}
    payload = {'data': [{'dep_id': 'study001', 'dep_name': 'C++/学院', 'master_name': 'C++-Master', 'slogan': 'Here is Slogan'}]}
    # header = {"Content-Type":"application/json"}
    print(run_method.run_main(methon,url,headers=None,cookie=None))