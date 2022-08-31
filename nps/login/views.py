from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . import models
# Create your views here.


def loginUser(r):
    if not r.user.is_authenticated:
        if r.method == 'POST':
            username = r.POST['username']
            password = r.POST['password']
            user = authenticate(username = username,password =password )
            if user:
                login(r,user)
                userModel = models.Usermodel.objects.get(username = username)
                team = userModel.teamname
                if team == 'admin':
                    return render(r,'adminpanel/')
            else:
                messages.error(r,"user not found")
    else:
        return
    return render(r,'user/login.html')

def registerUser(request):
    context = models.TeamModels.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        team = request.POST['team']
        if not User.objects.filter(username = email).exists():
            user = User.objects.create_user(username=email,email=email,password=password)
            user.first_name = name
            user.save()
            user_auth = authenticate(username = email,password = password)
            login(request,user_auth)
            models.Usermodel(username = email,team = team).save()
            return  redirect('home')
        else:
            messages.error(request,"email already exists login to continue")
            return redirect('user/register')
    return render(request,'user/register.html',{'con':context})
def logoutUser(request):
    logout(request)
    return redirect('login')