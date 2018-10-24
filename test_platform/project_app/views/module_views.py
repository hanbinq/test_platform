from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Module
from project_app.forms import ModuleForm


@login_required
def module_manage(request):
    """
    模块列表管理
    :param request:
    :return:
    """
    username = request.session.get('user', '')
    module_all = Module.objects.all()
    return render(request, "module_manage.html", {
        "user": username,
        "modules": module_all,
        "type": "list"
    })


@login_required
def add_module(request):
    """
    添加模块
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            project = form.cleaned_data['project']
            Module.objects.create(
                name=name, describe=describe, project=project)
            return HttpResponseRedirect('/manage/module_manage/')
    else:
        form = ModuleForm()

    return render(request, 'module_manage.html', {
        'form': form,
        "type": "add",
    })


def edit_module(request, mid):
    """
    编辑模块
    :param request:
    :param mid:
    :return:
    """
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            module = Module.objects.get(id=mid)
            module.name = form.cleaned_data['name']
            module.describe = form.cleaned_data['describe']
            module.project = form.cleaned_data['project']
            module.save()
            return HttpResponseRedirect('/manage/module_manage/')
    else:
        if mid:
            form = ModuleForm(
                instance=Module.objects.get(id=mid)
            )
    return render(request, 'module_manage.html', {
        'form': form,
        "type": "edit",
    })


@login_required
def delete_module(request, mid):
    """
    删除模块
    :param request:
    :param mid:
    :return:
    """
    Module.objects.get(id=mid).delete()
    return HttpResponseRedirect("/manage/module_manage")




