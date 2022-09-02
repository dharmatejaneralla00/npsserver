from django.urls import path
from . import views
urlpatterns=[
    path("fullpatentapplication",views.FullPatentapplication),
    path("patentapplication",views.Patentapplication),
    path("documentationstatus",views.Documentationstatus),
    path("documentationtable",views.Documentationtable),
    path("draftingstatus",views.Draftingstatus),
    path("draftingtable",views.Draftingtable),
    path("drawingstatus",views.Drawingstatus),
    path("drawingtable",views.Drawingtable),
    path("patentabilitysearchstatus",views.Patentabilitysearchstatus),
    path("patentabilitysearchtable",views.Patentabilitysearchtable),
]