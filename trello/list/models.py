from django.db import models
from .fields import OrderField

class List(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateField(unique=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.created)

class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['list'])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

