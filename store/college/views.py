from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect


def home(request):
    return render(request, "base.html")


def newpage(request):
    if request.method == 'POST':
        name = request.POST['name']
        DOB = request.POST['DOB']
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        Course = request.POST.get('Course')
        Purpose = request.POST.get('Purpose')
        Materialsprovide = request.POST.get('Materialsprovide')

        user = auth.authenticate(name=name, address=address, phone_number=phone_number, email=email, DOB=DOB, age=age,
                                 gender=gender, Course=Course, Purpose=Purpose, Materialsprovide=Materialsprovide,
                                 department=department)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Application Accepted")
            return redirect('/msg/')
    else:
        return render(request, "newpage.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            messages.info(request, "invaild username or password")
            return redirect('newpage')
    else:
        return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('register')
    return render(request, "register.html")


def msg(request):
    return render(request, 'msg.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
