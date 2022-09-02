from django.shortcuts import render

# Create your views here.
def FullPatentapplication(r):
    return render(r,"Patent/FullPatentapplication.html")

def Patentapplication(r):
    return render(r,"Patent/Patentapplication.html")

def Documentationstatus(r):
    return render(r,"Patent/Documentationstatus.html")

def Documentationtable(r):
    return render(r,"Patent/Documentationtable.html")

def Draftingstatus(r):
    return render(r,"Patent/Draftingstatus.html")

def Draftingtable(r):
    return render(r,"Patent/Draftingtable.html")

def Drawingstatus(r):
    return render(r,"Patent/Drawingstatus.html")

def Drawingtable(r):
    return render(r,"Patent/Drawingtable.html")

def Patentabilitysearchstatus(r):
    return render(r,"Patent/Patentabilitysearchstatus.html")

def Patentabilitysearchtable(r):
    return render(r,"Patent/Patentabilitysearchtable.html")

