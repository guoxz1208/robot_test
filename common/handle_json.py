# coding:utf -8
import os
import sys
base_path = os.path.abspath(os.path.join(os.getcwd(), '../'))
sys.path.append(base_path)
import json

class HandleJson:
    def read_json(self,file_name=None):

        """
        读取json文件内容
        :param file_name:json文件名称
        """
        if file_name is not None:
            file_path = base_path + file_name
        else:
            file_path = base_path + '/config/test.json'
        with open(file_path,encoding='UTF -8') as f:
            data = json.load(f)
        return data


    def get_value(self,file_name=None):
        """
        读取json文件中内容
        :param file_name:json文件路径
        """
        data = self.read_json(file_name)
        return data

    def with_value(self,data,file_name=None):
        """
        内容写入json文件
        :param data: 内容
        :param file_name: json文件路径
        """
        if data is json:
            data_value = json.dumps(data)
        else:
            data_value = str(data)
        if file_name is not None:
            file_path = base_path + file_name
        else:
            file_path = base_path + '/config/hand_json.json'
        with open(file_path, 'w') as f:
            f.write(data_value)



hand_json = HandleJson()

# token = '<RequestsCookieJar[<Cookie XSRF-TOKEN=eyJpdiI6Ik9IMlJUdTJjeDI2ZTJZWllUbW1FUGc9PSIsInZhbHVlIjoieDNBOUZMcHZxZXlRQTVvdmdoNDlKVndKWXhvZE5ZYzd0dHhcLzI1RnFlMjN4VG9CMTROQjNIUjZES0VZU29JSkQiLCJtYWMiOiI5OWM5Mjc0MmEyNzVkMjg5YTYyYzQyNzllNTY4YzQyODg2MTJhOWI4NTZmODc3MjI1MDVjNDllNGU5YWI1NmI2In0%3D for devrobot.shyunhua.com/>, <Cookie laravel_session=eyJpdiI6IlVISjNPRXZyazlPUGVrZEZ1MG5mcFE9PSIsInZhbHVlIjoiY1JSbU5ocHphMjROZ25xUXlpMXFWb3RBNHZDTXNLUU1qZnBJK3ZHdldnUjFTMVNJaThpSlZ3VjUwcGtJbWRjeSIsIm1hYyI6IjNmZjM3MGJkZjQ4ZjNmZDFjOTBlODdjZjJiMjhhNTJkNGJmYzRmN2Q2NWY0N2RkMmI3OGRkZDkyOGRmYzJlZDYifQ%3D%3D for devrobot.shyunhua.com/>]>'
# print(read_json())
# if __name__ == '__main__':
#     hand_json = HandleJson()
#     data = hand_json.read_json("/config/cookie.json")
#     print(data['token'])
# #     data = {"username":"admin","password":"123456"}
# #     # print(hand_json.get_value())
# #     print(hand_json.with_value(data))