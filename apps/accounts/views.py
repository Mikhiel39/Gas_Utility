from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .forms import CustomUserCreationForm
from .serializers import CustomUserSerializer


class RegisterView(TemplateView):
    template_name = 'accounts/register.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, self.template_name, {'form': form})


class LoginView(TemplateView):
    template_name = 'accounts/login.html'

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to the dashboard after successful login
            return redirect('dashboard')
        return render(request, self.template_name, {'form': form})


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'user': request.user})


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)
