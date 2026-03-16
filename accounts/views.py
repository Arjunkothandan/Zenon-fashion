from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect("main")
    else:
        form = SignupForm()

    return render(request,"signup.html",{"form":form})


def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')   # redirects to main.html page

        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")



def user_logout(request):
    logout(request)
    return redirect("landing")
