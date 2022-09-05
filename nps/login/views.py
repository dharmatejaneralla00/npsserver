from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from . import models


# Create your views here.


def loginuser(r):
    # if not r.user.is_authenticated:
        if r.method == 'POST':
            username = r.POST['username']
            password = r.POST['password']
            print(username)
            user = authenticate(username=username, password=password)
            if user:
                print(username)
                login(r, user)
                userModel = models.Usermodel.objects.get(username=username)
                team = userModel.teamname
                if team == 'admin':
                    print('admin')
                    return redirect('adminpanel')
            else:
                messages.error(r, "user not found")
        return render(r, 'user/login.html')


def registeruser(request):
    context = models.TeamModels.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        team = request.POST['team']
        if not User.objects.filter(username=email).exists():
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.save()
            user_auth = authenticate(username=email, password=password)
            login(request, user_auth)
            models.Usermodel(username=email, team=team, name=name).save()
            return redirect('home')
        else:
            messages.error(request, "email already exists login to continue")
            return redirect('user/register')
    return render(request, 'user/register.html', {'con': context})


def logoutuser(request):
    logout(request)
    return redirect('login')


def displayuser(r):
    users = models.Usermodel.objects.all()
    return render(r, 'user/displayuser.html', {'user': users})


def resetpassword(r, username):
    if r.method == 'POST':
        user = User.objects.get(username=username)
        newpass = r.POST['password']
        user.set_password(newpass)
        user.save()
        messages.success(r, "password reset successfully")
        return redirect('users/')
    return render(r, 'users/resetpassword.html')
