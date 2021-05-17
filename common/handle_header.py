# coding=utf -8
import sys
import os
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
# base_path = os.getcwd()
sys.path.append(base_path)
from common.handle_json import hand_json

def get_header():
    data = hand_json.read_json('/config/header.json')
    return data

def header_md5():
    data = get_header()
    key = data["Content-Type"]
    print(key)

# header_md5()