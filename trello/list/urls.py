from django.urls import path
from . import views

app_name = 'list'

urlpatterns = [
    path('overwrite/', views.TaskListOverwrite.as_view(), name='overwrite'),
    path('', views.get_tasks, name='all_tasks'),
]