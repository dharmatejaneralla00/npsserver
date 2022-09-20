from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginuser,name = 'user/login'),
    path('register', views.registeruser),
    path('logout', views.logoutuser, name='user/logout'),
    path('reset/<str:username>', views.resetpassword,name = 'resetpass'),
    # path('reset/resetpass/<str:username>', views.resetpassword,name = 'resetpass'),
    path('', views.displayuser,name = 'user/displayuser'),
    path('referedby', views.referedby,name = 'user/referedby')
]
