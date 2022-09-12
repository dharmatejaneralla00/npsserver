from django.shortcuts import render
from django.apps import apps


# Create your views here.

def adminpanel(r):
    patent = apps.get_model('Patent', 'Patentapplication')
    status = apps.get_model('Patent','ApplicationStatus')
    return render(r, "admin/admin.html", {'con': patent.objects.all()})


def Editapplication(r, uid):
    patent = apps.get_model('Patent', 'Patentapplication')
    patent = patent.objects.get(uid = uid)
    status = apps.get_model('Patent','ApplicationStatus')
    return render(r, 'Patent/editappliaction.html', {'app': patent,'status':status.objects.get(uid = uid)})
