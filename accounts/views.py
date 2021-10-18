from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=email,password=password)
        if user:
            login(request,user)
            return redirect("/")
        else:
            messages.error(request,"Wrong email or password, please try again ")

    return render(request,template_name="login.html",context={
        "title":"Log In - just todo it"
    })


def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password1"]

            user = User(username=email,first_name=first_name,last_name=last_name,email=email,password=make_password(password))
            user.save()
            return redirect("/account/login/")
        else:
            return render(request, template_name="register.html", context={
                "title":"Register - just todo it",
                "form": form
            })

    return render(request,template_name="register.html",context={
        "title":"Register - just todo it",
        "form":form
    })

def logoutUser(request):
    if not request.user.is_authenticated:
        return redirect('/account/login')
    logout(request)
    return redirect('/')