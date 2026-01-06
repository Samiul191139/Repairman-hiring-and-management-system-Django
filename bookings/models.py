from django.db import models
from django.utils import timezone
from accounts.models import User
from services.models import Service

class Booking(models.Model):

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='customer_bookings'
    )

    repairman = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='repairman_bookings'
    )

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    booking_date = models.DateField()
    booking_time = models.TimeField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    address = models.TextField()

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking #{self.id} - {self.service.name}"
