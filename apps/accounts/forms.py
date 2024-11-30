from django import forms
from apps.accounts.models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'address', 'phone_number']

    password = forms.CharField(widget=forms.PasswordInput())
