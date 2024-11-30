# support/views.py
from django.views.generic import ListView, DetailView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from apps.service_requests.models import ServiceRequest


@method_decorator(staff_member_required, name='dispatch')
class SupportTicketListView(ListView):
    model = ServiceRequest
    template_name = 'support/ticket_list.html'
    context_object_name = 'tickets'
    paginate_by = 10

    def get_queryset(self):
        return ServiceRequest.objects.filter(status__in=['PENDING', 'IN_PROGRESS'])


@method_decorator(staff_member_required, name='dispatch')
class SupportTicketDetailView(DetailView):
    model = ServiceRequest
    template_name = 'support/ticket_detail.html'
    context_object_name = 'ticket'
