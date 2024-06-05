import unittest
from flask import current_app
from flask_demo.app import create_app, db

# kkkk python标准库unittest编写单元测试
class BasicsTestCase(unittest.TestCase):
    # 各测试之前运行
    def setUp(self):
        # 创建测试环境
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        # 创建全新数据库,供测试使用,应用上下文和数据库在tearDown()方法中删除
        db.create_all()
    # 各测试之后运行
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    # test_开头方法作为测试用行
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
