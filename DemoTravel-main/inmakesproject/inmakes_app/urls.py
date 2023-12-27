from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home')
    # path('arithematic/',views.operation,name="operation"),
    # path('contact/',views.contact,name='contact'),
    # path('details/',views.details,name='details'),
    # path('thanks/',views.thanks,name='thanks')
]
