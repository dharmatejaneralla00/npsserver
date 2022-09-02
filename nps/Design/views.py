from django.shortcuts import render

# Create your views here.
def Designapplication(r):
    return render(r,"Design/Designapplication.html")

def Designtable(r):
    return render(r,"Design/Designtable.html")

def Designstatus(r):
    return render(r,"Design/Designstatus.html")