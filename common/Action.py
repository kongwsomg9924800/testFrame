# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/148:38 下午
@DESC : 
'''
import configparser
import yaml
import os


def get_config(item: str):
    config = configparser.ConfigParser()
    config.read(get_path('/config.ini'))
    items = dict(config.items('api_info'))
    return items[item]


def get_yaml(path):
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


def get_path(path):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + path
    return path


# get_path()