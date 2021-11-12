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


class BaseApi:
    data = {}

    def get_cookies(self):
        config = configparser.ConfigParser()
        config.read('./config.ini')
        items = dict(config.items('api_info'))
        return eval(items['cookies'])

    def get_yaml(self, path):
        with open(path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data

    def send_request(self):
        # data =
        # json =
        # params , 路由由"？"拼接参数

        res = requests.request(  # res 为请求的响应数据对象
            method=self.data["method"],
            url=self.data["url"],
            params=self.data["params"],
            data=self.data["data"],
            cookies=self.data["cookies"]
            # headers={},  # 请求头
            # verify=True,  # 是否验证证书
            # proxies={'http': '127.0.0.1: 8000'},  # 代理
            # files='./xxx/xx.jpg'  # 上传图片
        )
        # print(res.status_code)
        # print(res.text)
        # print(res.headers)
        return res
