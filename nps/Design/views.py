from django.shortcuts import render,redirect
from .models import Design

# Create your views here.
def Designapplicationview(request):
    if request.method == 'POST':
        title = request.POST['title']
        organization = request.POST['organization']
        resource = request.POST['resource']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        r = Design(title=title, organization=organization, resource=resource, referedBy=referedby
                                  , contactnumber=contactnumber, email=emailid)
        r.save()
    else:
         return render(request,"Design/Designapplication.html")

def Designtableview(r):
    return render(r,"Design/Designtable.html")

def Designstatusview(r):
    return render(r,"Design/Designstatus.html")