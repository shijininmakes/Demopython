from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages, auth

from store.forms import OrderForm, LoginForm, RegistrationForm
from store.models import Department, Course, Material


def home(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'home.html', context)

def department(request, department_id):
    try:
        department = Department.objects.get(id=department_id)
        wikipedia_link = department.wikipedia_link
        return redirect(wikipedia_link)
    except Department.DoesNotExist:
        return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('new_page')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def new_page(request):
    departments = Department.objects.all()
    courses = Course.objects.filter(department__name=departments.name)

    materials = Material.objects.all()
    context = {'departments': departments, 'courses': courses, 'materials': materials}
    return render(request, 'new_page.html', context)


@login_required
def user_profile(request):
    user = request.user
    return render(request, 'user_profile.html', {'user': user})


def confirmation(request):
    message='order confirmed'
    context={'message':message}
    return render(request, 'confirmation.html',context)


def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation', message='order confirmed')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})
