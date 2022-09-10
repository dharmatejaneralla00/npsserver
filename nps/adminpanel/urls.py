from django.urls import path
from . import views
urlpatterns=[
    path("",views.adminpanel,name = 'adminpanel/<str:uid>')
]