import operator
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def demo(request):
    return render(request,"index.html")
def addition(request):
     x=int(request.GET["num1"])
     y = int(request.GET["num2"])
    #  operator=request.GET['+']
    #  if operator=='+':
    #      res=x+y
    #  elif operator=='-':
    #     res=x-y
    #  elif operator=='*':
    #     res=x*y
    #  elif operator=='/':
    #     if y !=0:
    #         res=x/y
    #     else:
    #         return render({'error':'cannot divide by zero'})
    #  else:
    #     return render({'error':'invalid operator'})
    #  return render(request,"result.html",{'result':res})
def multiplication(request):
    x = int(request.GET["num1"])
    y = int(request.GET["num2"])
    res=x*y
    return render(request,"result.html",{'result':res})
def subtraction(request):
    x = int(request.GET["num1"])
    y = int(request.GET["num2"])
    res=x-y
    return render(request,"result.html",{'result':res})
def division(request):
    x = float(request.GET["num1"])
    y = float(request.GET["num2"])

    if y !=0:
        res = x / y
    else:
        return render({'error':'cannotdivided by zero'})
        # else:
        # return render({'error':'invaild error'})

    return render(request,"result.html",{'result':res})
