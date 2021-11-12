# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/128:00 下午
@DESC : 
'''
from first_debug_api.common.BaseApi import BaseApi


class SelfInfo(BaseApi):
    info_data = BaseApi().get_yaml('../data/SelfInfoApi.yaml')

    def check_login(self):
        self.data = self.info_data['test_check_login']
        res = self.send_request()
        return res

    def get_info(self):
        self.data = self.info_data['test_get_info']
        self.data['cookies'] = self.get_cookies()
        res = self.send_request()
        return res

    def update_info(self):
        self.data = self.info_data['test_update_info']
        self.data['cookies'] = self.get_cookies()
        res = self.send_request()
        return res

# dfdslkfjdskljfkldsjfjdslkjklfjsadlkfds