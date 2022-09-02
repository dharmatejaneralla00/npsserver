from django.urls import path
from . import views
urlpatterns=[
    path("application/",views.Trademarkapplication),
    path("status/", views.Trademarkstatus),
    path("table/", views.Trademarktable),

]