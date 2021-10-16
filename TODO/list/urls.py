from django.urls import path
from . import views

app_name = "list"

urlpatterns = [
    path("home/",views.home,name="home"),
    path("add-item/",views.addItem,name="add-item"),
    path("delete/<int:id>",views.deleteTask,name="delete-task")
]