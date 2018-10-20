from django.urls import path
from . import views


urlpatterns = [
    # project_manage path
    # ex : /manage/project_manage
    path('project_manage/', views.project_manage),
    path('add_project/', views.add_project),
    path('edit_project/<int:pid>/', views.edit_project),
    path('delete_project/<int:pid>/', views.delete_project),
]


