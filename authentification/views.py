from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from main.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def log(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)

        user = authenticate(request, username=user.username, password=password)
        print('------------------------------------------------')
        print(user)
        print('------------------------------------------------')
        print('------------------------------------------------')
        # user = User.objects.get(email=email)

        if(user):
            login(request, user)
            return render(request, 'main/index.html')

    return render(request, 'auth/login.html')

def unlog(request):
    logout(request)
    return redirect('index')


def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if(str(password) == str(confirm_password)):
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            return redirect('index')

    return render(request, 'auth/register.html')
