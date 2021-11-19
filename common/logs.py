# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/149:22 下午
@DESC :
'''
import logging
import os
from logging import handlers

from common.Action import get_path


class Logger:

    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    if os.path.exists(get_path('/report/logs')) is False:
        os.mkdir(get_path('/report/logs'))
    filename = get_path('/report/logs/all.log')

    def __init__(self, log_name, filename=filename, level='debug', when='D', backCount=3,
                 fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):

        self.logger = logging.getLogger(log_name)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                               encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)


# if __name__ == '__main__':
    # logs = Logger('xxxxxx')
    # logs.logger.debug('debug')
    # logs.logger.info('info')
    # logs.logger.warning('警告')
    # logs.logger.error('报错')
    # logs.logger.critical('严重')
