# support/urls.py
from django.urls import path
from .views import SupportTicketListView, SupportTicketDetailView

urlpatterns = [
    path('tickets/', SupportTicketListView.as_view(), name='ticket_list'),
    path('tickets/<int:pk>/', SupportTicketDetailView.as_view(), name='ticket_detail'),
]
