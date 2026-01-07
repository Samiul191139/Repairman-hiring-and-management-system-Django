from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'ADMIN')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('CUSTOMER', 'Customer'),
        ('REPAIRMAN', 'Repairman'),
        ('ADMIN', 'Admin'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.email





class RepairmanProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    skills = models.TextField(help_text="Electrical, AC, Plumbing, etc.")
    experience_years = models.PositiveIntegerField()

    price_per_service = models.DecimalField(max_digits=10, decimal_places=2)

    availability = models.BooleanField(default=True)

    nid_number = models.CharField(max_length=30)

    documents = models.FileField(upload_to='repairman_documents/', null=True, blank=True)

    rating = models.FloatField(default=0.0)
    total_jobs = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.email
    

# class ServiceCategory(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     icon = models.ImageField(upload_to='service_category_icons/')

#     def __str__(self):
#         return self.name
    

# class Service(models.Model):
#     category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
#     name = models.CharField(max_length=100)
#     base_price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()

#     def __str__(self):
#         return self.name


