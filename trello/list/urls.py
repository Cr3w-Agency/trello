from django.urls import path
from . import views

app_name = 'list'

urlpatterns = [
    path('orders_overwrite/', views.TaskListOverwrite.as_view(), name='orders_overwrite'),
    path('', views.get_tasks, name='all_tasks'),
]