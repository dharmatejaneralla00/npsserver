from django.apps import apps
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from . import models



# Create your views here.


def loginuser(r):
    if not r.user.is_authenticated:
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
                elif team =='drawing':
                    c = apps.get_model('Patent','Patentapplication')
                    ro = c.objects.all()
                    return render(r,'Patent/Drawingtable.html',{'r':ro})
                elif team =='drafting':
                    c = apps.get_model('Patent','Patentapplication')
                    ro = c.objects.all()
                    return render(r,'Patent/Draftingtable.html',{'r':ro})
                elif team =='documentation':
                    c = apps.get_model('Patent','Patentapplication')
                    ro = c.objects.all()
                    return render(r,'Patent/Documentationtable.html',{'r':ro})
                elif team =='noveltysearch':
                    c = apps.get_model('Patent','Patentapplication')
                    ro = c.objects.all()
                    return render(r,'Patent/Patentabilitysearchtable.html',{'r':ro})
                elif team =='trademark':
                    return redirect('trademark/table')
                elif team =='design':
                    return redirect('design/table')
                elif team =='copyright':
                    return redirect('copyright/table')
                else:
                    return redirect('user/login')
            else:
                messages.error(r, "user not found")
            return render(r, 'user/login.html')
    else:
        username = r.user.username
        userModel = models.Usermodel.objects.get(username=username)
        team = userModel.teamname
        if team == 'admin':
            print('admin')
            return redirect('adminpanel')
    return render(r, 'user/login.html')


def registeruser(request):
    context = models.TeamModels.objects.all()
    if request.method == 'POST':
        email = request.POST['username']
        name = request.POST['name']
        password = request.POST['password']
        team = request.POST['team']
        if not User.objects.filter(username=email).exists():
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.save()
            user_auth = authenticate(username=email, password=password)
            login(request, user_auth)
            models.Usermodel(username=email, teamname=team, name=name).save()
            return redirect('user/displayuser')
        else:
            messages.error(request, "email already exists login to continue")
            return redirect('user/register')
    return render(request, 'user/register.html', {'con': context})


def logoutuser(request):
    logout(request)
    return redirect('user/login')


def displayuser(r):
    users = models.Usermodel.objects.all()
    return render(r, 'user/displayuser.html', {'user': users})


def resetpassword(r, username):
    c = username
    if r.method == 'POST':
        newpass = r.POST['password']
        username1 = r.POST['username']
        u = User.objects.get(username=username1)
        u.set_password(newpass)
        u.save()
        messages.success(r, "password reset successfully")
        return redirect('user/displayuser')
    return render(r, 'user/resetpassword.html', {'c': c})


def referedby(r):
    c = models.referdby.objects.all()
    if r.method == "POST":
        name = r.POST['names']
        r = models.referdby(names=name)
        r.save()
        return render(r, 'user/refered.html', {'c': c})
    return render(r, 'user/refered.html', {'c': c})
