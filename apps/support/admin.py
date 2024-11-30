# support/admin.py
from django.contrib import admin
from apps.service_requests.models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'request_type', 'status', 'created_at')
    list_filter = ('status', 'request_type')
    search_fields = ('user__username', 'details')

# No need to register the model again here
