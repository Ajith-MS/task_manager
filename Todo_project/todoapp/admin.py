from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ("id","task_title", "user")
    fields = ("task_title", "task_complete", "task_description", "user")
admin.site.register(Task, TaskAdmin)

