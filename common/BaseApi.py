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
from first_debug_api.common.logs import Logger


class BaseApi:
    data = {}  # {'phone': ''， 'name'： '3333'}
    _host = get_config('host')  # 获取/config.ini下的host的值
    log = Logger('base')

    def my_assert(self, res, ass, *args):
        """
        封装断言+日志
        """

        try:
            exec(ass)
            self.log.logger.info(
                '{}: 用例通过，请求时间：{}s'.format(sys._getframe().f_back.f_code.co_name, res.elapsed.total_seconds()))
        except:
            self.log.logger.error(
                '{}: 断言失败 \n 参数：{} \n 返回值: {}'.format(sys._getframe().f_back.f_code.co_name, self.data, res.text))
            raise AssertionError('断言失败')

    def send_request(self, api_info: dict):
        # data =
        # json =
        # params , 路由由"？"拼接参数
        """
        发送请求：供业务层调用
        替换url、请求体参数
        :param api_info: 业务层传递过来的接口信息，包括method、url、params、cookies等
        :return:
        """
        api_info = str(api_info).replace('${host}', self._host)  # 替换url中的host，用的是字符串替换方法replace

        for i, j in self.data.items():  # 遍历data。第一次：i=phone，j=''，第二次：i=name，j=3333
            api_info = api_info.replace('${%s}' % i, str(j))  # 将 ${xxx} 替换成data对应键的值

        api_info = eval(api_info)  # 转成字典

        # print("\n请求参数：" + str(api_info))
        # l=Logger(a)
        # self.l.logger.warning("\n请求参数：" + str(api_info))
        # 发送请求，将响应赋值给res
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
        # print("响应体: " + res.text + "\n")
        # self.l.logger.warning("响应体: " + res.text + "\n")
        return res  # 将响应返回

