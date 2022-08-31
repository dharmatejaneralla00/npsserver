from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


# Create your views here.


def loginUser(r):
    if r.method == 'POST':
        username = r.POST['username']
        password = r.POST['password']
        user = authenticate(username = username,password =password )
        if user:
            login(r,user)
            return render(r,"")
        else:
            messages.error(r,"user not found")
    return render(r,'user/login.html')

def registerUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        if not User.objects.filter(username = email).exists():
            user = User.objects.create_user(username=email,email=email,password=password)
            user.first_name = name
            user.save()
            user_auth = authenticate(username = email,password = password)
            login(request,user_auth)
            return  redirect('home')
        else:
            messages.error(request,"email already exists login to continue")
            return render(request,'account/login.html')
    return render(request,'user/register.html')
def logoutUser(request):
    logout(request)
    return redirect('login')