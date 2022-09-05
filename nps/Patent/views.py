from django.shortcuts import render
from .models import Patentapplication

# Create your views here.
def FullPatentapplicationview(request):
    if request.method == 'POST':
        title = request.POST['title']
        organization = request.POST['organization']
        resource = request.POST['resource']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        r = Patentapplication(title=title, organization=organization, resource=resource, referedBy=referedby
                      , contactnumber=contactnumber, email=emailid)
        r.save()
    else:
         return render(request,"Patent/FullPatentapplication.html")

def Patentapplicationview(request):
    if request.method == 'POST':
        title = request.POST['title']
        organization = request.POST['organization']
        resource = request.POST['resource']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        r = Patentapplication(title=title, organization=organization, resource=resource, referedBy=referedby
                                  , contactnumber=contactnumber, email=emailid)
        r.save()
    else:
          return render(request,"Patent/Patentapplication.html")

def Documentationstatusview(r):
    return render(r,"Patent/Documentationstatus.html")

def Documentationtableview(r):
    return render(r,"Patent/Documentationtable.html")

def Draftingstatusview(r):
    return render(r,"Patent/Draftingstatus.html")

def Draftingtableview(r):
    return render(r,"Patent/Draftingtable.html")

def Drawingstatusview(r):
    return render(r,"Patent/Drawingstatus.html")

def Drawingtableview(r):
    return render(r,"Patent/Drawingtable.html")

def Patentabilitysearchstatusview(r):
    return render(r,"Patent/Patentabilitysearchstatus.html")

def Patentabilitysearchtableview(r):
    return render(r,"Patent/Patentabilitysearchtable.html")

