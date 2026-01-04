from django.shortcuts import render

def dashboard(request):
    return render(request, 'repairman/dashboard.html')

def login_view(request):
    return render(request, 'repairman/login.html')

def register_view(request):
    return render(request, 'repairman/register.html')

def requests(request):
    return render(request, 'repairman/requests.html')
