from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Travel


# Create your views here.
def home(request):
    obj=Place.objects.all()
    obj1=Travel.objects.all()

    return render(request,"index.html",{'result':obj,'values':obj1})












# def operation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     subt=x-y
#
#
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     multi=x*y
#
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     divi=x/y
#
#
#
#
#     return render(request,"result_add.html",{'result':res,'sub':subt,'mult':multi,'div':divi})

# def about(request):
#     return render(request,"result_add.html")
#
#
# def contact(request):
#     return HttpResponse("programer")
#
#
# def details(request):
#     return HttpResponse("tech word")
#
# def thanks(request):
#     return HttpResponse("tech man")
