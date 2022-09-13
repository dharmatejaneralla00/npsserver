from django.urls import path
from . import views
urlpatterns=[
    path("fullpatentapplication",views.FullPatentapplicationview,name ='fullpatentapplication'),
    path("patentapplication",views.Patentapplicationview,name = 'patentapplication'),
    path("documentationstatus/<str:uid>'",views.Documentationstatusview),
    path("documentationtable",views.Documentationtableview),
    path("draftingstatus/<str:uid>'",views.Draftingstatusview),
    path("draftingtable",views.Draftingtableview),
    path("drawingstatus/<str:uid>'",views.Drawingstatusview),
    path("drawingtable",views.Drawingtableview),
    path("patentabilitysearchstatus/<str:uid>'",views.Patentabilitysearchstatusview),
    path("patentabilitysearchtable",views.Patentabilitysearchtableview),
    path("editapplication",views.Editapplicationview),
]