# coding =utf -8
import pytest
import os
from tools.excel_test import excel_data
from API.all_api import RunMethod


('新增01', 'yes', 'http://127.0.0.1:8099/api/departments/', 'POST', 'qwertyuiopsdfghjklcvbnm', {'Content-Type': 'application/json'}, '{"data": [{"dep_id": "study001","dep_name": "study01学院","master_name": "study01校长","slogan": "Here is Slogan"}]}')
class TestLogin:
    @pytest.mark.parametrize('name,is_run,url,method,token,header,response',excel_data('new'))
    def test_new(self,name,is_run,url,method,token,header,response):
        res = RunMethod().run_main(method,url,response,token)
        return res

class TestSelect:
    @pytest.mark.parametrize('name,is_run,url,method,token,header,response', excel_data('select'))
    def test_select(self,name,is_run,url,method,token,header,response):
        res = RunMethod().run_main(method, url, response)
        return res

if __name__ == '__main__':
    pytest.main(['test_case.py','-s','--alluredir','../report/tmp'])
    os.system('allure serve ../report/tmp')