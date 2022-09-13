from django.shortcuts import render, redirect
from django.apps import apps


# Create your views here.

def adminpanel(r):
    patent = apps.get_model('Patent', 'Patentapplication')
    return render(r, "admin/admin.html", {'con': patent.objects.all()})


def Editapplication(r, uid):
    patent = apps.get_model('Patent', 'Patentapplication')
    patent = patent.objects.get(uid=uid)
    paymentstatus = apps.get_model('Patent','PaymentStatus')
    nda = apps.get_model('Patent', 'NDAStatus')
    return render(r, 'Patent/editappliaction.html', {'app': patent, 'paymentstatus':paymentstatus.objects.get(uid=uid)})

def ndsatatus(r,uid):
    nda = apps.get_model('Patent','NDAStatus')
    if r.method == 'POSt':
        status = r.POST['status']
        nda(status = True,uid = uid,nda = status).save()
        return redirect('editapplication/'+uid)

def dashboard(r):
    return  redirect()