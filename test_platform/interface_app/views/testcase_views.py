from django.shortcuts import render
from django.http import HttpResponse
from interface_app.models import TestCase
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# 用例列表
def case_manage(request):
    testcases = TestCase.objects.all().order_by("id")   # 一定要排序，主要是因为取的数据是无序的，Paginator分页会出错
    paginator = Paginator(testcases, 2)

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型，取第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)

    if request.method == "GET":
        return render(request, "case_manage.html", {
            "type": "list",
            "testcases": contacts,
        })
    else:
        return HttpResponse("404")


# 搜索用例的名称
def search_case_name(request):
    if request.method == "GET":
        case_name = request.GET.get('case_name', "")
        cases = TestCase.objects.filter(name__contains=case_name)

        paginator = Paginator(cases, 2)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        return render(request, "case_manage.html", {
            "type": "list",
            "testcases": contacts,
            "case_name": case_name,
        })


# 创建/调试接口  --> 跳转至调试/保存接口页
def add_case(request):

    if request.method == "GET":
        return render(request, "add_case.html", {
            "type": "add"   # 修改，待调试
        })
    else:
        return HttpResponse("404")


# 编辑/调试用例
def debug_case(request, cid):

    if request.method == "GET":
        return render(request, "debug_case.html", {
            "type": "debug"
        })
    else:
        return HttpResponse("404")






