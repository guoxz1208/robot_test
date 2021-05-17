# coding: utf -8
import json
import os,sys
base_file = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_file)
import xlrd

class Excel_Xrld:
    def load_excel(self,file_name=None,):
        if file_name == None:
            file_path = base_file + '/data/学生信息管理系统接口测试用例v1.0.xlsx'
        else:
            file_path = base_file + file_name
        open_excel = xlrd.open_workbook(file_path,formatting_info=False)
        return open_excel

    def get_sheet_data(self,num=None):
        """
        获取Excel中全部sheet
        """
        if num == None:
            num = 0
        sheet_name = self.load_excel().sheet_by_index(num)
        return sheet_name

    def get_cell_value(self,row,cols):
        """
        获取某个单元格内容
        """
        cell_value = self.get_sheet_data().cell_value(row,cols)
        return cell_value

    def get_row(self):
        """
        获取有效总行数
        """
        row_num = self.get_sheet_data().nrows
        return row_num

    def get_row_value(self,rows):
        """
        获取某一行内容
        """
        row_list = []
        for i in self.get_sheet_data().row_values(rows):
            row_list.append(i)
        return row_list

    def get_col(self):
        """
        获取总列数
        """
        col_num = self.get_sheet_data().ncols
        return col_num

    def get_col_value(self,col=None):
        """
        获取某一列内容
        """
        if col == None:
            col = 0
        col_value = self.get_sheet_data().col_values(col)
        return col_value

    def get_value(self,num=None):
        """
        获取Excel全部内容
        """
        row_list = []
        if num == None:
            num=0
        for i in range(num, self.get_row()):
            data = self.get_row_value(i)
            row_list.append(data)
        return row_list

excel_xrld = Excel_Xrld()

# if __name__ == '__main__':
#     excel_xrld = Excel_Xrld()
    # 获取Excel中全部sheet
    # print(excel_xrld.get_sheet_data(0))
    # print(excel_xrld.get_cell_value(1,8))
    # print(excel_xrld.get_row())
    # print(excel_xrld.get_row_value(1))
    # print(excel_xrld.get_col())
    # print(excel_xrld.get_col_value(0))
    # print(excel_xrld.get_value())