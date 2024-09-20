from django import forms
from .models import Session
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookSession(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('Name', 'email', 'phone_number', 'Date', 'Time')


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

