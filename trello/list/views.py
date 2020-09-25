from django.shortcuts import render
from .models import List, Task
from datetime import date, timedelta
from braces.views import CsrfExemptMixin, JSONRequestResponseMixin
from django.views.generic.base import View

def get_tasks(request):
    today = date.today()
    first = Task.objects.filter(list__created=today).order_by('order')
    second = Task.objects.filter(list__created=today + timedelta(1)).order_by('order')
    third = Task.objects.all()
    fourth = Task.objects.all()
    return render(request, 'tasklist.html', { 'first': first, 'second': second})

class TaskListOverwrite(CsrfExemptMixin, JSONRequestResponseMixin, View):
    def post(self, request):
        print(self.request_json.items())
        return self.render_json_response({'saved': 'OK'})