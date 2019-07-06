# apiMethodGenerator

通过元编程的方式将一个 dict 形式的配置文件转化为一组 api 方法.
本例为 github 提供的开放接口,配置文件如下:

```python
base_url = "https://api.github.com"

# github api
api = {
    "users": {
        "get_user_info": "{user_name}" # 获取用户信息
    },
    "repos": {
        "get_repo": "{user_name}/{repo_name}",                                      # 获取仓库信息
        "get_contents": "{user_name}/{repo_name}/contents",                         # 获取仓库内容
        "set_file": "{user_name}/{repo_name}/contents/{path}",                      # 添加/修改文件
        "delete_file": "{user_name}/{repo_name}/contents/{path}",                   # 删除文件
        "get_contents_in_dir": "{user_name}/{repo_name}/contents/{dir_name}",       # 获取文件夹中文件列表
        "get_commits": "{user_name}/{repo_name}/commits",                           # 获取提交列表
        "get_commit": "{user_name}/{repo_name}/commits/{commit_RSA}",               # 获取一次提交的详细信息
        "get_issuess": "{user_name}/{repo_name}/issues?state={state:open}",         # 获取issuess列表
        "get_issue": "{user_name}/{repo_name}/{issue_NO}",                          # 获取一个issue详情
    }
}
```

之后便可以使用上述定义的 key 作为方法名调用,例如:

```python
from api.api_class import API

handler = API(token='***')
user_info = handler.get_user_info('kailunfan')
repo_info = handler.get_repo('kailunfan', 'githubApiTest')

# 需要传入payload时用data接收
data = {
    "message": "new file",
    "content": base64.b64encode("this is the original content!".encode()).decode()
}
file_info = handler.set_file("kailunfan", "githubApiTest", "src/test_set_file2.txt", data=data)
```

## API 配置文件说明

- 所有的 API 方法在 `config/api_config.py` 文件中定义, 在创建类时动态生成;
- 以上述配置文件中`get_issuess`为例:
  - 字典 api 中一级 key 和二级 key 共同组成请求 url;
  - 通过方法名`get_issuess`推断出HTTP请求方法为`get`;
  - {user_name}和{repo_name}表示位置参数,调用的时候需按顺序传入;
  - {state:open} 表示关键字参数;
  - 调用传参如下: `handler.get_issuess("kailunfan", "githubApiTest", state="closed")`
- 需要传入payload时用data关键字接收,类型为dict.
