base_url = "https://api.github.com"

# 需要动态生成方法的类名
gen_func_class_names = ["API"]

# 根据api方法名首个单词确定http请求方法
keywords = {
    "get": ["get"],
    "post": ["post", "add", "create"],
    "put": ["update", "modify", "set"],
    "delete": ["delete"]
}

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
