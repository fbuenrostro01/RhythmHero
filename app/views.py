from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages




from app.models import *



# Create your views here.

def login_func(request):
    return render(request,"login.html")


def register_func(request):
    form=CreateUserForm()
   

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get("username")
            messages.success(request,"Account Created"+user)
            return redirect("game_page")

    context={'form':form}

    return render(request,"register.html",context)

def game_func(request):

    return render(request,"Game.html")
    

