from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import customer_required
from bookings.models import Booking
from accounts.models import RepairmanProfile
from services.models import ServiceCategory, Service

@login_required
@customer_required
def dashboard(request):
    # Example stats
    total_bookings = Booking.objects.filter(customer=request.user).count()
    completed_bookings = Booking.objects.filter(customer=request.user, status='Done').count()
    pending_bookings = Booking.objects.filter(customer=request.user, status__in=['Pending', 'Accepted', 'Working']).count()

    return render(request, 'customer/customer_dashboard.html', {
        'total_bookings': total_bookings,
        'completed_bookings': completed_bookings,
        'pending_bookings': pending_bookings
    })


def home(request):
    return render(request, 'customer/home.html')

def login_view(request):
    return render(request, 'customer/login.html')

def register_view(request):
    return render(request, 'customer/register.html')

@login_required
def services(request):
    categories = ServiceCategory.objects.prefetch_related('services').all()
    return render(request, 'customer/services.html', {'categories': categories})

@login_required
def repairman_list(request):
    # Fetch only available repairmen
    repairmen = RepairmanProfile.objects.filter(availability=True).select_related('user')
    return render(request, 'customer/repairman_list.html', {'repairmen': repairmen})

def create_booking(request):
    return render(request, 'customer/booking_form.html')

def booking_history(request):
    return render(request, 'customer/booking_history.html')

def profile(request):
    return render(request, 'customer/profile.html')

@login_required
def home(request):
    return render(request, 'customer/home.html')
