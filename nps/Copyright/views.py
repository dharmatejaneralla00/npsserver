from django.shortcuts import render, redirect
from .models import Copyright

# Create your views here.
def Copyrighttableview(r):
    c = Copyright.objects.all()
    return render(r,"copyright/Copyrighttable.html",{'c':c})

def Copyrightstatusview(r,uid):
    return render(r,"copyright/Copyrightstatus.html")

def Copyrightapplicationview(request):
    if request.method == 'POST':
        categoryofwork = request.POST['title']
        clientname = request.POST['organization']
        titleofwork = request.POST['resource']
        referedby = request.POST['referedby']
        modeofcontact = request.POST['contactnumber']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        r = Copyright(categoryofwork=categoryofwork, clientname=clientname, titleofwork=titleofwork, referedBy=referedby
                                  ,modeofcontact=modeofcontact, contactnumber=contactnumber, email=emailid)
        r.save()
        return redirect('home')
    else:
        return render(request,"copyright/Copyrightapplication.html")