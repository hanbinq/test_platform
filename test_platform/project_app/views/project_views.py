from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from project_app.forms import ProjectForm


@login_required
def project_manage(request):
    """
    项目列表管理
    :param request:
    :return:
    """
    username = request.session.get('user', '')   # 读取浏览器session
    # project_all = Project.objects.order_by("-create_time")   # 按照创建时间倒序排列
    project_all = Project.objects.all()
    return render(request, "project_manage.html", {"user": username,
                                                   "projects": project_all,
                                                   "type": "list"})


@login_required
def add_project(request):
    """
    添加项目
    :param request:
    :return:
    """
    if request.method == "POST":
        form = ProjectForm(request.POST)
        # 判断表单是否有效
        if form.is_valid():
            # 已验证的表单数据将被放到form.cleaned_data字典中，这里的数据已经很好的转化为python类型。
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            Project.objects.create(name=name, describe=describe, status=status)
            return HttpResponseRedirect('/manage/project_manage/')
    else:
        form = ProjectForm()

    return render(request, 'project_manage.html', {
        'form': form,
        "type": "add",
    })


@login_required
def edit_project(request, pid):
    """
    编辑/修改项目
    :param request:
    :param pid:
    :return:
    """
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            model = Project.objects.get(id=pid)
            model.name = form.cleaned_data['name']
            model.describe = form.cleaned_data['describe']
            model.status = form.cleaned_data['status']
            model.save()
            return HttpResponseRedirect('/manage/project_manage/')

    else:
        if pid:
            # instance属性，表示与它绑定的模型实例
            form = ProjectForm(
                instance=Project.objects.get(id=pid)  # 赋值instance可以使form表单是可以接受对象的数据
            )
        else:
            form = ProjectForm()

    return render(request, 'project_manage.html', {
        'form': form,
        "type": "edit",
    })


@login_required
def delete_project(request, pid):
    """
    删除项目
    :param request:
    :param pid:
    :return:
    """
    Project.objects.get(id=pid).delete()
    return HttpResponseRedirect("/manage/project_manage/")



