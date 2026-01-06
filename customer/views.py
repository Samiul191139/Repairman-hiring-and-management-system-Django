from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import customer_required
from bookings.models import Booking

@login_required
@customer_required
def dashboard(request):
    bookings = Booking.objects.filter(customer=request.user).order_by('-created_at')[:5]

    context = {
        'bookings': bookings,
    }
    return render(request, 'customer/dashboard.html', context)

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
