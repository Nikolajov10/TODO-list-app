from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path("login/",views.login,name="login"),
    path("",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("sign-up/",views.sign_up,name="sign-up"),
]
