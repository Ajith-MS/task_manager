from django.urls import path
from .views import display_home, add_task, delete_task, view_single_task, update_task  #get_time, sum_two_numbers, task_list,
app_name = 'todoapp'
urlpatterns =[
    path("", display_home, name="homepage"),
    path("viewsingletask/<int:id>", view_single_task, name="view_single_task"),
    path("addtask/", add_task, name="add_task"),
    path("delete/<int:id>", delete_task, name="deletetask"),
    path("viewsingletask/delete/<int:id>", delete_task),
    path("addtask/viewsingletask/<int:id>", view_single_task),
    path("update/<int:id>", update_task, name="updatetask"),
    path("viewsingletask/update/<int:id>", update_task),

    # path(""),
    # path("listtask/delete/<int:id>", delete_task),
    # path("/viewsingletask/delete/<int:id>", delete_task),
    # path("create_task.html/", ),
    # path("gettime/", get_time),
    # path('sum/', sum_two_numbers),
    # path("listtask/", task_list),
]
