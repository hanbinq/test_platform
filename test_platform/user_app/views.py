from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth


# 主要代码逻辑
def index(request):
    return render(request, "index.html")


# 处理登录请求
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = auth.authenticate(username=username, password=password)

        if username == "" or password == "":
            return render(request, "index.html",
                          {"error": "用户名或者密码为空"})
        elif user is not None:
            auth.login(request, user)  # 记录用户的登录状态
            request.session['user'] = username  # 将session信息记录到浏览器
            return HttpResponseRedirect('/manage/project_manage/')
        else:
            return render(request, "index.html",
                          {"error": "用户名或密码错误"})


def logout(request):
    auth.logout(request)   # 调用自带的方法，清除用户登录状态
    response = HttpResponseRedirect('/')
    return response


"""
应用划分
user_app 用户登录、密码修改，基于用户的用例展示
project_app 项目和模块
interface_app 接口用例，测试任务
tools_app 测试工具
"""