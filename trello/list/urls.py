from django.urls import path
from . import views

app_name = 'list'

urlpatterns = [
    path('', views.get_tasks, name='all_tasks')
]