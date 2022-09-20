from django.urls import path
from . import views

urlpatterns = [
    path("", views.adminpanel, name='adminpanel'),
    path('editapplication/<str:uid>', views.Editapplication, name='editapplication'),
    path('dashboard',views.dashboard),
    path('ndastatus',views.ndsatatus,name = 'ndastatus'),
    path('closeapplication',views.closeapplication,name = 'closeapplication'),
    path('FilingStatus',views.filingstatus,name = 'FilingStatus')
]
