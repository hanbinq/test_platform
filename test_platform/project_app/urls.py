from django.urls import path
from . import views


urlpatterns = [
    # project_manage path
    # ex : /manage/project_manage
    path('project_manage/', views.project_manage),
]


