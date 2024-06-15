from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('userdata', views.userdata, name='userdata'),
    path('home', views.home, name='home'),
    path('editdata', views.editdata, name='editdata'),
    path('logout', views.logout, name='logout'),
    path('success', views.success, name='success'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('getid', views.getid, name='getid'),
    path('deletedata', views.deletedata, name='deletedata')
    
]