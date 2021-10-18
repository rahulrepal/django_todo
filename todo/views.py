from django.shortcuts import render

def home(request):
    return render(request, template_name="home/home.html", context={"title": "Just todo it"})