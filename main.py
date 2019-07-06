import unittest
import json
import base64
from api.api_class import API

class TestTrionesAPI(unittest.TestCase):
    def setUp(self):
        token = "***"
        self.handler = API(token)

    def test_get(self):
        # get user info
        # 位置参数
        self.handler.get_user_info("kailunfan")
        self.handler.get_repo("kailunfan", "githubApiTest")
        # 关键字参数
        self.handler.get_issuess("kailunfan", "githubApiTest")
        self.handler.get_issuess("kailunfan", "githubApiTest", state="closed")

    def test_modify_file(self):
        # 新建一个文件,路径为/src/test_set_file.txt
        data = {
            "message": "new file",
            "content": base64.b64encode("this is the original content!".encode()).decode()
        }
        file_info = self.handler.set_file("kailunfan", "githubApiTest", "src/test_set_file2.txt", data=data)

        # 更改这个文件
        data = {
            "message": "update file",
            "content": base64.b64encode("this is new content!".encode()).decode(),
            "sha":file_info['content']['sha']
        }
        file_info = self.handler.set_file("kailunfan", "githubApiTest", "src/test_set_file2.txt", data=data)

        # 删除这个文件
        data = {
            "message": "delete file",
            "sha":file_info['content']['sha']
        }
        file_info = self.handler.delete_file("kailunfan", "githubApiTest", "src/test_set_file2.txt", data=data)



    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
