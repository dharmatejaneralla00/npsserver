from django.apps import apps
from django.shortcuts import render
from .models import Trademark

# Create your views here.
def Trademarkapplicationview(request):
    referedby = apps.get_model('login', 'referdby')
    if request.method == 'POST':
        categoryofwork = request.POST['categoryofwork']
        clientname = request.POST['clientname']
        titleofwork = request.POST['titleofwork']
        modeofcontact = request.POST['modeofcontact']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        r = Trademark(categoryofwork=categoryofwork, clientname=clientname, titleofwork=titleofwork, modeofcontact=modeofcontact
                                  ,referedby=referedby, contactnumber=contactnumber, email=emailid)
        r.save()
    return render(request,"Trademark/Trademarkapplication.html",{'ref':referedby.objects.all})

def Trademarkstatusview(r,uid):
    c = Trademark.objects.all()
    return render(r,"Trademark/Trademarkstatus.html",{'c':c})

def Trademarktableview(r):
    return render(r,"Trademark/Trademarktable.html")