# /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask
import yaml


def import_config():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


app = Flask(__name__)
# 初始化配置
config = import_config()
for key, value in config.items():
    app.config[key] = value

from applications.api import api

app.register_blueprint(api)
