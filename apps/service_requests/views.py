from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ServiceRequest


class RequestListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'service_requests/request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class RequestDetailView(LoginRequiredMixin, DetailView):
    model = ServiceRequest
    template_name = 'service_requests/request_detail.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class RequestCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRequest
    fields = ['request_type', 'details', 'attachment']
    template_name = 'service_requests/request_form.html'
    success_url = '/requests/'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the logged-in user
        return super().form_valid(form)
