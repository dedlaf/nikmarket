from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, User, Task

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'my-input-class'}),
            'last_name': forms.TextInput(attrs={'class': 'my-input-class'}),
            'email': forms.EmailInput(attrs={'class': 'my-input-class'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'main_cont', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'text-title'}),
            'main_cont': forms.Textarea(attrs={'class': 'area-main'}),
        }


class RegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'my-input-class', 'placeholder': 'Логин', 'name': 'login'}),
            'first_name': forms.TextInput(attrs={'class': 'my-input-class', 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'my-input-class', 'placeholder': 'Фамилия'}),
            'email': forms.TextInput(attrs={'class': 'my-input-class', 'placeholder': 'Номер телефона'}),
            'password': forms.PasswordInput(attrs={'class': 'my-input-class', 'placeholder': 'Пароль'}),
        }