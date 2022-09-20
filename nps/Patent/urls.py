from django.urls import path
from . import views
urlpatterns=[
    path("fullpatentapplication",views.FullPatentapplicationview,name ='fullpatentapplication'),
    path("patentapplication",views.Patentapplicationview,name = 'patentapplication'),
    path("documentationstatus/<str:uid>",views.Documentationstatusview,name = 'documentationstatus'),
    path("documentationtable",views.Documentationtableview),
    path("draftingstatus/<str:uid>",views.Draftingstatusview,name = 'draftingstatus/'),
    path("draftingtable",views.Draftingtableview),
    path("drawingstatus/<str:uid>",views.Drawingstatusview,name = 'drawingstatus'),
    path("drawingtable",views.Drawingtableview),
    path("patentabilitysearchstatus/<str:uid>",views.Patentabilitysearchstatusview,name= 'patentabilitysearchstatus'),
    path("patentabilitysearchtable",views.Patentabilitysearchtableview)
]