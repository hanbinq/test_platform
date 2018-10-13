from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Project, Module


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
            return HttpResponseRedirect('/project_manage/')
        else:
            return render(request, "index.html",
                          {"error": "用户名或密码错误"})


@login_required
def project_manage(request):
    username = request.session.get('user', '')   # 读取浏览器session
    project_all = Project.objects.all()

    return render(request, "project_manage.html", {"user": username,
                                                   "projects": project_all})


def logout(request):
    auth.logout(request)   # 调用自带的方法，清除用户登录状态
    response = HttpResponseRedirect('/')
    return response
