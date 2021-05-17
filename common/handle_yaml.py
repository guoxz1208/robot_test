# coding=utf -8

import os
import sys
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)
import yaml

class ReadYaml:

    def read_yaml(self,file_name=None):
        if file_name == None:
            yaml_path = base_path + '/config/api_config.yml'
        else:
            yaml_path = base_path + file_name
        f = open(yaml_path, 'r', encoding='UTF-8')
        data = f.read()
        datas = yaml.load(data,Loader=yaml.FullLoader)
        return datas

    def get_url(self,api_name):
        contebt = self.read_yaml()
        url = contebt['longlukou_host'] + contebt[api_name]['login']['path']
        return url


if __name__ == '__main__':
    read_yaml = ReadYaml()
    print(read_yaml.read_yaml())
    print(read_yaml.get_url("LongLuKou_Manage"))