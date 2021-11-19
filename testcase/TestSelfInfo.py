# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/99:58 下午
@DESC : 
'''
import allure
import pytest
from api.SelfInfo import SelfInfo
from common.Action import *


@allure.feature('people info')
class TestActive:
    s = SelfInfo()  # 实例化业务类SelfInfo，并赋值给s
    # get_path('/data/SelfInfoData.yaml') 获取SelfInfoData.yaml的绝对路径
    # get_yaml（）获取 上面绝路径下的所有yaml内容，并转为字典
    data = get_yaml(get_path('/data/SelfInfoData.yaml'))

    # pytest内置装饰器，作用是参数传递。底层逻辑是for循环，有多少组参数就循环多少次（发送多少次请求）
    # @pytest.mark.parametrize('phone, name', [['0', 'linxin'], ['13103759028', ''], ['231213213', '#$%#$%']])
    @allure.story('check login')
    @pytest.mark.parametrize('phone', data['test_check_login'])
    def test_check_login(self, phone):

        res = self.s.check_login(phone)  # 调用实例化后的SelfInfo类的check_login方法，并将yaml文件中获取的phone参数传递过去，拿到响应
        # 断言
        if not phone:
            self.s.my_assert(res, "assert res.json()['message'] == '手机号或ursToken不能为空'")
        elif phone == '2321321%$%&%' or phone == 0:
            self.s.my_assert(res, "assert res.json()['exist'] == -1")
        elif phone == 13103759028:
            self.s.my_assert(res, "assert res.json()['exist'] == 1")
        ...

    @allure.story('get info')
    def test_get_info(self):
        res = self.s.get_info()
        self.s.my_assert(res, "assert res.json()['code'] == 200")

    @allure.story('update info')
    @pytest.mark.parametrize('gender, signature, city, nickname, birthday, province', data['test_update_info'])
    def test_update_info(self, gender, signature, city, nickname, birthday, province):
        res = self.s.update_info(gender, signature, city, nickname, birthday, province)
        self.s.my_assert(res, "assert res.json()['code'] == 200")

    @allure.story('add music list')
    @pytest.mark.parametrize('name, types, privacy', data['test_add_music_list'])
    def test_add_music_list(self, name, types, privacy):
        res = self.s.add_music_list(name, types, privacy)
        self.s.my_assert(res, "assert res.status_code == 200")

    @allure.story('register')
    @pytest.mark.skip()
    @pytest.mark.parametrize('captcha, phone, password, nickname', data['test_register'])
    def test_register(self, captcha, phone, password, nickname):
        res = self.s.register(captcha, phone, password, nickname)
        self.s.my_assert(res, "assert res.status_code == 200")

    @allure.story('captcha send')
    @pytest.mark.skip()
    @pytest.mark.parametrize('phone', data['test_captcha_send'])
    def test_captcha_send(self, phone):
        res = self.s.captcha_send(phone)
        self.s.my_assert(res, "assert res.status_code == 200")

    @allure.story('new nickname')
    @pytest.mark.parametrize('nickname', data['test_new_nickname'])
    def test_new_nickname(self, nickname):
        res = self.s.new_nickname(nickname)
        self.s.my_assert(res, "assert res.status_code == 200")

    @allure.story('get account info')
    @pytest.mark.parametrize('uid', data['test_get_account_info'])
    def test_get_account_info(self, uid):
        res = self.s.get_account_info(uid)
        self.s.my_assert(res, 'assert res.status_code == 200')
