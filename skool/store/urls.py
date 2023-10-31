from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
app_name='store'
urlpatterns = [

    path('', views.home, name='home'),
    path('department/<int:department_id>/', views.department, name='department'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('order_form/',views.order_form,name='order_form'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
