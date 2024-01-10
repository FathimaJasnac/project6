from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def logout(request):
    auth.logout(request)
    return redirect('clgapp:index')


def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpswd = request.POST['confirm password']
        if password == cpswd:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register_app:reg')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('register_app:login')

        else:
            messages.info(request, "password not matching")
            return redirect('register_app:reg')
        return redirect('/')
    return render(request, "register.html")



def login(request):
    if request.method== 'POST':
        uname=request.POST['username']
        pswd=request.POST['password']
        user=auth.authenticate(username=uname,password=pswd)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid registration")
            return redirect('register_app:login')
    return render(request,"login.html")
