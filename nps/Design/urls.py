from django.urls import path
from . import views
urlpatterns=[
    path("application/",views.Designapplication),
    path("status/",views.Designstatus),
    path("table/",views.Designtable),
]