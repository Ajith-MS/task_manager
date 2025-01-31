from django.urls import path
from .views import user_login, registration, home, logout_user
app_name = 'authentication'
urlpatterns =[
    path("", user_login, name="login"),
    path("registration/", registration, name="registration"),
    path("homelogin/", home, name="homelogin"),
    path("logout/", logout_user, name="logout"),
    # path("homelogin/", login, name="homelogin"),
    # path("login/registration/", registration, name="login_registration"),

]
