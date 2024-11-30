from django.contrib import admin
from .models import ServiceRequest


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'request_type',
                    'status', 'created_at', 'updated_at')
    list_filter = ('request_type', 'status', 'created_at')
    search_fields = ('user__username', 'details')
