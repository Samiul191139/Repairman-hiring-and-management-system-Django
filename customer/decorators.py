from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def customer_required(view_func):
    @login_required(login_url='login')
    def wrapper(request, *args, **kwargs):
        if request.user.role != 'CUSTOMER':
            messages.error(request, "Unauthorized access")
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper
