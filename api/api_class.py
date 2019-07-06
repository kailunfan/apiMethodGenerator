import requests
import logging
import json
from .api_meta_class import APIMetaClass
from config import api_config, response, log


class API(metaclass=APIMetaClass):
    """
    以APIMetaClass为元类,加载api_config.api数据,生成方法.
    """
    __doc__ = json.dumps(api_config.api, ensure_ascii=False, indent=2)
    base_url = api_config.base_url
    api = api_config.api

    def __init__(self, token=None):
        self.header = {"Content-Type": "application/json"}
        if token:
            self.header['Authorization'] = "token {}".format(token)

    def _request(self, method, url, data, *args):
        try:
            if not isinstance(data, str):
                data = json.dumps(data)
            r = requests.request(method, url, data=data, headers=self.header)
        except IOError:
            r = response.ConnectError()
        return self._check_response(r, *args)

    @staticmethod
    def _check_response(res, *args):
        """
        1. 检查响应,记录日志;
        2. 此处根据返回值格式不同作出更改;github api出错后返回值会有message键表示错误原因,这里讲其记录;
        """
        status_code = res.status_code
        content = res.json()

        if str(status_code).startswith("2"):
            logging.info('{}, status_code: {}'.format(args, status_code))
        else:
            logging.error('{}, status_code: {}, message:{}'.format(
                args, status_code, content.get('message', '').replace('\n', '')))

        return res.json()
