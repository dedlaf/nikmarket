from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'my-input-class'}),
            'last_name': forms.TextInput(attrs={'class': 'my-input-class'}),
            'email': forms.EmailInput(attrs={'class': 'my-input-class'}),
        }
