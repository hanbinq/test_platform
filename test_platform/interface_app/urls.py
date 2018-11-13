from django.urls import path
from interface_app import views


urlpatterns = [
    # case_manage path
    # ex : /interface/case_manage
    # 接口管理
    path('case_manage/', views.case_manage),
    path('debug/', views.debug),
    path('api_debug/', views.api_debug),
]


