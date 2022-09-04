from django.urls import path
from . import views
urlpatterns=[
    path("fullpatentapplication",views.FullPatentapplicationview),
    path("patentapplication",views.Patentapplicationview),
    path("documentationstatus",views.Documentationstatusview),
    path("documentationtable",views.Documentationtableview),
    path("draftingstatus",views.Draftingstatusview),
    path("draftingtable",views.Draftingtableview),
    path("drawingstatus",views.Drawingstatusview),
    path("drawingtable",views.Drawingtableview),
    path("patentabilitysearchstatus",views.Patentabilitysearchstatusview),
    path("patentabilitysearchtable",views.Patentabilitysearchtableview),
]