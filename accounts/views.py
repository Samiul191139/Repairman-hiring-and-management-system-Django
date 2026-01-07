from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, CustomerProfile, RepairmanProfile
from .forms import RepairmanProfileForm



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)

            if user.role == 'CUSTOMER':
                return redirect('customer_dashboard')
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

@login_required
def repairman_profile_setup(request):
    form = RepairmanProfileForm(instance=request.user.repairmanprofile)

    if request.method == 'POST':
        form = RepairmanProfileForm(request.POST, request.FILES, instance=request.user.repairmanprofile)
        if form.is_valid():
            form.save()
            return redirect('repairman_dashboard')

    return render(request, 'repairman/profile_setup_modal.html', {
        'form': form,
        'show_modal': True
    })


def logout_view(request):
    logout(request)
    return redirect('login')
