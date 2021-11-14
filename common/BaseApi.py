# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/119:54 下午
@DESC : 
'''
import configparser
import requests
import yaml
from first_debug_api.common.Action import *


class BaseApi:
    data = {}  # {'phone': ''}
    _host = get_config('host')

    def send_request(self, api_info: dict):
        # data =
        # json =
        # params , 路由由"？"拼接参数

        api_info = str(api_info).replace('${host}', self._host)  # ti huan host

        for i, j in self.data.items():
            api_info = api_info.replace('${%s}' % i, str(j))  # ${phone}

        api_info = eval(api_info)

        print("\n请求参数：" + str(api_info))
        res = requests.request(  # res 为请求的响应数据对象
            method=api_info["method"],
            url=api_info["url"],
            params=api_info["params"],
            data=api_info["data"],
            cookies=api_info["cookies"]
            # headers={},  # 请求头
            # verify=True,  # 是否验证证书
            # proxies={'http': '127.0.0.1: 8000'},  # 代理
            # files='./xxx/xx.jpg'  # 上传图片
        )
        # print(res.status_code)
        # print(res.text)
        # print(res.headers)
        print("响应体: " + res.text + "\n")
        return res
