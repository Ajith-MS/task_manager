from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth.models import User
from datetime import datetime



# Create your views here.

# def get_time(request):
#     return HttpResponse(f"""<html><body style='background:powderblue'><br><br>
#     <center><h1 style='color:red'>Your Current time</h1></center>
#     <center><p>your time is :{datetime.now().time()}</p></center></body></html>""")


# def sum_two_numbers(request):
#     # import pdb
#     # pdb.set_trace()
#     try:
#         a = int(request.GET.get('x', default=0))
#         b = int(request.GET.get('y', default=0))
#         return HttpResponse(f"sum of numbers: {a + b}")
#     except Exception as e:
#         return HttpResponse(f"Error: {e}")

@login_required(login_url='authentication:login')
def display_home(request):
    # return HttpResponse(request.method)
    # import pdb
    # pdb.set_trace()
    task_lst = Task.objects.filter(user=request.user).values()
    return render(request, "home.html", {"task_list": task_lst})

@login_required(login_url='authentication:login')
def add_task(request):
    # import pdb
    # pdb.set_trace()
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        task_complete = request.POST.get('task_complete')
        task_description = request.POST.get('task_description')
        if task_title:
            Task.objects.create(task_title=task_title, task_complete=task_complete, task_description=task_description, user=request.user)
            messages.success(request, "Record added successfully")
            return redirect('todoapp:homepage')
        else:
            messages.success(request, "Task is Empty!!")
    task_lst = Task.objects.all()
    return render(request, "create_task.html", {"task_list": task_lst})

#
# def task_list(request):
#     try:
#         task = Task.objects.filter(user=request.user).values()
#         return render(request, "view_tasks.html", {"task_lst": task})
#     except Exception as e:
#         return HttpResponse(f"Error: {e}")

@login_required(login_url='authentication:login')
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request, "Record deleted successfully")
    return redirect("todoapp:homepage")

@login_required(login_url='authentication:login')
def view_single_task(request, id):
    task = Task.objects.get(id=id)
    return render(request, "view_single_task.html", {"task_list": task})

@login_required(login_url='authentication:login')
def update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task_title = request.POST.get("task_title")
        task_complete = request.POST.get("task_complete")
        task_description = request.POST.get("task_description")
        task.task_title = task_title
        task.task_complete = task_complete
        task.task_description = task_description
        task.save()
        return redirect("todoapp:homepage")
    return render(request, "update.html", {"task": task})
