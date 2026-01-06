from django.shortcuts import redirect
from django.contrib import messages

def customer_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role != 'CUSTOMER':
            messages.error(request, "Unauthorized access")
            return redirect('customer_login')
        return view_func(request, *args, **kwargs)
    return wrapper
