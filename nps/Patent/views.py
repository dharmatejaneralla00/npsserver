import random

from django.shortcuts import render, redirect
from .models import Patentapplication, NDAStatus, PaymentStatus, NoveltyStatus, DocumentationStatus, DrawingStatus, \
    DraftingStatus, FerStatus, ExaminationSatus, FilingStatus, HearingStatus, GrantsStatus


def random_string(ReferedBy):
    unique_id = ReferedBy[0:2] + "".join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
    return unique_id


# Create your views here.
def FullPatentapplicationview(request):
    if request.method == 'POST':
        title = request.POST['title']
        organization = request.POST['organization']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        modeofcontact = request.POST['modeofcontact']
        uid = random_string(referedby)
        r = Patentapplication(title=title, uid=uid, organisation=organization, referedby=referedby
                              , conntactnumber=contactnumber, emailid=emailid, modeofcontact=modeofcontact,
                              patenttype='full', status=False)
        r.save()
        NDAStatus(uid=uid, status=False).save()
        NoveltyStatus(uid=uid, status=False).save()
        DraftingStatus(uid=uid, status=False).save()
        DrawingStatus(uid=uid, status=False).save()
        DocumentationStatus(uid=uid, status=False).save()
        FilingStatus(uid=uid, status=False).save()
        ExaminationSatus(uid=uid, status=False).save()
        FerStatus(uid=uid, status=False).save()
        HearingStatus(uid=uid, status=False).save()
        GrantsStatus(uid=uid, status=False).save()
        PaymentStatus(uid=uid, status=False).save()
        return redirect('home')
    return render(request, "Patent/FullPatentapplication.html")


def Patentapplicationview(request):
    if request.method == 'POST':
        title = request.POST['title']
        type = request.POST['check[]']
        organization = request.POST['organization']
        referedby = request.POST['referedby']
        contactnumber = request.POST['contactnumber']
        emailid = request.POST['emailid']
        modeofcontact = request.POST['modeofcontact']
        uid = random_string(referedby)
        r = Patentapplication(uid=uid, title=title, organisation=organization, referedby=referedby
                              , conntactnumber=contactnumber, emailid=emailid, modeofcontact=modeofcontact,
                              patenttype=type)
        r.save()
        NDAStatus(uid=uid, status=False).save()
        if type == 'novelty search':
            NoveltyStatus(uid=uid, status=False).save()
        if type == 'drafting':
            DraftingStatus(uid=uid, status=False).save()
        if type == 'drawing':
            DrawingStatus(uid=uid, status=False).save()
        if type == 'documentation':
            DocumentationStatus(uid=uid, status=False).save()
        if type == 'filing':
            FilingStatus(uid=uid, status=False).save()
        if type == 'examination':
            ExaminationSatus(uid=uid, status=False).save()
        if type == 'FER':
            FerStatus(uid=uid, status=False).save()
        if type == 'hearing':
            HearingStatus(uid=uid, status=False).save()
        GrantsStatus(uid=uid, status=False).save()
        PaymentStatus(uid=uid, status=False).save()
        return redirect('home')
    else:
        return render(request, "Patent/Patentapplication.html")


def Documentationstatusview(r, uid):
    return render(r, "Patent/Documentationstatus.html")


def Documentationtableview(r):
    return render(r, "Patent/Documentationtable.html")


def Draftingstatusview(r, uid):
    return render(r, "Patent/Draftingstatus.html")


def Draftingtableview(r):
    return render(r, "Patent/Draftingtable.html")


def Drawingstatusview(r, uid):
    return render(r, "Patent/Drawingstatus.html")


def Drawingtableview(r):
    return render(r, "Patent/Drawingtable.html")


def Patentabilitysearchstatusview(r, uid):
    return render(r, "Patent/Patentabilitysearchstatus.html")


def Patentabilitysearchtableview(r):
    return render(r, "Patent/Patentabilitysearchtable.html")
