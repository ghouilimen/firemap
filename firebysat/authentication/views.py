from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .forms import LoginForm


def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST' :
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form' : form})

def user_login(request):
    if request.method == 'POST' :
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request, username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse(" <h1> Disable account </h1>")
            else:
                return HttpResponse("<h1> Invalid login </h1>")
        
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form})
