from parameterized import parameterized
# 导包
import unittest, logging
from api.login_api import LoginApi
from app import BASE_DIR

from utils import assert_common, read_data


# 创建unittest的类
class TestIHRMLogin(unittest.TestCase):
    # 进行初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 编写登录成功函数
    @parameterized.expand(read_data(BASE_DIR+"/data/login_data.json"))
    def test01_login_success(self,case_name,request_body,success,code,msg,vreify_code):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login(request_body,headers={"Content-Tyepe":"application/json"})
        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self, vreify_code, success, code, msg, response)
