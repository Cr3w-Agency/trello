from django.shortcuts import render
from .models import List, Task
from datetime import date, timedelta
from braces.views import CsrfExemptMixin, JSONRequestResponseMixin
from django.views.generic.base import View
from datetime import datetime

def get_tasks(request):
    today = date.today() + timedelta(0)
    tomorrow = today + timedelta(1)
    third_day = today + timedelta(2)
    fourth_day = today + timedelta(3)
    first_list = List.objects.get(created=today).pk
    second_list = List.objects.get(created=tomorrow).pk
    first_tasks = Task.objects.filter(list__created=today).order_by('order')
    second_tasks = Task.objects.filter(list__created=tomorrow).order_by('order')
    third = Task.objects.all()
    fourth = Task.objects.all()
    return render(request, 'tasklist.html', { 'first_tasks': first_tasks,
                                              'second_tasks': second_tasks,
                                              'first_list': first_list,
                                              'second_list': second_list})

class TaskListOverwrite(CsrfExemptMixin, JSONRequestResponseMixin, View):
    def post(self, request):
        list = List.objects.get(pk=self.request_json['list'])
        tasks = self.request_json['tasks']
        for key, value in tasks.items():
            task = Task.objects.get(pk=key)
            task.order = value
            task.list = list
            task.save()
        return self.render_json_response({'saved': 'OKs)'})