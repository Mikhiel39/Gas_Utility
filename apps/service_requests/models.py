from django.db import models
from django.conf import settings
from django.urls import reverse


class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('GAS_REPAIR', 'Gas Repair'),
        ('BILLING', 'Billing Issue'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='service_requests')
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    details = models.TextField()
    attachment = models.FileField(
        upload_to='attachments/', blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request {self.id} by {self.user.username}"

    def get_absolute_url(self):
        return reverse('requests:request_detail', kwargs={'pk': self.pk})
