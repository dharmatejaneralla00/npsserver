from django.urls import path
from . import views
urlpatterns = [
    path('login', views.loginuser),
    path('register', views.registeruser),
    path('logout',views.logout),
    path('reset/<str:username>', views.resetpassword),
    path('', views.displayuser)
]