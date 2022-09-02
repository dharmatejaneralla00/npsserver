from django.urls import path
from . import views
urlpatterns=[
    path("table/",views.Copyrighttable),
    path("application/",views.Copyrightapplication),
    path("status/",views.Copyrightstatus),
]