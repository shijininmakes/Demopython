from django.shortcuts import render

from .models import Place
from .models import Team

# Create your views here.


def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request, "index.html",{'result':obj,'obj1':obj1})

# def addition(request):
#     x=int(request.GET["num1"])
#     y=int(request.GET["num2"])
#     res=x+y
#     return render(request,"result.html",{'result':res})

# def contact(reqeuest):
#     return HttpResponse("hello am contact")
