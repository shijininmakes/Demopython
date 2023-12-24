from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def demo(request):
#     return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return HttpResponse("hello am contact")
def home(request):
    return render(request,"home.html")
def details(request):
    return render(request,"details.html")
def thanks(request):
    return HttpResponse(" thanks")
