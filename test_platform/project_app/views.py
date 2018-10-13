from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project


@login_required
def project_manage(request):
    """
    项目列表管理
    :param request:
    :return:
    """
    username = request.session.get('user', '')   # 读取浏览器session
    project_all = Project.objects.all()
    return render(request, "project_manage.html", {"user": username,
                                                   "projects": project_all})


