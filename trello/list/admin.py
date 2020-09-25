from django.contrib import admin
from .models import List, Task

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['list', 'title', 'created']
