from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
   path("", views.index, name="index"),
   path("add", views.add_task, name="add_task"),
   path("edit/<int:id>/", views.editing, name="editing"),
   path("deleting/<int:id>/", views.deleting, name="deleting")
]

