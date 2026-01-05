from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'customer/home.html')

def login_view(request):
    return render(request, 'customer/login.html')

def register_view(request):
    return render(request, 'customer/register.html')

def services(request):
    return render(request, 'customer/services.html')

def booking(request):
    return render(request, 'customer/booking.html')

@login_required
def home(request):
    return render(request, 'customer/home.html')
