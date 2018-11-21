from django.urls import path
from interface_app.views import testcase_views, testcase_api


urlpatterns = [
    # case_manage path
    # ex : /interface/case_manage
    # 用例管理
    path('case_manage/', testcase_views.case_manage),
    path('add_case/', testcase_views.add_case),
    path('search_case_name/', testcase_views.search_case_name),
    path("debug_case/<int:cid>/", testcase_views.debug_case),

    # 用例管理  --> 由JS调用的接口
    path('get_project_list/', testcase_views.get_project_list),
    path('api_debug/', testcase_views.api_debug),
    path("api_assert/", testcase_api.api_assert),   # 待完善
    path('save_case/', testcase_views.save_case),
    path("get_case_info/", testcase_views.get_project_list),
]


