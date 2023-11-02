from . import views
from django.urls import path

urlpatterns =[
    path('',views.home,name='home'),
    path('login/', views.login, name='login'),
    path('newpage/', views.newpage, name='newpage'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('msg/',views.msg,name="msg")

]