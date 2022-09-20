from django.apps import apps
from django.shortcuts import render, redirect
from .models import Copyright

# Create your views here.
def Copyrighttableview(r):
    c = Copyright.objects.all()
    return render(r,"copyright/Copyrighttable.html",{'c':c})

def Copyrightstatusview(r,uid):
    return render(r,"copyright/Copyrightstatus.html")

def Copyrightapplicationview(request):
    referedby = apps.get_model('login', 'referdby')
    if request.method == 'POST':
        categoryofwork = request.POST['categoryofwork']
        clientname = request.POST['clientname']
        titleofwork = request.POST['titleofwork']
        referedby = request.POST['referedby']
        modeofcontact = request.POST['modeofcontact']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        r = Copyright(categoryofwork=categoryofwork, clientname=clientname, titleofwork=titleofwork, referedBy=referedby
                                  ,modeofcontact=modeofcontact, contactnumber=contactnumber, email=emailid)
        r.save()
        return redirect('home')
    else:
        return render(request,"copyright/Copyrightapplication.html",{'ref':referedby.objects.all})