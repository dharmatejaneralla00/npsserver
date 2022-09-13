from django.urls import path
from . import views
urlpatterns=[
    path("application/", views.Trademarkapplicationview),
    path("status//<str:uid>'", views.Trademarkstatusview),
    path("table/", views.Trademarktableview),

]