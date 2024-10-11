from django import forms
from .models import Session, CounselingSession
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class BookSession(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('Name', 'email', 'phone_number', 'Date', 'Time',)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data


class BookSessionForm(forms.Form):
    session_id = forms.ModelChoiceField(queryset=CounselingSession.objects.all())
