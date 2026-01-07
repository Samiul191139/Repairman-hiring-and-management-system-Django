from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import RepairmanProfileForm

@login_required
def dashboard(request):
    profile = getattr(request.user, 'repairmanprofile', None)

    show_modal = False
    form = None

    if not profile or not profile.is_complete:
        show_modal = True
        form = RepairmanProfileForm(instance=profile)

    return render(request, 'repairman/dashboard.html', {
        'show_modal': show_modal,
        'form': form
    })


def login_view(request):
    return render(request, 'repairman/login.html')


def register_view(request):
    return render(request, 'repairman/register.html')


@login_required
def requests(request):
    # Optional: also protect this page
    if not hasattr(request.user, 'repairmanprofile'):
        return redirect('repairman_profile_setup')

    return render(request, 'repairman/requests.html')
