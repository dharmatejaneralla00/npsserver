from django.shortcuts import render,redirect
from .models import Copyright

# Create your views here.
def Copyrighttableview(r):
    c = Copyright.objects.all()
    return render(r,"copyright/Copyrighttable.html",{'c':c})

def Copyrightstatusview(r):
    return render(r,"copyright/Copyrightstatus.html")

def Copyrightapplicationview(request):
    if request.method == 'POST':
        title = request.POST['title']
        organization = request.POST['organization']
        resource = request.POST['resource']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        r = Copyright(title=title, organization=organization, resource=resource, referedBy=referedby
                                  , contactnumber=contactnumber, email=emailid)
        r.save()
    else:
        return render(request,"copyright/Copyrightapplication.html")