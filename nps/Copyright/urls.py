from django.urls import path
from . import views
urlpatterns=[
    path("table/",views.Copyrighttableview),
    path("application/",views.Copyrightapplicationview,name = 'copyrightapplication'),
    path("status/<str:uid>",views.Copyrightstatusview),
]