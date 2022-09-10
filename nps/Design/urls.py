from django.urls import path
from . import views
urlpatterns=[
    path("application/",views.Designapplicationview,name= 'Design/<str:uid>'),
    path("status/",views.Designstatusview,name= 'Design/<str:uid>'),
    path("table/",views.Designtableview,name= 'Design/<str:uid>'),
]