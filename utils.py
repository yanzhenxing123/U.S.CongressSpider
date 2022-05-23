"""
@Author: yanzx
@Date: 2022/5/19 23:13
@Description: 
"""
import os
import re
from typing import Dict
from urllib.parse import quote, unquote

root_url = "https://www.congress.gov/"


def get_project_path():
    """得到项目路径"""
    project_path = os.path.join(
        os.path.dirname(__file__), "."
    )
    return project_path


def print_dict(data: Dict):
    """
    格式化输出字典
    :param data:
    :return:
    """
    for key, value in data.items():
        print(str(key) + ': ' + str(value))
    print("*" * 100)


def format_url(url: str):
    """
    匹配 url，将 ?q=后面的去掉
    :param url: 原始url
    :return: 匹配后的url
    """
    try:
        url = re.search('(.*?)(\?)', url).group(1)
    except Exception:
        url = url
    if url:
        return root_url + url
    return url


def quote_text(text: str):
    """
    url编码
    :param text:
    :return:
    """
    return quote(text, 'utf-8')


def unquote_text(text: str):
    """
    url解码
    :param text:
    :return:
    """
    return unquote(text, 'utf-8')


if __name__ == '__main__':
    text = "https://www.congress.gov/search?q=%7B%22congress%22%3A%5B%22117%22%5D%2C%22source%22%3A%22all%22%2C%22search%22%3A%22health+care%22%7D&pageSize=100&page=1"
    res = unquote_text(text)
    print(res)
