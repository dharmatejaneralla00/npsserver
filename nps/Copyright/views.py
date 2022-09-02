from django.shortcuts import render

# Create your views here.
def Copyrighttable(r):
    return render(r,"copyright/Copyrighttable.html")

def Copyrightstatus(r):
    return render(r,"copyright/Copyrightstatus.html")

def Copyrightapplication(r):
    return render(r,"copyright/Copyrightapplication.html")