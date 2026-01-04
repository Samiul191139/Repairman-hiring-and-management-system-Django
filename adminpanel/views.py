from django.shortcuts import render

def dashboard(request):
    return render(request, 'adminpanel/dashboard.html')

def login_view(request):
    return render(request, 'adminpanel/login.html')

def users(request):
    return render(request, 'adminpanel/users.html')