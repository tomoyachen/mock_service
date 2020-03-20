#!/usr/bin/env python3
# @Time    : 2020-3-20 15:20
# @Author  : chen
# @FileName: app.py
# @Software: PyCharm
import threading
from core import start_mock_service

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "index"

#启动mock服务路由
@app.route('/start')
def start():
    t_start_mock_service =threading.Thread(target=start_mock_service, args=()) #多线程
    t_start_mock_service.start()
    return "Yes"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5002")


