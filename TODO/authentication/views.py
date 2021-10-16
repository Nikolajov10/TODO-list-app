from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import RegUsers
from django.contrib import messages
from TODO.user import User
from django.urls import reverse


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        find_user = RegUsers.objects.filter(username=username,password=password)
        if len(find_user) == 0:
            messages.add_message(request,messages.ERROR,"Username or password incorect!")
        else:
            User.login(username)
            messages.add_message(request,messages.SUCCESS,"Loged in successfully")
            return redirect(reverse('list:home'))
    return render(request,"login.html",{'user': User.getUser() })

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        conf_password = request.POST.get("password2")
        if len(username) <= 2:
            messages.add_message(request,messages.ERROR,"Too short username")
        if len(password) <= 3:
            messages.add_message(request,messages.ERROR,"Too short password")
        if password != conf_password:
            messages.add_message(request,messages.ERROR,"Passwords don't match")
        try:
            user = RegUsers(username=username,email=email,password=password)
            user.save()
            User.login(username)
            messages.add_message(request,messages.SUCCESS,"Sign up successfully")
            return redirect(reverse('list:home'))
        except Exception as e:
            messages.add_message(request,messages.ERROR,"Username or email already exist!")
    return render(request,"sign-up.html",{"user":User.getUser()})

def logout(request):
    if not User.isLoged():
        return redirect(reverse('authentication:login'))
    User.logout()
    return render(request,"logout.html",{"user":User.getUser()})
