from django.urls import path
from .views import RequestListView, RequestDetailView, RequestCreateView

app_name = 'service_requests'

urlpatterns = [
    path('', RequestListView.as_view(), name='request_list'),
    path('<int:pk>/', RequestDetailView.as_view(), name='request_detail'),
    path('new/', RequestCreateView.as_view(), name='request_create'),
]
