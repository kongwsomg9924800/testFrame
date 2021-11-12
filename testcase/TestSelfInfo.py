# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/99:58 下午
@DESC : 
'''
from first_debug_api.api.SelfInfo import SelfInfo


class TestActive:
    s = SelfInfo()

    def test_check_login(self):
        res = self.s.check_login()
        assert res.json()['code'] == 200

    def test_get_info(self):
        res = self.s.get_info()
        assert res.json()['code'] == 200

    def test_update_info(self):
        res = self.s.update_info()
        assert res.json()['code'] == 200

