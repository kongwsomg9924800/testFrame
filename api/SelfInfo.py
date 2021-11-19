# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/128:00 下午
@DESC : 
'''
from common.BaseApi import BaseApi
from common.Action import *


class SelfInfo(BaseApi):
    info_data = get_yaml(get_path('/data/SelfInfoApi.yaml'))  # 获取yaml文件的请求相关数据，info_data类型为字典

    def check_login(self, phone):
        self.data = {'phone': phone}  # 将父类的data属性赋值，键为'phone'，值为入参
        res = self.send_request(
            self.info_data['check_login'])  # 调用父类的send_request方法，并将SelfInfoApi.yaml中的check_login数据传入，拿到响应
        return res  # 将响应返回给 用例层

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

    def add_music_list(self, name, types, privacy):
        self.data = {'name': name, 'types': types, 'privacy': privacy}
        self.info_data['add_music_list']['cookies'] = eval(get_config('cookies'))
        res = self.send_request(self.info_data['add_music_list'])
        return res

    def register(self, captcha, phone, password, nickname):
        self.data = {'captcha': captcha, 'phone': phone, 'password': password, 'nickname': nickname}
        res = self.send_request(self.info_data['register'])
        return res

    def captcha_send(self, phone):
        self.data = {'phone': phone}
        res = self.send_request(self.info_data['captcha_send'])
        return res

    def new_nickname(self, nickname):
        self.data = {'nickname': nickname}
        self.info_data['new_nickname']['cookies'] = eval(get_config('cookies'))
        res = self.send_request(self.info_data['new_nickname'])
        return res

    def get_account_info(self, uid):
        self.data = {'uid': uid}
        # self.info_data['new_nickname']['cookies'] = eval(get_config('cookies'))
        res = self.send_request(self.info_data['get_account_info'])
        return res


SelfInfo().get_info()
