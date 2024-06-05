from flask import Blueprint

api = Blueprint('api', __name__)

# eeee
# 将导入模块和蓝本关联, 注意末尾导入避免循环导入依赖,因为模块内部还要导入蓝本
from . import authentication, posts, users, comments, errors
