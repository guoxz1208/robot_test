# coding:utf -8

import os,sys
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)
import json
import configparser
from common.handle_json import hand_json


def get_cookie_value(cookie_key):
    # 读取cookie
    data = hand_json.read_json('/config/cookie.json')
    return data[cookie_key]

def write_cookie(data,cookie_key):
    # 写入cookie
    value = hand_json.read_json('/config/cookie.json')
    value[cookie_key] = data
    hand_json.with_value(value,'/config/cookie.json')

if __name__ == '__main__':
    # data ={"aa":"1111111111111"}
    # cookie = Cookie()
    print(get_cookie_value('token'))
    # print(write_cookie(data,'web'))