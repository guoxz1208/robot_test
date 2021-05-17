# coding = utf -8
from common.excel_xrld import excel_xrld
import json
import sys
import os
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
# base_path = os.getcwd()
sys.path.append(base_path)

class ExcelData:

    def number_value(self):
        resList = []
        idx = 0
        for one in excel_xrld.get_col_value():
            num = excel_xrld.get_cell_value(idx,0)
            idx += 1
            resList.append(num)
        return resList
    def is_run(self,num=None):
        # resList = []
        if num == None:
            num = 0
            for one in excel_xrld.get_col_value():
                is_run = excel_xrld.get_cell_value(num,2)
                num += 1
            # resList.append(is_run)
        return is_run



if __name__ == '__main__':
    data = ExcelData()
    print(data.is_run())