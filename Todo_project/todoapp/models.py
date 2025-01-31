from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Task(models.Model):
    task_title = models.CharField(max_length=30, null=True)
    task_complete = models.BooleanField(default=False, null=True)
    task_description = models.CharField(max_length=5000, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # date = models.DateTimeField(default="30-01-2025")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.task_title
