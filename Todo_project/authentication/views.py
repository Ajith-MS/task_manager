from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
# from django.contrib.

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "you have successfully logged in!")
            return redirect('todoapp:homepage')
        else:
            messages.error(request, "Invalid username or password")
            # import pdb
            # pdb.set_trace()
            # return render("homelogin", {"user": user})
    return render(request, 'login.html')


def home(request):
    return render(request, "homelogin.html")


def registration(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password:
            User.objects.create_user(username=username, first_name=firstname, email=email, password=password)
            return redirect('authentication:login')
        else:
            messages.error(request, "Password and confirm password dosen't match")
    return render(request, "Registration.html")
    # return redirect('homelogin')


def logout_user(request):
    logout(request)
    return redirect('login')
