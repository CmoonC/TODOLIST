from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Tasks
# Create your views here.


class NewTaskForm(forms.Form):
    name = forms.CharField(label="Name your task")
    description = forms.CharField(label="Tell more about task")


def index(request):
    # if "list_of_tasks" not in request.session:
    #     request.session["list_of_tasks"] = []
    print(Tasks.objects.all())
    return render(request, 'habbit/index.html',
                  {
                      "list_of_tasks": Tasks.objects.all()
                      # "list_of_tasks": request.session["list_of_tasks"]
                  })


def add_task(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task = Tasks(name = form.cleaned_data["name"], description = form.cleaned_data["description"])
            new_task.save()
            # request.session["list_of_tasks"] += [name]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, 'habbit/add.html', {
                "form": form
            })
    return render(request, 'habbit/add.html', {
        "form": NewTaskForm()
    })


def editing(request, id):
    task = get_object_or_404(Tasks, id=id)

    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task.name = form.cleaned_data["name"]
            task.description = form.cleaned_data["description"]
            task.save()
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, 'habbit/edit.html', {
                "form": form,
                "task": task
            })
    return render(request, 'habbit/edit.html', {
        "form": NewTaskForm(initial={'name': task.name, 'description': task.description}),
        "task": task
    })


def deleting(request, id):
    task = get_object_or_404(Tasks, id=id)
    Tasks.delete(task)
    return HttpResponseRedirect(reverse("tasks:index"))