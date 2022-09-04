from django.urls import path
from . import views
urlpatterns=[
    path("table/",views.Copyrighttableview),
    path("application/",views.Copyrightapplicationview),
    path("status/",views.Copyrightstatusview),
]