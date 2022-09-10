from django.urls import path
from . import views
urlpatterns=[
    path("table/",views.Copyrighttableview,name= 'Copyright/<str:uid>'),
    path("application/",views.Copyrightapplicationview,name= 'Copyright/<str:uid>'),
    path("status/",views.Copyrightstatusview,name= 'Copyright/<str:uid>'),
]