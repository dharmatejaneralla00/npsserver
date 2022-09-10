from django.urls import path
from . import views
urlpatterns=[
    path("fullpatentapplication",views.FullPatentapplicationview,name= 'Patent/<str:uid>'),
    path("patentapplication",views.Patentapplicationview,name= 'Patent/<str:uid>'),
    path("documentationstatus",views.Documentationstatusview,name= 'Patent/<str:uid>'),
    path("documentationtable",views.Documentationtableview,name= 'Patent/<str:uid>'),
    path("draftingstatus",views.Draftingstatusview,name= 'Patent/<str:uid>'),
    path("draftingtable",views.Draftingtableview,name= 'Patent/<str:uid>'),
    path("drawingstatus",views.Drawingstatusview,name= 'Patent/<str:uid>'),
    path("drawingtable",views.Drawingtableview,name= 'Patent/<str:uid>'),
    path("patentabilitysearchstatus",views.Patentabilitysearchstatusview,name= 'Patent/<str:uid>'),
    path("patentabilitysearchtable",views.Patentabilitysearchtableview,name= 'Patent/<str:uid>'),
]