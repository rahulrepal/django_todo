from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Todo
from .forms import AddTodoForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="/account/login")
def todos(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request,template_name="todos.html",context={
        "todos":todos,
        "title":"Todos",
        "first_name":request.user.first_name
    })

@login_required(login_url="/account/login")
def add_todo(request):
    form = AddTodoForm()
    if request.method == "POST":
        form = AddTodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user_id = request.user.id
            todo.save()
            return redirect("/todos/")
        else:
            return render(request,"add_todo.html",context={
                "form":form,
                "title":"Add todo"
            })
    return render(request,"add_todo.html",context={
            "form":form,
            "title":"Add todo"
    })

@login_required(login_url="/account/login")
def delete_todo(request,id):
    todo = Todo.objects.get(pk=id)
    todo.delete()
    messages.success(request,"Successfuly delete todo")
    return redirect("/todos/")

