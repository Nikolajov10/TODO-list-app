from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from TODO.user import User
from .models import Task
import datetime
# Create your views here.

def home(request):
    if not User.isLoged(): return redirect('authentication:login')
    tasks = Task.objects.filter(username=User.getUser().name)
    priority_val = {
        "High":0,"Medium":1,"Low":2
    }
    tasks = sorted(tasks,key=lambda x:priority_val[x.priority])
    date = datetime.date.today()
    date_diffs = []
    context = {
        "user":User.getUser(),
        "tasks":tasks,
        "today":date,
    }
    for index,task in enumerate(tasks):
        task.setDiff((task.due_date - date).days)
    return render(request,"list_home.html",context)

def addItem(request):
    if not User.isLoged(): return redirect('authentication:login')
    if request.method == "POST":
        desc = request.POST.get("desc")
        due = request.POST.get("due")
        priority = request.POST.get("priority")
        title= request.POST.get("title")
        if len(desc) == 0:
            messages.add_message(request,messages.ERROR,"Enter description!")
        elif not due:
            messages.add_message(request,messages.ERROR,"Enter due date!")
        elif not priority:
            messages.add_message(request,messages.ERROR,"Enter prirority!")
        else:
            task = Task(username=User.getUser().name,description=desc,due_date=due,priority=priority,title=title)
            task.save()
    return render(request,"add_item.html",{"user":User.getUser()})

def deleteTask(request,id:int):
    Task.objects.filter(id=id).delete()
    return redirect("list:home")