from django.urls import path
from . import views
urlpatterns=[
    path("application/>",views.Designapplicationview),
    path("status/<str:uid>'",views.Designstatusview),
    path("table/",views.Designtableview),
]