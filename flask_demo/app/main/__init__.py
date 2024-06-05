from flask import Blueprint

# dddd
# 创建主蓝本 指定蓝本名称和蓝本所在包或模块,与应用一样,第二参数使用python的__name__即可
main = Blueprint('main', __name__)

from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
