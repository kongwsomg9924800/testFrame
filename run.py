# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/128:46 下午
@DESC : 
'''
import logging
import os

import pytest as pytest
import requests
import configparser
from common.Action import get_path, del_file


def save_cookies():
    # 保存cookie
    url = 'http://127.0.0.1:3000/login/cellphone'  # 定义变量，值为请求url
    params = {'phone': '18813963217', 'password': 'a18839770280'}  # 定义变量，值为请求体
    res = requests.get(url=url, params=params)  # 调用python的第三方库requests，传入参数，发送请求。res为收到的响应
    cookies = requests.utils.dict_from_cookiejar(res.cookies)  # 根据上面的响应（res），提取cookies，并保存后赋值给cookies变量

    # 存入到ini文件？？？

    config = configparser.ConfigParser()  # 调用python的标准库configparser，并实例化
    config.read(get_path('/config.ini'))  # 读取/config.ini文件，get_path('/config.ini')为自定义方法，作用是获取绝对路径
    config.set('api_info', 'cookies', str(cookies))  # 将ini文件中的api_info标题下的cookies键赋值为str(cookies)
    config.write(open(get_path('/config.ini'), 'r+'))  # 保存


if __name__ == '__main__':  # 程序入口，运行整个项目
    save_cookies()  # 调用自定义方法，获取并保存cookies到config文件。目的是数据持久化，供其他接口使用。
    allure_path = get_path('/report/allure/')
    case_path = get_path('/testcase/TestSelfInfo.py')
    del_file(allure_path)
    pytest.main(['-s', '--alluredir', allure_path, case_path])  # pytest的内置方法 -s 参数是打印详细信息，
    os.system('allure serve ' + allure_path)  # 运行allure服务
    # 'testcase/TestSelfInfo.py' 意思是执行'TestSelfInfo.py'下的所有用例
    # allure测试报告：
    # 1、brew install allure  本机安装allure环境（可以使用allure命令）
    # 2、pip install allure-pytest  python环境安装allure第三方库
    # 3、给用例代码中加装饰器：
    # 3-1：目录装饰器： @allure.feature("一级目录")    @allure.story("二级目录")
    # 3-2：严重等级装饰器： @allure.severity(xxx)  blocker  critical  normal  minor  trivial
    # 4、运行时生成allure报告：pytest.main(['--alluredir', allure报告存放路径])
    # 5、运行allure服务（看报告）：allure server -p 端口号 allure报告存放路径
