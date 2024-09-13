from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Todo
from .forms import TodoForm


def home(request):
    todos = Todo.objects.all()
    form = TodoForm()
    context = {
        "todos": todos,
        "form": form,
    }
    return render(request, "index.html", context)


@require_http_methods(["POST"])
def add(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo_select = form.save(commit=False)
        todo_select.save()
    return redirect("/")


def edit(request, todo_id):
    todo = Todo.objects.filter(id=todo_id)[0]
    if todo:
        todo.done = not todo.done
        todo.save()
    return redirect("/")


def delete(request, todo_id):
    todo = Todo.objects.filter(id=todo_id)[0]
    if todo:
        todo.delete()
    return redirect("/")
