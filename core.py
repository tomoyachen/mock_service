#!/usr/bin/env python3
# @Time    : 2020-3-20 16:02
# @Author  : chen
# @FileName: core.py
# @Software: PyCharm


def write_file(content, method="a"):
    if method not in ("a", "w"):
        method = "a"
    file_path = "mock.py"
    file = open(file_path, method)
    file.write(content)
    file.close()


# 插入flask头
def make_mock_head():
    content = """
from flask import Flask
app = Flask(__name__)
"""
    write_file(content, "w")


# 插入flask尾（调试用）
def make_mock_tail():
    content = """
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5003")
"""
    write_file(content)


# 写入一个api路由内容
def make_mock_api(route_path, function_name, return_content):
    content = """
@app.route('%s')
def %s():
    return "%s"
""" % (route_path, function_name, return_content)
    write_file(content)


# 启动mock服务，数据来源可以是数据库或者配置文件
def start_mock_service(host="0.0.0.0", port="5003"):
    make_mock_head()
    make_mock_api("/", "index", {"id": 1, "name": "zhangsan"})
    make_mock_api("/aaa", "aaa", "'aaa'")
    make_mock_tail()

    from mock import app
    app.run(host=host, port=port)
