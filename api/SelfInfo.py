# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/128:00 下午
@DESC : 
'''
from first_debug_api.common.BaseApi import BaseApi
from first_debug_api.common.Action import *


class SelfInfo(BaseApi):
    info_data = get_yaml(get_path('/data/SelfInfoApi.yaml'))

    def check_login(self, phone):
        self.data = {'phone': phone}
        res = self.send_request(self.info_data['check_login'])
        return res

    def get_info(self):
        self.info_data['get_info']['cookies'] = eval(get_config('cookies'))
        res = self.send_request(self.info_data['get_info'])
        return res

    def update_info(self, gender, signature, city, nickname, birthday, province):
        self.data = {'gender': gender, 'signature': signature, 'city': city, 'nickname': nickname, 'birthday': birthday,
                     'province': province}
        self.info_data['update_info']['cookies'] = eval(get_config('cookies'))
        res = self.send_request(self.info_data['update_info'])
        return res


SelfInfo().get_info()