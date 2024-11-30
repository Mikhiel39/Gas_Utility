from django.urls import path
from .views import RegisterView, LoginView, dashboard, ProfileAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
]
