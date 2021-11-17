# /Users/kongweicheng/desktop
# encoding : utf-8
# system : macbook pro
'''
@author:David
@time:2021/11/148:38 下午
@DESC : 
'''
import configparser
import shutil

import yaml
import os


def get_config(item: str):
    """
    获取/config.ini文件下，api_info标题下，指定item键的值
    :param item: 键
    :return:
    """
    config = configparser.ConfigParser()
    config.read(get_path('/config.ini'))
    items = dict(config.items('api_info'))
    return items[item]


def get_yaml(path):
    """
    获取yaml下的所有内容，并转为字典
    :param path: yaml文件路径
    :return:
    """
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f)   # safe_load(f) yaml自带的函数，作用是将读取后的yaml内容转为字典
    return data


def get_path(path):
    """
    获取绝对路径，并将传入的path拼接到绝对路径末尾
    :param path: 传入的相对路径
    :return:
    """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + path
    return path


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


# get_path()