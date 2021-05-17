# coding:utf -8
import configparser
import os, sys
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
# base_path = os.getcwd()
sys.path.append(base_path)

# cf = configparser.ConfigParser()
# cf.read(base_path+'/config/server.ini',encoding='UTF-8')
# data = cf.get('HOST','rootManage')
# print(data)

class HandleIni:

    def load_ini(self,file_name=None):
        cf = configparser.ConfigParser()
        if file_name is not None:
            file_path = base_path + file_name
        else:
            file_path = base_path + '/config/server.ini'
        cf.read(file_path,encoding='UTF-8-sig')
        return cf

    def get_value(self,key,value=None):
        if value == None:
            value = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(key,value)
        except Exception:
            print("没有获取到值，输入信息有误")
            data = None
        return data
hand_init = HandleIni()
# if __name__ == '__main__':
#     print(HandleIni().get_value("HOST",'study_url'))