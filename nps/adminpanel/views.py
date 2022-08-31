from django.shortcuts import render

# Create your views here.

def adminpanel(r):
    return render(r,"admin/admin.html")