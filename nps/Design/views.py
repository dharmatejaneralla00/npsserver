from django.shortcuts import render, redirect
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
        return redirect('users/login')
    else:
         return render(request,"Design/Designapplication.html")

def Designtableview(r):
    c = Design.objects.all()
    return render(r,"Design/Designtable.html",{'c':c})

def Designstatusview(r,uid):
    design= Design.objects.get(uid = uid)
    return render(r,"Design/Designstatus.html",{'des':design})