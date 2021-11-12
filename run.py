# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/128:46 下午
@DESC : 
'''
import pytest as pytest
import requests
import configparser


def save_cookies():
    url = 'http://127.0.0.1:3000/login/cellphone'
    params = {'phone': '13103759028', 'password': 'DS465441'}
    res = requests.get(url=url, params=params)
    cookies = requests.utils.dict_from_cookiejar(res.cookies)

    # cun ru ini wenjian
    config = configparser.ConfigParser()
    config.read('./config.ini')
    config.set('api_info', 'cookies', str(cookies))
    config.write(open('./config.ini', 'r+'))


if __name__ == '__main__':
    save_cookies()
    pytest.main(['-s', './TestSelfInfo.py'])