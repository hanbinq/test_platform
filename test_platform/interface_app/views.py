import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse



# Create your views here.
def case_manage(request):
    if request.method == "GET":
        return render(request, "case_manage.html", {
            "type": "list"
        })


# 创建/调试接口
def debug(request):
    if request.method == "GET":
        return render(request, "api_debug.html", {
            "type": "debug"
        })


# 调试接口
def api_debug(request):
    if request.method == "POST":
        form = Test
    else:
        return render(request, "api_debug.html", {
            "type": "debug"
        })




