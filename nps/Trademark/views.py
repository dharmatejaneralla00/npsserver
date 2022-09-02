from django.shortcuts import render

# Create your views here.
def Trademarkapplication(r):
    return render(r,"Trademark/Trademarkapplication.html")

def Trademarkstatus(r):
    return render(r,"Trademark/Trademarkstatus.html")

def Trademarktable(r):
    return render(r,"Trademark/Trademarktable.html")