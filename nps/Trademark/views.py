from django.shortcuts import render
from .models import Trademark

# Create your views here.
def Trademarkapplicationview(request):
    if request.method == 'POST':
        title = request.POST['title']
        organization = request.POST['organization']
        resource = request.POST['resource']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        r = Trademark(title=title, organization=organization, resource=resource, referedBy=referedby
                                  , contactnumber=contactnumber, email=emailid)
        r.save()
    return render(request,"Trademark/Trademarkapplication.html")

def Trademarkstatusview(r,uid):
    c = Trademark.objects.all()
    return render(r,"Trademark/Trademarkstatus.html",{'c':c})

def Trademarktableview(r):
    return render(r,"Trademark/Trademarktable.html")