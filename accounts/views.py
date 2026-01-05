from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, CustomerProfile


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)

            if user.role == 'CUSTOMER':
                return redirect('customer_home')
            elif user.role == 'REPAIRMAN':
                return redirect('repairman_dashboard')
            else:
                return redirect('admin_dashboard')

    return render(request, 'accounts/login.html')

def register_customer(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            email=request.POST['email'],
            password=request.POST['password'],
            name=request.POST['name'],
            phone=request.POST['phone'],
            role='CUSTOMER'
        )

        CustomerProfile.objects.create(
            user=user,
            address=request.POST['address']
        )

        return redirect('login')

    return render(request, 'accounts/register_customer.html')

def register_repairman(request):
    if request.method == 'POST':
        User.objects.create_user(
            email=request.POST['email'],
            password=request.POST['password'],
            name=request.POST['name'],
            phone=request.POST['phone'],
            role='REPAIRMAN'
        )
        return redirect('login')

    return render(request, 'accounts/register_repairman.html')

def logout_view(request):
    logout(request)
    return redirect('login')
