# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/99:58 下午
@DESC : 
'''
import pytest

from first_debug_api.api.SelfInfo import SelfInfo
from first_debug_api.common.Action import *


class TestActive:
    s = SelfInfo()
    data = get_yaml(get_path('/data/SelfInfoData.yaml'))

    @pytest.mark.parametrize('phone', data['test_check_login'])
    def test_check_login(self, phone):
        res = self.s.check_login(phone)
        if not phone:
            assert res.json()['message'] == '手机号或ursToken不能为空'
        elif phone == '2321321%$%&%' or phone == 0:
            assert res.json()['exist'] == -1
        elif phone == 13103759028:
            assert res.json()['exist'] == 1
        ...

    def test_get_info(self):
        res = self.s.get_info()
        assert res.json()['code'] == 200

    @pytest.mark.parametrize('gender, signature, city, nickname, birthday, province', data['test_update_info'])
    def test_update_info(self, gender, signature, city, nickname, birthday, province):
        res = self.s.update_info(gender, signature, city, nickname, birthday, province)
        assert res.json()['code'] == 200
