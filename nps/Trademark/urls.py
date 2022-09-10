from django.urls import path
from . import views
urlpatterns=[
    path("application/", views.Trademarkapplicationview,name='Trademark/<str:uid>'),
    path("status/", views.Trademarkstatusview,name='Trademark/<str:uid>'),
    path("table/", views.Trademarktableview,name='Trademark/<str:uid>'),

]