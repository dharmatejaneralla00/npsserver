from django.urls import path
from . import views
urlpatterns=[
    path("table/",views.Copyrighttableview),
    path("application/",views.Copyrightapplicationview,name = 'cpoyrightapplication'),
    path("status/<str:uid>",views.Copyrightstatusview),
]