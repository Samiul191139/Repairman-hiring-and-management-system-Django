from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/customer/', views.register_customer, name='register_customer'),
    path('register/repairman/', views.register_repairman, name='register_repairman'),
    path('logout/', views.logout_view, name='logout'),
]
